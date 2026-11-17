---
name: ai-berkshire-fpa-mc-stock-analyzer
description: Analyzes any stock ticker using the full 9-Phase AI-Berkshire adversarial framework, Data Provenance & Epistemic Tagging ([FILING]/[CONSENSUS]/[PROXY]/[ASSUMP]/[SIM]), 2-Layer Plain + Institutional FP&A explanations, Jack Alexander FP&A standard formulas, Full Cost-Leverage & Commercial Driver Diagnostics (CapEx/D&A, OpEx, HC, OHC, FC/VC, DOL, PVM, Book-to-Bill/NRR, Cash Conversion, Covenants & Utilization), 10-year financial schedule, 3-Step DuPont ROE, Direct Competitor & Value-Chain Supplier Benchmarking, Consulting Visual Suite (Patterns A, B, C), Time-Series ML, 10-Dimension Objective Rubric, Fat-Tail 10,000-run Monte Carlo simulation (Student-t + CVaR 95%), and Phase 8 AI/Headcount/Triad Growth—combining full 2-wave data depth with a zero-CDN Pure HTML/CSS Print-Ready engine to eliminate 500 TURN_STEPS_EXCEEDED errors.
---

# AI-Berkshire 10Y FP&A, Value-Chain, Fat-Tail Monte Carlo & AI/Triad Stock Analyzer (v3.1 — Full 2-Wave + Complete FP&A Cost/Leverage/Drivers + Provenance + Zero-CDN Print-Ready Edition)

## Hard Step-Budget, Mode Routing & Anti-Timeout Protocol (CRITICAL — ZERO ERROR 500 / TURN_STEPS_EXCEEDED)

Whenever the user enters a stock ticker or company name (e.g., `AAPL`, `NVDA`, `PTT`, `0700.HK`, `ADVANC`, `TSM`), deliver a complete institutional-grade analysis with a decisive verdict: **PASS / CONDITIONAL PASS / GREY ZONE / FAIL**.

- **`FULL` Mode (Default):** Render a **self-contained Editorial HTML Dashboard (`index.html`)** containing **all Phases 1–9** plus the **Phase 9 Final Distilled Synthesis** in chat.
- **`QUICK` Mode (Only when user explicitly asks for "quick", "triage", or "สรุปสั้น"):** Run 1 parallel search wave and deliver a concise chat-only triage (5-Line Plain-Language Opener, Provenance & Core KPI Table, 3-Step DuPont summary, Peer/Supplier snapshot, 10-Dimension Rubric score, and 3 Non-Negotiable Triggers).

To preserve **100% of original data depth and visual richness** while strictly preventing `500 INTERNAL (TURN_STEPS_EXCEEDED)`, enforce these 4 execution locks:

1. **3-PATH DATA INGESTION & MAX 2 PARALLEL SEARCH WAVES (Hard Stop After Wave 2):**
   - **US Tickers SEC EDGAR XBRL Pre-Flight (`scripts/fetch_sec_edgar.py`):** Whenever analyzing a US SEC-reporting ticker (e.g., `NVDA`, `AAPL`, `AVGO`, `AMD`), first run `python scripts/fetch_sec_edgar.py <TICKER> --out <ticker>_sec_xbrl.json` to pull 10 years of audited `10-K` and `10-Q` US GAAP facts directly from `data.sec.gov/api/xbrl/companyfacts/` (capturing exact `D&A`, `SBC`, `Tax`, `Interest Expense`, `Operating Leases`, `CapEx`, and YTD-differenced quarterly cash flows as primary `[FILING]` truth with zero `N/A` gaps on SEC-disclosed sub-lines).
   - **Path A — Live 2-Wave Search (Default when no financial files are uploaded):**
     - **Wave 1 (Target 10Y Deep-Dive):** Gather primary filings (`10-K`/`10-Q`/`20-F`/`56-1`/HKEX/Investor Day) for the Target's 10Y & LTM Income Statement (incl. `OpEx` split: `SG&A`, `R&D`, `G&A OHC`, `D&A`, `Interest Expense`, and disclosed `FC/VC` cost structure), Balance Sheet (Cash + ST/LT Marketable Securities, Interest-Bearing Debt incl. Leases, NCI, AR/Inv/AP for `OC`, `CCC` & AR/Inv aging divergence), Cash Flow (`CFO`, `CapEx`, `SBC`), `WACC`, `R&D Cap%`, Workforce (`Headcount / FTE`, `Rev/Emp`, `EBIT/Emp`, `Labor/SBC % Rev`), Top-Line Commercial & Operational Drivers (`Price-Volume-Mix PVM`, `Gross-to-Net`, `Backlog / Book-to-Bill`, `NRR / Churn`, `LTV/CAC`, `Capacity Utilization %` where applicable), Debt Covenants (`Net Debt/EBITDA`, `Interest Coverage`), AI ROI disclosures, and Geographic Triad notes.
     - **Wave 2 (Direct Competitors, Suppliers & Gap-Fill ONLY):** Gather LTM & multi-year metrics (`Revenue`, `EBIT`, `FCF`, `CapEx`, `CapEx Intensity %`, `CapEx/D&A`, `GM%`, `SG&A/OpEx%`, `EBIT%`, `FCF%`, `ROIC`, `3-Step DuPont ROE`, `DOL`, `Interest Coverage`, `CCC/DIO/DSO/DPO`, `R&D Cap%`, `Headcount`, `Triad mix`, `FC27E consensus`, and `Multiples: P/E, Fwd P/E, EV/EBITDA, FCF Yield`) for the **3 Direct Competitors + 2 Key Value-Chain Suppliers + Real-World/Industry Benchmarks**, plus any missing Target metric from Wave 1.
     - **HARD STOP AFTER WAVE 2:** Never execute a 3rd search wave or URL-by-URL crawl loops. Immediately assign `"N/A"` to any figure still unverified after Wave 2.
   - **Path B — User-Uploaded Filings / CSV / Screener Export:** Parse uploaded `10-K`/`56-1`/CSV tables directly as primary `[FILING]` truth for the Target, then execute **at most 1 search wave** solely for Direct Competitors, Value-Chain Suppliers, and current market price.
   - **Path C — Unlisted / Offline Qualitative Mode:** If search is unavailable and no files are uploaded, never fabricate numbers—assign `"N/A"` to unverified quantitative cells and complete qualitative moat, value-chain, and sensitivity frameworks transparently.

