# FPA Value Chain MC — 10Y FP&A, Value-Chain, Fat-Tail Monte Carlo & AI/Triad Stock Analyzer (v3.1)

An institutional-grade Antigravity agent skill implementing a 9-Phase equity analysis framework for any stock ticker, combined with direct SEC EDGAR XBRL data extraction and a self-contained, zero-CDN print-ready HTML/CSS dashboard engine.

## Repository Structure

```text
fpa-valuechain-mc/
├── SKILL.md                      # Main Antigravity skill specification (Phases 1–9)
├── scripts/
│   └── fetch_sec_edgar.py        # Direct SEC EDGAR XBRL JSON API extractor (10-K & 10-Q)
├── examples/
│   └── nvda/
│       ├── index.html            # Verified NVDA dashboard updated through Q3 FY27 (Nov 17, 2026 8-K)
│       └── nvda_sec_xbrl.json    # Extracted SEC XBRL 10Y + quarterly dataset (CIK 0001045810)
└── README.md
```

## Key Capabilities

- **Direct SEC EDGAR XBRL Integration (`scripts/fetch_sec_edgar.py`):** Resolves any US ticker to its 10-digit CIK and fetches audited US GAAP 10-K (10 years) and 10-Q (with automatic YTD-to-standalone cash flow differencing) facts directly from `data.sec.gov/api/xbrl/companyfacts/`. Eliminates missing sub-lines (`D&A`, `SBC`, `Effective Tax Rate`, `Interest Expense`, `Operating Leases`, `CapEx/D&A`, `Owner FCF`, `Unlevered FCFF`, `Incremental ROIC`).
- **2-Wave Search + Strict Provenance Floor:** Enforces inline epistemic tags (`[FILING]`, `[CONSENSUS]`, `[PROXY]`, `[ASSUMP]`, `[SIM]`) and a strict `N/A` zero-fabrication policy for undisclosed metrics.
- **Full FP&A & Cost-Leverage Diagnostics:** Includes 10-year financial schedules, Cost-Volume-Profit (CVP Variable vs. Fixed Cost proxy, Break-Even Sales, Margin of Safety, Empirical DOL), Working Capital (`OC`, `DSO/DIO/DPO`, `CCC`), 3-Step DuPont ROE tree, Direct Competitor & Value-Chain Supplier Benchmarking, and Consulting Visual Suite (Patterns A, B, C).
- **10-Dimension Objective Rubric & Fat-Tail Monte Carlo:** Deterministic scoring (`0–100`) mapped to `PASS / CONDITIONAL PASS / GREY ZONE / FAIL`, Jack Alexander Table 22.1/22.2 DCF, and a 10,000-run Student-t (`df=5`) + 10% bear-jump Monte Carlo simulator with `CVaR 95%`.
- **Zero-CDN Print-Ready HTML Engine:** Pure HTML/CSS + inline SVG polylines with A4 landscape print-to-PDF support.

## Installation in Antigravity

Copy or clone this folder into either:
- **Workspace-level:** `<your-workspace>/.agents/skills/fpa-valuechain-mc/`
- **Global-level (all workspaces):** `~/.gemini/config/skills/fpa-valuechain-mc/`

## Standalone SEC EDGAR Script Usage

```bash
python scripts/fetch_sec_edgar.py NVDA --years 10 --quarters 6 --out nvda_sec_xbrl.json
```
