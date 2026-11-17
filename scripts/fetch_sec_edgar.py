#!/usr/bin/env python3
"""
SEC EDGAR XBRL Direct Extractor for AI-Berkshire FP&A Stock Analyzer (v3.1)
Fetches official US GAAP 10-K & 10-Q line items from data.sec.gov/api/xbrl/companyfacts/
to eliminate missing sub-lines (D&A, SBC, Tax, Interest, Leases, CapEx) for US tickers.
"""
import argparse
import datetime
import json
import os
import sys
import urllib.request

USER_AGENT = os.environ.get(
    "SEC_USER_AGENT", "AIBerkshireAnalyzer/3.1 (research@aiberkshire.local)"
)

TAG_MAP = {
    "revenue": [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "SalesRevenueNet",
        "SalesRevenueGoodsNet",
    ],
    "gross_profit": ["GrossProfit"],
    "cogs": ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"],
    "rd": [
        "ResearchAndDevelopmentExpense",
        "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
    ],
    "sga": ["SellingGeneralAndAdministrativeExpense", "GeneralAndAdministrativeExpense"],
    "ebit": ["OperatingIncomeLoss"],
    "ebt": [
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
    ],
    "tax": ["IncomeTaxExpenseBenefit"],
    "net_income": ["NetIncomeLoss", "ProfitLoss"],
    "interest_expense": [
        "InterestExpenseNonoperating",
        "InterestExpense",
        "InterestAndDebtExpense",
    ],
    "da": [
        "DepreciationDepletionAndAmortization",
        "DepreciationAndAmortization",
        "Depreciation",
    ],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
    "cfo": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": [
        "PaymentsToAcquireProductiveAssets",
        "PaymentsToAcquirePropertyPlantAndEquipment",
    ],
    "cash": [
        "CashAndCashEquivalentsAtCarryingValue",
        "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
    ],
    "marketable_sec": [
        "MarketableSecuritiesCurrent",
        "AvailableForSaleSecuritiesDebtSecurities",
        "ShortTermInvestments",
    ],
    "cash_and_st_inv": ["CashCashEquivalentsAndShortTermInvestments"],
    "ar": ["AccountsReceivableNetCurrent", "ReceivablesNetCurrent"],
    "inventory": ["InventoryNet", "Inventories"],
    "ap": ["AccountsPayableCurrent"],
    "st_debt": ["LongTermDebtCurrent", "DebtCurrent", "ShortTermBorrowings"],
    "lt_debt": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"],
    "lease_liab": ["OperatingLeaseLiability"],
    "assets": ["Assets"],
    "equity": [
        "StockholdersEquity",
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
    ],
    "nci": ["MinorityInterest"],
    "diluted_shares": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
}


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve_cik(ticker: str) -> tuple[str, str]:
    ticker_up = ticker.strip().upper()
    if ticker_up.isdigit():
        return ticker_up.zfill(10), f"CIK-{ticker_up.zfill(10)}"
    tickers_data = fetch_json("https://www.sec.gov/files/company_tickers.json")
    for entry in tickers_data.values():
        if entry.get("ticker", "").upper() == ticker_up:
            return str(entry["cik_str"]).zfill(10), entry.get("title", ticker_up)
    raise ValueError(f"Ticker '{ticker}' not found in SEC company_tickers.json")


def _days_between(start: str, end: str) -> int:
    d1 = datetime.date.fromisoformat(start)
    d2 = datetime.date.fromisoformat(end)
    return (d2 - d1).days