2. **ZERO External CDN / ZERO `<canvas>` Libraries (1-Pass Pure HTML/CSS + Inline Vector Polylines):**
   - Do **NOT** load Chart.js or any external JS chart library (load Google Fonts only).
   - Render ALL charts (Graph 1 Scale, Graph 2 Margins & Intensity, Consulting Patterns A/B/C, Phase 3 5Y Forecast & Value-Chain Bars, Phase 6 24-bin Monte Carlo Histogram, Phase 8 Workforce & Triad Charts) using **Pure HTML/CSS Flexbox & Grid percentage bars** plus crisp inline `<svg><polyline>` trend/slope lines (**NEVER place multi-word `<text>` inside fixed-width SVG boxes**—keep all titles, legends, and labels in auto-wrapping HTML). This eliminates multi-step canvas repair loops and guarantees 1-pass generation.

3. **Single `const DATA = {...}` Store + Compact Vanilla JS Renderers (`<= 450` Lines Total):**
   - Store all verified metrics and inline epistemic tags in one compact `const DATA = {...}` JS object inside a single `<script>`.
   - Compute all FP&A formulas (`OPAT`, `OC`, `Unlevered FCFF`, `Owner FCF`, `FCF/EBITDA Conversion`, `CapEx/D&A`, `Incremental ROIC`, `OpEx%`, `Incremental Margin`, `Empirical DOL`, `Interest Coverage`, `DuPont ROE`, `CCC`), forecast math, 10-Dimension Rubric totals, and the live 10,000-run Monte Carlo (Fat-Tail Student-t + Box-Muller) directly in inline JS, generating repeating table rows, Consulting Patterns A & C, DuPont switcher views, and the 24-bin histogram via concise `.map()` templates.

4. **Crisp A4 Print-to-PDF Support:**
   - Include `@media print { @page { size: A4 landscape; margin: 10mm; } * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; } .no-print { display: none !important; } section, .card, .ed-diagram-board { break-inside: avoid; } }` and wire the top `Export PDF` / `พิมพ์ / Save PDF` buttons to `window.print()`.

---

## 0. Mandatory UI, Editorial Craft, Zero-Overflow, Epistemic Provenance & `"N/A"` Honesty Rules

1. **Layout & Navigation (Zero Sticky Headers / Zero Shadows):**
   - Stamp first line of `<style>`: `/* HALLMARK STAMP | Material: Archival Financial Broadsheet | Dials: V4-M2-D8 | Accent: #d94e34 | Gates: 8-Width Zero-Overflow + Epistemic-Tags + Strict-NA + Print-Safe */`
   - **NEVER** use `position: sticky` or `fixed`. Start `<main class="container" id="report-root">` with a static `.static-toc` bar (`P1`–`P9` jump links + primary solid `Export PDF` button `#0f172a` + secondary ghost `พิมพ์ / Save PDF` button).
   - Palette: `--paper:#f8fafc; --surface:#ffffff; --soft:#f1f5f9; --ink:#0f172a; --ink-secondary:#334155; --muted:#64748b; --hairline:#cbd5e1; --border:#e2e8f0; --accent:#d94e34` (max 1–2 focal elements per section), `--emerald:#047857; --amber:#b45309; --rose:#be123c`. Zero `box-shadow`, `text-shadow`, gradients, glassmorphism, or nested card-in-card borders. Radius scale: `2px` inputs, `4px` cards/tables/buttons, `9999px` semantic pills only.

