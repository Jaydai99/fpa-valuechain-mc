# FPA Value Chain MC — 10Y FP&A, Value-Chain, Fat-Tail Monte Carlo & AI/Triad Stock Analyzer (v3.1)

An institutional-grade Antigravity agent skill implementing a 9-Phase equity analysis framework for any stock ticker, combined with direct SEC EDGAR XBRL data extraction and a self-contained, zero-CDN print-ready HTML/CSS dashboard engine.

## Repository Structure

```text
fpa-valuechain-mc/
├── SKILL.md                 # 9-Phase equity analysis skill specification
├── README.md                # Guide, workflow docs & live capture gallery
├── docs/
│   ├── build_presentation.py # Builds HTML, PDF & 16 slide PNGs
│   ├── slides.html           # 16-slide English deck source
│   ├── slides/               # 16 rendered slide PNGs (slide_01..16.png)
│   └── fpa-valuechain-mc-presentation.pdf
├── scripts/
│   └── fetch_sec_edgar.py    # SEC EDGAR XBRL JSON API (10-K & 10-Q)
└── examples/
    └── nvda/
        ├── index.html        # Verified NVDA Q3 FY27 dashboard (Nov 17 8-K)
        ├── nvda_sec_xbrl.json
        └── shot_01..14.png   # 14 surgical section captures (P1–P9)
```

## Methodology & Full Function Presentation (Captured from Styled HTML Slides)

- **Self-Contained Deck:** [docs/fpa-valuechain-mc-presentation.pdf](docs/fpa-valuechain-mc-presentation.pdf) ([HTML source](docs/slides.html) · [Builder](docs/build_presentation.py)) — explains **Present Value (PV)**, **Unlevered FCFF DCF**, **10,000-run Fat-Tail Student-t Monte Carlo & CVaR 95%**, **CVP / DOL / DuPont ROE**, **10-Dimension Objective Rubric**, and every functional module (`Phase 1` to `Phase 9`) using 14 live `NVDA` Q3 FY27 captures.

### Part 1 — Cover, Core Valuation Principles & Execution Architecture (Slides 1–4)

![Slide 1 — Cover](docs/slides/slide_01.png)

![Slide 2 — Present Value & Discounted Cash Flow Core](docs/slides/slide_02.png)

![Slide 3 — 10,000-Run Fat-Tail Monte Carlo & CVaR 95%](docs/slides/slide_03.png)

![Slide 4 — FP&A Cost Leverage, DuPont ROE, Epistemic Rigor & Pipeline](docs/slides/slide_04.png)

### Part 2 — Complete Function-by-Function Walkthrough (Slides 5–16 with Live `NVDA` Captures)

| Module / Phase | Captured Slide |
| --- | --- |
| **Slide 5 — Phase 1A: Nav Bar, Provenance Strip & Dual-Layer Verdict**<br>![Slide 5](docs/slides/slide_05.png) | **Slide 6 — Phase 1B: Live Earnings Beat & Accounting Identity Gate**<br>![Slide 6](docs/slides/slide_06.png) |
| **Slide 7 — Phase 2A: 10-Year SEC XBRL Ledger & Commercial Drivers**<br>![Slide 7](docs/slides/slide_07.png) | **Slide 8 — Phase 2B: CVP Cost Structure (FC/VC/DOL) & Dual Charts**<br>![Slide 8](docs/slides/slide_08.png) |
| **Slide 9 — Phase 2.2A/B: Interactive DuPont ROE Tree & Value-Chain Map**<br>![Slide 9](docs/slides/slide_09.png) | **Slide 10 — Phase 2.2C: Industry & Supplier Benchmarking Matrix**<br>![Slide 10](docs/slides/slide_10.png) |
| **Slide 11 — Phase 2.2D: Consulting Visual Suite (Patterns A, B, C)**<br>![Slide 11](docs/slides/slide_11.png) | **Slide 12 — Phase 3 & 4: Time-Series ML, Forensics & Force Alignment**<br>![Slide 12](docs/slides/slide_12.png) |
| **Slide 13 — Phase 5: 4-Masters Committee & 10-Dim Objective Rubric**<br>![Slide 13](docs/slides/slide_13.png) | **Slide 14 — Phase 6A: Jack Alexander DCF & Live 10k Monte Carlo**<br>![Slide 14](docs/slides/slide_14.png) |
| **Slide 15 — Phase 6B & 7: Action Zones, Mirror Test & 10-Pt Self-Audit**<br>![Slide 15](docs/slides/slide_15.png) | **Slide 16 — Phase 8, 9 & Quick Start: AI/Triad & Distilled Verdict**<br>![Slide 16](docs/slides/slide_16.png) |

### Full-Resolution Section Captures (`examples/nvda/`)

![NVDA Phase 1 Verdict & Dual-Layer Opener](examples/nvda/shot_01_p1_verdict.png)

![NVDA Phase 2 CVP Cost Structure & Peer Charts](examples/nvda/shot_04_p2_cvp_charts.png)

![NVDA Phase 2.2 DuPont ROE & Value-Chain Map](examples/nvda/shot_05_p22_dupont_vc.png)

![NVDA Phase 6 DCF & 10k Fat-Tail Monte Carlo](examples/nvda/shot_11_p6_dcf_mc.png)

![NVDA Phase 9 Ultimate Synthesis & Verdict](examples/nvda/shot_14_p9_verdict.png)

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