def extract_fact_series(us_gaap: dict, tags: list[str], mode: str, is_shares: bool = False) -> dict[str, dict]:
    """
    Extract deduplicated values keyed by end_date ('YYYY-MM-DD').
    mode: 'annual' (10-K, 330-385 days for duration; any 10-K instant)
          'quarter' (10-Q/10-K, 70-105 days standalone; falls back to YTD differencing for CF/D&A)
    Prefers higher-priority tag order, and for the same tag/end_date prefers latest filed date.
    """
    out: dict[str, dict] = {}
    ytd_by_start: dict[str, list[dict]] = {}
    unit_pref = ("shares",) if is_shares else ("USD",)
    for tag in tags:
        node = us_gaap.get(tag)
        if not node or "units" not in node:
            continue
        unit_key = next((u for u in unit_pref if u in node["units"]), None)
        if not unit_key:
            continue
        for item in node["units"][unit_key]:
            form = item.get("form", "")
            end = item.get("end")
            start = item.get("start")
            filed = item.get("filed", "")
            val = item.get("val")
            if not end or val is None:
                continue
            scale = 1.0 if is_shares else 1e6
            norm_val = round(val / scale, 2)
            if mode == "annual":
                if form not in ("10-K", "10-K/A"):
                    continue
                if start is not None and not (330 <= _days_between(start, end) <= 385):
                    continue
            elif mode == "quarter":
                if form not in ("10-Q", "10-Q/A", "10-K", "10-K/A"):
                    continue
                if start is not None:
                    days = _days_between(start, end)
                    if 150 <= days <= 290:
                        ytd_by_start.setdefault(start, []).append(
                            {"end": end, "days": days, "val_m": norm_val, "tag": tag, "form": form, "fp": item.get("fp", ""), "filed": filed}
                        )
                        continue
                    if not (70 <= days <= 105):
                        continue
            prev = out.get(end)
            if prev is None or (prev["tag"] == tag and filed >= prev["filed"]):
                out[end] = {
                    "val_m": norm_val,
                    "tag": tag,
                    "form": form,
                    "fp": item.get("fp", ""),
                    "filed": filed,
                    "start": start,
                }
    if mode == "quarter" and ytd_by_start:
        # Derive standalone Q2/Q3 from cumulative YTD facts when standalone quarter wasn't tagged
        for fy_start, items in ytd_by_start.items():
            # Include Q1 standalone with same fiscal start
            q1_match = [v | {"end": k} for k, v in out.items() if v.get("start") == fy_start]
            combined = {}
            for row in q1_match + items:
                e = row["end"]
                if e not in combined or row["filed"] >= combined[e]["filed"]:
                    combined[e] = row
            seq = sorted(combined.values(), key=lambda x: x["end"])
            for i in range(1, len(seq)):
                prev_r, curr_r = seq[i - 1], seq[i]
                if curr_r["end"] not in out:
                    out[curr_r["end"]] = {
                        "val_m": round(curr_r["val_m"] - prev_r["val_m"], 2),
                        "tag": curr_r["tag"] + " (YTD-diff)",
                        "form": curr_r["form"],
                        "fp": curr_r["fp"],
                        "filed": curr_r["filed"],
                        "start": prev_r["end"],
                    }
    return out


def build_period_record(end_date: str, series_map: dict[str, dict], period_days: float = 365.0) -> dict:
    rec = {"end_date": end_date, "source": "[FILING] SEC EDGAR XBRL"}
    tags_used = {}
    for field, by_end in series_map.items():
        if end_date in by_end:
            rec[field] = by_end[end_date]["val_m"]
            tags_used[field] = by_end[end_date]["tag"]
        else:
            rec[field] = None

    # Derive missing COGS from Revenue - GrossProfit if needed
    if rec["cogs"] is None and rec["revenue"] is not None and rec["gross_profit"] is not None:
        rec["cogs"] = round(rec["revenue"] - rec["gross_profit"], 2)
    if rec["gross_profit"] is None and rec["revenue"] is not None and rec["cogs"] is not None:
        rec["gross_profit"] = round(rec["revenue"] - rec["cogs"], 2)

    # Cash + Marketable Securities reconciliation
    if rec["cash"] is not None and rec["marketable_sec"] is not None:
        rec["cash_and_ms"] = round(rec["cash"] + rec["marketable_sec"], 2)
    elif rec["cash_and_st_inv"] is not None:
        rec["cash_and_ms"] = rec["cash_and_st_inv"]
    else:
        rec["cash_and_ms"] = rec["cash"]

    # Debt incl. operating leases
    st = rec["st_debt"] or 0.0
    lt = rec["lt_debt"] or 0.0
    lease = rec["lease_liab"] or 0.0
    if rec["st_debt"] is not None or rec["lt_debt"] is not None:
        rec["debt_excl_lease"] = round(st + lt, 2)
        rec["debt_incl_lease"] = round(st + lt + lease, 2)
    else:
        rec["debt_excl_lease"] = None
        rec["debt_incl_lease"] = None

    # Jack Alexander FP&A Metrics
    rev = rec["revenue"]
    gp = rec["gross_profit"]
    ebit = rec["ebit"]
    ebt = rec["ebt"]
    tax = rec["tax"]
    ni = rec["net_income"]
    cfo = rec["cfo"]
    capex = rec["capex"]
    da = rec["da"]
    sbc = rec["sbc"]
    intr = rec["interest_expense"]

    rec["gm_pct"] = round(gp / rev * 100, 2) if gp is not None and rev else None
    rec["rd_pct"] = round(rec["rd"] / rev * 100, 2) if rec["rd"] is not None and rev else None
    rec["sga_pct"] = round(rec["sga"] / rev * 100, 2) if rec["sga"] is not None and rev else None
    rec["ebit_pct"] = round(ebit / rev * 100, 2) if ebit is not None and rev else None
    rec["eff_tax_rate_pct"] = (
        round(tax / ebt * 100, 2) if tax is not None and ebt and ebt > 0 else None
    )
    t_dec = (rec["eff_tax_rate_pct"] / 100.0) if rec["eff_tax_rate_pct"] is not None else None
    rec["opat"] = round(ebit * (1.0 - t_dec), 2) if ebit is not None and t_dec is not None else None
    rec["ebitda"] = round(ebit + da, 2) if ebit is not None and da is not None else None
    rec["std_fcf"] = round(cfo - capex, 2) if cfo is not None and capex is not None else None
    rec["capex_pct"] = round(capex / rev * 100, 2) if capex is not None and rev else None
    rec["capex_to_da"] = round(capex / da, 2) if capex is not None and da and da > 0 else None
    rec["fcf_ebitda_pct"] = (
        round(rec["std_fcf"] / rec["ebitda"] * 100, 2)
        if rec["std_fcf"] is not None and rec["ebitda"] and rec["ebitda"] > 0
        else None
    )
    rec["unlevered_fcff"] = (
        round(rec["std_fcf"] + (intr or 0.0) * (1.0 - (t_dec or 0.0)), 2)
        if rec["std_fcf"] is not None
        else None
    )
    rec["owner_fcf"] = (
        round(rec["std_fcf"] - (sbc or 0.0), 2)
        if rec["std_fcf"] is not None and sbc is not None
        else None
    )
    rec["interest_coverage"] = (
        round(ebit / intr, 1) if ebit is not None and intr and intr > 0 else None
    )

    # Working Capital & DuPont
    ar, inv, ap = rec["ar"], rec["inventory"], rec["ap"]
    cogs = rec["cogs"]
    if ar is not None and inv is not None and ap is not None:
        rec["core_oc"] = round(ar + inv - ap, 2)
        if rev and cogs and cogs > 0:
            rec["dso"] = round(ar / rev * period_days, 1)
            rec["dio"] = round(inv / cogs * period_days, 1)
            rec["dpo"] = round(ap / cogs * period_days, 1)
            rec["ccc_days"] = round(rec["dso"] + rec["dio"] - rec["dpo"], 1)
    ast, eq = rec["assets"], rec["equity"]
    if ni is not None and rev and ast and eq and eq > 0:
        nm = ni / rev * 100
        at = rev / ast
        em = ast / eq
        rec["dupont_nm_pct"] = round(nm, 2)
        rec["dupont_at_x"] = round(at, 3)
        rec["dupont_em_x"] = round(em, 3)
        rec["dupont_roe_pct"] = round(nm * at * em, 2)
    rec["tags_used"] = tags_used
    return rec