2. **Zero Text Overflow Guarantee (`diagram-design` Standard):**
   - Global CSS: `p,li,td,th,h1,h2,h3,span,div{overflow-wrap:break-word;word-break:break-word} *{min-width:0;box-sizing:border-box}`
   - `.kpi-val{font-size:clamp(16px,1.8vw,19.5px)}` and `.table-scroll{width:100%;overflow-x:auto;border:1px solid var(--border)}`.
   - Build structural diagrams (**3-Step DuPont ROE Tree**, **Value-Chain & Peers Map**, **DCF Valuation Bridge**) strictly as **auto-wrapping HTML/CSS Grid & Flexbox cards** connected by slim CSS borders or inline `<svg>` arrows—never place multi-word descriptions inside fixed-width SVG `<text>` elements. Keep card text concise.

3. **Typography, Same-Hue Contrast & Global `"N/A"` Floor:**
   - Google Fonts (`display=swap`): `'Plus Jakarta Sans'` + `'Noto Sans Thai'` (headings/prose, `max-width:72ch`) and `'JetBrains Mono'` (`tabular-nums lining-nums` on all `td, th, .kpi-val, .badge-mono, output`, using true minus `−`).
   - Same-hue badges (`>=4.5:1` contrast): PASS (`#047857`/`#ecfdf5`/`#a7f3d0`), CONDITIONAL (`#b45309`/`#fffbeb`/`#fde68a`), FAIL (`#be123c`/`#fff1f2`/`#fecdd3`), GREY/NA (`#334155`/`#f1f5f9`/`#cbd5e1`).
   - **Global `"N/A"` Rule:** Across Phases 1–9, never invent or interpolate undisclosed figures (including internal `FC/VC` splits, factory `OHC` absorption, `PVM`, `Book-to-Bill`, `NRR`, `LTV/CAC`, or `Utilization %` if omitted from filings). Render `<span class="badge-mono na-tag">N/A</span>` in HTML and mark missing bars cleanly as `N/A` in CSS visual charts.

4. **Mandatory Inline Epistemic Provenance Tags:**
   - Tag key KPI cards, benchmark cells, forecast inputs, and simulation outputs with compact monospace badges so historical facts are never mixed with assumptions:
     - `[FILING]` — Audited/reported primary filing (`10-K`/`10-Q`/`20-F`/`56-1`/HKEX/earnings release).
     - `[CONSENSUS]` — Published street consensus (`FC27E`).
     - `[PROXY]` — Industry/peer median or statutory benchmark.
     - `[ASSUMP]` — Explicit analyst model input (`WACC`, `Terminal g`, `5Y CAGR`, `Sigma`).
     - `[SIM]` — Derived output from the 10,000-run Monte Carlo or explicit DCF engine.

5. **2-Layer Communication Rule (Plain-Language Top + Institutional FP&A Below):**
   - **Layer 1 (Buffett Plain-Language Callout):** Begin major phases with a 1–2 sentence everyday-language takeaway (no unexplained acronyms) stating what the numbers practically mean for a business owner.
   - **Layer 2 (Institutional FP&A Layer):** Deliver 100% of Jack Alexander FP&A ratios, accounting checks, and valuation schedules directly underneath.

---

## Phase 1: Provenance Strip, 5-Line Opener, Executive Verdict & Cross-Validation Gate (`#phase-1`)

1. **Top Data Provenance Strip (`.provenance-strip`):** Compact 6-cell header bar displaying: `Primary Source Filings`, `Latest Fiscal Period End`, `Currency & FX`, `Accounting Standard (GAAP/IFRS/TFRS)`, `Data Path (A/B/C) & Info Richness Grade (A/B/C)`, and `Explicit N/A Fields`.

2. **Verdict Masthead (`.verdict-banner`):** Ticker, exchange, currency, period, hue-matched Verdict badge (`PASS / CONDITIONAL PASS / GREY ZONE / FAIL` mapped from the 10-Dimension Rubric Score `XX/100`), target entry zone, and two summary layers:
   - **Layer 1 — 5-Line Plain-Language Opener (Zero Jargon):** (1) What this company actually sells & why customers stay, (2) True cash kept per `$100` of sales, (3) Real-money downside pain on a `$10,000` (or `฿1,000,000` for Thai stocks) position under tail stress (`CVaR 95%`), (4) Biggest hidden operational or value-chain bottleneck, (5) Clear action today.
   - **Layer 2 — Answer-First Institutional Executive Paragraph:** Synthesizing `10-Dimension Rubric Score`, 4-Masters Score, Duan Yongping Veto, `OPAT`, `Unlevered FCFF`, `ROIC vs. WACC` (and `Incremental ROIC`), `Cost/Operating Leverage (OpEx%, DOL, CapEx/D&A)`, `3-Step DuPont ROE`, `CCC` & `Operating Capital`, `Top-Line Commercial Drivers`, Peer/Supplier position, AI/Triad growth, `Table 22.1 DCF Fair Value (P50)` vs. Market Price, `MC Prob > Market Price`, and `CVaR 95%`.

3. **Cross-Validation Table (2+ Sources) & 6 Core KPI Cards:**
   - 5-row verification table: (1) Price & Diluted Shares (`Mkt Cap`), (2) Cash + ST/LT Marketable Securities, (3) Interest-Bearing Debt incl. Leases (excl. AP/Accruals) + `Interest Coverage (EBIT/Int)`, (4) Minority Interest (`NCI`), (5) Information Richness Grade (`A/B/C`) & Enterprise Value (`EV`) check.
   - 6-card `.kpi-grid` (with `[FILING]`/`[SIM]` tags): `Revenue (+YoY & 10Y CAGR)`, `OPAT (with Tax Rate t)`, `Unlevered FCFF (Margin % & FCF/EBITDA %)`, `ROIC vs. WACC (Spread & Incr. ROIC)`, `DuPont ROE (Avg & Ending)`, `DCF P50 Fair Value (MC Prob > Price & CVaR 95%)`.

---

## Phase 2: 10-Year Schedule, Jack Alexander FP&A, Full Cost-Leverage/Commercial Drivers & Direct Competitor Charts (`#phase-2`)

1. **10-Year Financial Table (`FY17`–`FY26` + `LTM` in `.table-scroll`):**
   - Rows: `Revenue`, `Gross Profit`, `GM%`, `SG&A / OpEx (% Rev, incl. G&A OHC where disclosed)`, `R&D (note R&D% & Cap% or N/A)`, `EBIT`, `EBIT%`, `Empirical DOL (%ΔEBIT ÷ %ΔSales)`, `Effective Tax Rate t`, **`OPAT = EBIT × (1 − t)`**, `Net Income`, `CFO`, `CapEx`, `CapEx Intensity (CapEx/Rev %)`, `CapEx / D&A (x)`, **`Std FCF = CFO − CapEx`**, `FCF / EBITDA Conversion %`, **`Unlevered FCFF = Std FCF + Int × (1 − t)`**, **`Owner FCF = Std FCF − NCI FCF − SBC`**, `Interest Coverage (EBIT ÷ Int)`, `Total Assets / Book Equity`, **`CCC (DIO + DSO − DPO)`**.

2. **4 FP&A, Cost-Leverage, Commercial & Workforce KPI Cards (`.grid-4`):**
   - **Card 1 (Working Capital & Liquidity Quality):** `Operating Capital (OC) = (AR + Inv + Op CA) − (AP + Accrued Op Liab)` (excl. Cash & Debt), `CCC (DIO/DSO/DPO)`, and `AR & Inventory Growth vs. Sales Growth` (aging/write-down risk check).
   - **Card 2 (Cash Conversion & CapEx Return Efficiency):** `FCFE = Std FCF + Net Borrowings`, `Owner FCF`, `FCF / EBITDA Conversion %`, `CapEx / D&A Ratio` (distinguishing Growth CapEx `>1.0x` vs. Maintenance CapEx), and `Incremental ROIC (ΔOPAT ÷ ΔInvested Capital)`.
   - **Card 3 (Full Cost Structure — OpEx, OHC, VC/FC, DOL — & Top-Line Commercial Drivers):**
     - *Cost & Leverage:* `OpEx % Sales` (`SG&A%` + `R&D%`), `Incremental Operating Margin (ΔEBIT ÷ ΔSales)`, `Empirical DOL` & `Incremental Contribution Margin Proxy (ΔGP ÷ ΔSales)` (plus explicit `VC`, `FC`, `Break-Even`, `Margin of Safety`, `Factory/G&A OHC Under-Absorption`, `LTV/CAC`, or `R&D Vitality` if disclosed, else `"N/A"`).
     - *Commercial & Capacity Drivers:* `Price-Volume-Mix (PVM)`, `Gross-to-Net Leakage`, `Order Backlog & Book-to-Bill Ratio`, `NRR / Churn`, `Capacity Utilization %`, and 3 Sector-Specific North Star KPIs (`"N/A"` if undisclosed).
   - **Card 4 (Concise Workforce Productivity — HC):** `Headcount / FTE`, `Rev/Employee`, `EBIT/Employee`, `Labor or SBC % of Revenue` (if disclosed), `Rev/Emp vs. OpEx/Emp jaws`, and brief note on how headcount/restructuring shifts impact `OpEx`, `Margin`, & `DuPont ROE`.