def analyze_ticker(ticker: str, years: int = 10, quarters: int = 6) -> dict:
    cik, entity_name = resolve_cik(ticker)
    facts_url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    facts = fetch_json(facts_url)
    us_gaap = facts.get("facts", {}).get("us-gaap", {})
    if not us_gaap:
        raise ValueError(f"No us-gaap XBRL facts found for {ticker} (CIK {cik})")

    ann_series = {
        k: extract_fact_series(us_gaap, tags, "annual", is_shares=(k == "diluted_shares"))
        for k, tags in TAG_MAP.items()
    }
    ann_dates = sorted(ann_series["revenue"].keys())[-years:]
    annual = [build_period_record(d, ann_series) for d in ann_dates]

    # Empirical DOL across consecutive annual periods
    for i in range(1, len(annual)):
        p, c = annual[i - 1], annual[i]
        if p["revenue"] and c["revenue"] and p["ebit"] and c["ebit"]:
            ds = (c["revenue"] - p["revenue"]) / p["revenue"]
            de = (c["ebit"] - p["ebit"]) / abs(p["ebit"])
            c["empirical_dol"] = round(de / ds, 2) if abs(ds) >= 0.01 else None

    qtr_series = {
        k: extract_fact_series(us_gaap, tags, "quarter", is_shares=(k == "diluted_shares"))
        for k, tags in TAG_MAP.items()
    }
    qtr_dates = sorted(qtr_series["revenue"].keys())[-quarters:]
    quarterly = [build_period_record(d, qtr_series, period_days=91.25) for d in qtr_dates]

    return {
        "ticker": ticker.upper(),
        "cik": cik,
        "entity_name": facts.get("entityName", entity_name),
        "source_url": facts_url,
        "units": "USD Millions (except ratios, days, and shares in millions)",
        "annual": annual,
        "quarterly": quarterly,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch SEC EDGAR XBRL facts for US stocks")
    parser.add_argument("ticker", help="US Stock Ticker (e.g., NVDA, AAPL, MSFT)")
    parser.add_argument("--years", type=int, default=10, help="Number of annual 10-K periods")
    parser.add_argument("--quarters", type=int, default=6, help="Number of standalone quarters")
    parser.add_argument("--out", help="Output JSON file path")
    args = parser.parse_args()

    result = analyze_ticker(args.ticker, args.years, args.quarters)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"Saved {result['ticker']} (CIK {result['cik']}) to {args.out}")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