3. **Graph 1 & Graph 2 (Unified Interactive Pure CSS Bar & Vector Line Panels):**
   - **Graph 1 (Scale Panel):** Defaults to **Direct Competitors** comparing `Revenue ($B)`, `EBIT ($B)`, `Free Cash Flow ($B)`, and `CapEx ($B)` vs. top 3 Direct Competitors (not just suppliers), with `.seg-control` toggles for `Competitors + Suppliers` and `10Y Historical Series`.
   - **Graph 2 (Margins & Efficiency Panel):** Defaults to **Direct Competitors** comparing `Gross Margin %`, `EBIT Margin %`, `FCF Margin %`, `CapEx Intensity (CapEx/Rev %)`, `ROIC %`, and `DuPont ROE %` vs. Direct Competitors & Sector Median, with toggles for `Competitors + Suppliers (incl. R&D/Rev % & SG&A/Rev %)` and `10Y Margin & CapEx % Trend`.

---

## Phase 2.2: 3-Step DuPont ROE Tree, Value-Chain Map & Consulting Suite (`#phase-2-2`)

### A. Interactive 3-Step DuPont ROE Return Tree (`.ed-diagram-board`)
- 3-level auto-wrapping HTML/CSS grid + slim connector arrows:
  - **Level 1 (`--accent` focal):** `DuPont ROE` + `Unlevered ROA (Margin × Turnover)`.
  - **Level 2 (`×` badges):** `Net Margin (NI ÷ Sales)` × `Asset Turnover (Sales ÷ Assets)` × `Equity Multiplier (Assets ÷ Equity)`.
  - **Level 3 (6 Driver Cards):** `Net Income`, `Sales`, `Operating Sales (with Rev/Emp)`, `Total Assets (CapEx % Rev)`, `Balance Sheet Assets`, `Book Equity (D/E or Net Cash)`.
- Include 8-entity `.seg-control` switcher (`Target LTM / Ending / Prior` + `3 Direct Competitors` + `2 Key Suppliers`) + 3 live What-If sliders (`Net Margin %`, `Turnover x`, `Multiplier x`).

### B. Value-Chain Suppliers & Direct Competitors Architecture Map
- Auto-wrapping 2-tier CSS grid: **Tier A** (`Upstream Chokepoint Suppliers` → `Target Stock Focal Node` → `Downstream Customers` with `GM%`, `EBIT%`, `ROE%`, `DIO/DSO/DPO`) + **Tier B** (3 Direct Competitors across Margins, DuPont ROE, Turnover, CapEx/FCF Yield, Valuation Multiples).

### C. Peer & Supplier Benchmarking Matrix Table (Real-World & Industry Standards)
- Compare **Target**, **3 Direct Competitors**, **2 Key Suppliers**, and **Industry/Real-World Benchmark `[PROXY]`** across 6 rows:
  1. `GM%, SG&A/OpEx%, EBIT% & Empirical DOL`
  2. `ROIC vs. WACC & Incremental ROIC`
  3. `3-Step DuPont ROE & Debt Covenant Headroom (Net Debt/EBITDA, Interest Coverage)`
  4. `Working Capital CCC / DSO / DIO / DPO & FCF/EBITDA Conversion %`
  5. `R&D Capitalization Ratio, CapEx Intensity % & CapEx/D&A (x)`
  6. `Workforce KPIs (Headcount, Rev/Emp, EBIT/Emp) & Multiples (P/E, Fwd P/E, EV/EBITDA, FCF Yield)`
- **Mandatory Operational Impact Column:** Explicitly badge each metric **HIGH / LOW** vs. peers/industry standards and state its practical impact on day-to-day business operations, cost absorption (`OHC/FC`), cash conversion, and strategic flexibility.

### D. Consulting Visual Suite (ANNUAL DATA ONLY — Pure CSS Bars + Vector Slope)
1. **Pattern A — 6-Company Annual Step-Bridge & Hatched Forecast Grid (`2022–2026 + FC27E [CONSENSUS]`):** 6-panel CSS grid (Target + 3 Competitors + 2 Suppliers) with 5 solid `#002b49` CSS bars + 1 CSS `repeating-linear-gradient` hatched `FC27E` bar (`N/A` if undisclosed), YoY step-bridge delta badges, overarching CAGR oval pill, and toggle (`Annual Revenue / EBIT / CapEx $B`).
2. **Pattern B — Indexed Growth (`2021 = 100`) + Dark-Navy Summary Table:** Left inline vector polyline panel (`Indexed Sales / Indexed CapEx / EBIT Margin %` with HTML legend); Right `#002b49`-header table (`Company`, `Sales FY26/LTM`, `Annual YoY%`, `CAGR 21–26`, `CapEx % Sales`).
3. **Pattern C — Multi-Row YoY Revenue & Embedded EBIT [%] Slope vs. 9Y Annual Trajectory:** 4 rows (Target + 3 Direct Competitors) × 3 cols: Brand block | 2-bar Prior vs. Current FY Revenue with embedded diagonal `EBIT %` vector slope & HTML pills | 8–9 CSS bar annual trajectory (`FY19–FY26/FC27E`) with growth pill.

---

## Phase 3: Time-Series ML & Forensic Diagnostics (`#phase-3`)
- **4 KPI Cards:** `10Y CAGR & R²` regime, `Altman Z (>2.99), Beneish M (<-1.78) & Covenant Headroom (Net Debt/EBITDA & Interest Coverage)` (or `N/A` for financials), `Sloan Accrual Ratio ((NI−CFO)/Assets) & CapEx-to-OpEx Capitalization Check`, `Working Capital, OHC Under-Absorption & Gross-to-Net Divergence Flag` (AR/Inv aging vs. Sales, Utilization drop vs. GM%).
- **2 Visual Panels (`.grid-2`):** Left: `Historical + 5Y Damped Holt-Winters / AR(1) Sales & Unlevered FCFF Forecast [ASSUMP]` (solid historical + hatched forecast CSS bars); Right: `Cross-Value-Chain GM%, EBIT% & DuPont ROE% Grouped CSS Bar Panel`.

---

## Phase 4 & Phase 5: Force Alignment, 4-Masters Debate & 10-Dimension Objective Rubric (`#phase-4`, `#phase-5`)
- **Phase 4 (Force Alignment):** 6-row External (`Macro/FX/Tariffs`, `Supply/Demand Cycle`, `Regulation/Geopolitics`) & Internal (`Pricing/Moat & PVM`, `Capital Allocation & CapEx/OpEx ROI`, `Balance Sheet/WC & Covenants`) table scored `-2.0` to `+2.0` with monospace gauges (`▓▓▓▓▓▓░░`).
- **Phase 5A (4-Masters Adversarial Debate):** 4-column editorial debate (`1.0–5.0` weighted score): **Duan Yongping** (30% — `<2.5` auto-VETO), **Warren Buffett** (30%), **Charlie Munger** (20% — Top 3 Fatal Scenarios with `%` prob), **Li Lu** (20%).
- **Phase 5B (10-Dimension Quantitative Rubric — Feeling-Based Scoring Banned):**
  - Score 10 dimensions (`0–10` pts each = `100` pts total) with explicit numeric cutoffs (`0–2 Weak`, `3–5 Sub-Peer`, `6–8 Institutional`, `9–10 Elite`):
    1. `ROIC − WACC Spread` (`<0%`: 0–2 | `0–4%`: 3–5 | `4–10%`: 6–8 | `>10%`: 9–10)
    2. `Owner FCF / OPAT Conversion %` (`<50%`: 0–2 | `50–75%`: 3–5 | `75–95%`: 6–8 | `>95%`: 9–10)
    3. `Balance Sheet Resilience (Net Debt/EBITDA & Interest Coverage)` (`>3.5x` or `Int Cov <2x`: 0–2 | `2.0–3.5x`: 3–5 | `0–2.0x` & `Int Cov >4x`: 6–8 | `Net Cash`: 9–10)
    4. `Working Capital CCC vs. Industry` (Deteriorating/Bottom quartile: 0–2 | Inline: 5–7 | Negative/Advantaged CCC: 9–10)
    5. `10Y Gross & EBIT Margin Durability (incl. OpEx/OHC & DOL Discipline)` (Secular erosion: 0–2 | Cyclical/High fixed-cost drag: 3–5 | Stable/Expanding: 6–8 | Pricing-power fortress: 9–10)
    6. `Direct Competitor Scale & Margin Rank` (Laggard: 0–2 | Mid-tier: 3–5 | Top-2 contender: 6–8 | #1 leader: 9–10)
    7. `Value-Chain Chokepoint & Supplier Leverage` (Squeezed: 0–2 | Neutral: 3–5 | Strong pass-through: 6–8 | Bottleneck tollbooth: 9–10)
    8. `Forensic Accounting Quality` (Beneish/Sloan warning: 0–2 | Watchlist: 3–5 | Clean filings: 6–8 | Conservative cash-generative: 9–10)
    9. `AI Monetization & Workforce Productivity (Rev & EBIT/Emp)` (AI-washing/bloated: 0–2 | Unproven: 3–5 | Margin lift: 6–8 | Proven revenue + EBIT/Emp expansion: 9–10)
    10. `Valuation Margin of Safety (MC Prob > Price & CVaR 95%)` (`Prob <35%`: 0–2 | `35–55%`: 3–5 | `55–75%`: 6–8 | `>75%`: 9–10)
  - **Deterministic Verdict Rule:** `>=78` (and Duan `>=2.5`) = **PASS** | `62–77` = **CONDITIONAL PASS** | `45–61` = **GREY ZONE** | `<45` or Duan `<2.5` = **FAIL**.

---

## Phase 6: Jack Alexander DCF (Table 22.1 & 22.2) & Fat-Tail 10,000-Run Monte Carlo (`#phase-6`)

1. **Table 22.1 (5Y Explicit DCF `[ASSUMP]`):** `Base + Y1–Y5` (`Sales → EBIT → Taxes → OPAT → +D&A −CapEx −ΔOC = FCFF → PV @ WACC`).
2. **EV-to-Equity Bridge (`.ed-bridge-flow`):** Auto-wrapping 6-card flow: `[PV 5Y FCFF] + [PV Terminal Value] = [Implied EV] + [Cash & MS] − [Interest-Bearing Debt & NCI] = [Implied Equity & Per-Share Value]`.
3. **Table 22.2 (5×5 Sensitivity Matrix + Explicit Assumption Delta):** `WACC (±50/100 bps)` vs. `Terminal g`, highlighting Base `P50` (`2px solid var(--accent)`), plus explicit callout badges showing `Δ Fair Value per +100 bps WACC` and `per −100 bps Terminal g`.
4. **10,000-Run Fat-Tail Monte Carlo Engine (`[SIM]`):**
   - `.seg-control` Distribution Toggle: **Fat-Tail Student-t (`df=5`) + 10% Bear Jump (Default)** vs. **Gaussian Box-Muller**.
   - 5 live sliders (`Base FCFF`, `Mean CAGR`, `Sigma σ`, `WACC %`, `Terminal g %`) + ghost reset & solid re-run buttons.
   - 9 stat boxes: `CVaR 95% (Expected Shortfall)`, `P5`, `P10`, `P25`, `P50`, `P75`, `P90`, `P95`, `Prob > Mkt Price %` + **24-bin Pure CSS Flexbox Histogram**.
5. **Actionable Cards (`.grid-2`):** Left: `3-Tier Price Action Zones (P10–P25 / P30–P50 / >P75)` + **Real-Money Downside Translation** (`$10,000` / `฿1,000,000` position value at `P10` & `CVaR 95%`); Right: `5-Sentence Mirror Test`.

---

## Phase 7: Mandatory 10-Point Pre-Response Self-Audit (`#phase-7`)
Emerald-ruled (`2px solid var(--emerald)`) concise 10-row verification table (`PASSED ✓`): (1) `OPAT = EBIT×(1−t)` check, (2) `OC` excludes Cash/Debt, (3) Realistic `CapEx >= D&A` & `CapEx/D&A` growth vs. maintenance check, (4) Strict EV-to-Equity (`+Cash −Debt −NCI`) & `Interest Coverage` check, (5) Market Price vs. `P50` divergence reason, (6) NCI/Geopolitical discount check, (7) Epistemic tags (`[FILING]`/`[ASSUMP]`/`[SIM]`) verified, (8) 10-Dimension Rubric sum matches Verdict badge, (9) Zero sticky/shadow/overflow & `tabular-nums` check, (10) Global `"N/A"` zero-fabrication check (incl. undisclosed `FC/VC`, `OHC`, `PVM`, `Book-to-Bill`, `NRR`, or `Utilization %`).

---

## Phase 8: AI Monetization Audit, Workforce Productivity & Global Geographic Triad (`#phase-8`)
Render a concise 3-card operational & geographic board (`.grid-3` + Pure CSS horizontal percentage bars):
1. **AI Monetization Proof vs. "AI Washing":** Classify the company as **Direct AI Monetizer / Cost-Efficiency Capturer / Unproven CapEx Cycle / AI Washing**, citing disclosed AI revenue, margin lift, CapEx intensity shift, or `"N/A"`.
2. **Workforce & Restructuring Leverage:** Concise comparison of `Headcount`, `Revenue/Employee`, and `EBIT/Employee` vs. Direct Competitors, explicitly showing how headcount discipline or restructuring flows into `OpEx%`, `EBIT%`, and `3-Step DuPont ROE`.
3. **Global Geographic Triad (`Americas / EMEA / APAC`):** Stacked Pure CSS revenue/profit mix bar, fastest-growing regional engine, and FX/tariff/geopolitical concentration exposure.

---

## Phase 9: Ultimate All-Phases Synthesis & Final Distilled Conclusion (`#phase-9` & Chat Summary — MANDATORY)
Whenever an analysis is completed (both inside `#phase-9` of the HTML dashboard and in the chat response), synthesize Phases 1–8 into a single, decisive **Final Distilled Conclusion (บทสรุปกลั่นกรองข้อสุดท้าย)**:

1. **Part-by-Part Analytical Synthesis Table (ตารางสังเคราะห์ครบทุกพาร์ท):**
   - **Part 1 (Executive, Provenance & Cross-Validation):** Data path/integrity grade, balance sheet net cash/debt & covenant reality `[FILING]`, and core scale.
   - **Part 2 (10Y FP&A, Cost-Leverage, Commercial Drivers & Peer Scale/Margins):** `OPAT`, `Std FCF / Unlevered FCFF`, `Owner FCF`, `FCF/EBITDA %`, `CapEx Intensity %` & `CapEx/D&A`, `OpEx/OHC %`, `Empirical DOL` & `Incremental Margin`, `Top-Line Drivers (PVM / Book-to-Bill / NRR / Utilization)`, `ROIC vs. WACC` spread (and `Incr. ROIC`), `Operating Capital (OC)`, and `CCC` vs. direct competitors.
   - **Part 2.2 (3-Step DuPont ROE & Value-Chain Benchmarking):** Decomposition of `Net Margin × Asset Turnover × Equity Multiplier`, supplier chokepoint power, and `HIGH / LOW` operational impact vs. industry standards.
   - **Part 3 (Time-Series ML & Forensic Accounting):** 10Y growth regime (`CAGR` & `R²`), `Altman Z`, `Beneish M`, `Sloan Accruals`, `Interest Coverage`, and working capital / OHC under-absorption divergence flags.
   - **Part 4 & Part 5 (Force Alignment, 4-Masters & 10-Dimension Rubric):** Net macro/internal force score (`-2.0` to `+2.0`), weighted 4-Masters score (`1.0–5.0`), Duan Yongping Veto status, Charlie Munger's top fatal risks, and `XX/100` Objective Rubric score.
   - **Part 6 (Explicit 5Y DCF & Fat-Tail Monte Carlo):** `Table 22.1 Base P50 Fair Value`, `P10–P25 / P30–P50 / >P75` distribution, `CVaR 95%` downside, `Prob > Market Price %`, and `±100 bps` WACC/g sensitivity.
   - **Part 7 & Part 8 (10-Point Audit, AI Monetization, Workforce & Global Triad):** Audit pass status, real AI cash proof vs. "AI washing", `Headcount` & `Rev/EBIT per Employee` leverage, and `Americas / EMEA / APAC Triad` shift.

2. **The Final Distilled Verdict Box (ข้อสรุปกลั่นกรองข้อสุดท้าย):**
   - **3 Investor Persona Fit Lines:** Concise action line for (a) *Quality Compounder*, (b) *Deep Value / Margin-of-Safety*, and (c) *Dividend / Cash-Yield* investors.
   - **1-Sentence Core Thesis + Mandatory Trade-Off Sentence (แก่นคำตัดสินเดียว):** State clearly whether the stock is a **BUY / HOLD (WAIT FOR PULLBACK) / AVOID**, followed by: *"Buying [TICKER] at [PRICE] means trading [X valuation/multiple risk] in exchange for [Y moat/cash-flow engine], and the key risk you must accept is [Z]."*
   - **The 3 Non-Negotiable Triggers (3 เงื่อนไขชี้ขาดในการลงมือทำ):**
     1. *Entry Price Trigger:* Exact price zone aligned with DCF `P50` and Fat-Tail Monte Carlo `P25–P50`.
     2. *Fundamental Bull Trigger:* Key operational, top-line (`PVM/Backlog/NRR`), cost-leverage (`DOL/OpEx`), or AI KPI that justifies a higher multiple.
     3. *Thesis-Breaker / Exit Trigger:* Exact forensic, debt-covenant, or value-chain threshold where the investment thesis fails.
