---
okf_version: "0.2"
id: "readme-root"
type: "concept"
title: "PmStudio — Quantitative Portfolio Studio"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["pmstudio", "overview", "quadrants", "personas", "architecture", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "AGENTS.md"
summary: "Overview of PmStudio: analytical copilot and macro scribe, 4 operational quadrants, and persona-driven directory architecture."
---

# PmStudio

> **Analytical copilot and macro scribe for a multi-asset quantitative investment portfolio.**

PmStudio is an advisory and staging operating environment for quantitative asset management. It enforces strict separation of concerns: **advisory and staging only; zero automated execution authority**. Snowflake is the fund's sole book of record, Git maintains the version-controlled codebase and research history, and all mathematical metrics derive purely in Python.

---

## The 4 Quadrants

The workspace architecture is governed by a **2×2 matrix** across two foundational dimensions:

1. **Origin of Truth (Endogenous vs. Exogenous):**
   - **Endogenous:** Internal to the fund (internal books, risk headroom, pure math, and execution staging).
   - **Exogenous:** External to the fund (clearing houses, regulatory mandates, dealer terms, and market tick data).

2. **Temporal Dynamic (Structural vs. Dynamic):**
   - **Structural:** Invariant rules, mathematical theorems, clearing mechanics, and hardened numerical solvers.
   - **Dynamic:** Fast-moving events, empirical falsification spikes, daily desk setups, and trade ticket staging.

```
                        STRUCTURAL (Invariants & Rules)
                                      ▲
                                      │
                 COMMONS              │             ENGINES
         [The Desk Strategist]        │     [The Software Engineer]
         Exogenous × Structural       │     Endogenous × Structural
         • Market plumbing & rules    │     • Deterministic math & risk
         • Haircut matrices           │     • Pure zero-I/O solvers
         • Analytical proofs          │     • Data ingress contracts
                                      │
  EXOGENOUS ──────────────────────────┼──────────────────────────► ENDOGENOUS
  (External Market)                   │                            (Internal Desk)
                                      │
                   LAB                │             JOURNAL
        [The Quant Researcher]        │     [The Portfolio Manager]
         Exogenous × Dynamic          │       Endogenous × Dynamic
         • Empirical research spikes  │     • Fiduciary headroom audit
         • RV anomaly falsification   │     • Ticket staging (Pydantic)
         • Disposable crash-testing   │     • Daily desk operations log
                                      │
                                      ▼
                         DYNAMIC (Events & Operations)
```

---

## Personas and Repository Structure

Each quadrant maps directly to an operational directory, governed by a specialized persona and charter:

| Quadrant | Directory | Persona | Orientation | Core Mission & Invariants |
| :--- | :--- | :--- | :--- | :--- |
| **I** | [`commons/`](file:///C:/Users/Eric/PmStudio/commons/README.md) | **The Desk Strategist** | *Exogenous × Structural* | Ingests institutional plumbing, clearing mechanics, exchange rulebooks, and dealer haircut matrices. Scribes analytical proofs into dense, structured notes without speculative forecasts or narrative rhetoric. |
| **II** | [`engines/`](file:///C:/Users/Eric/PmStudio/engines/README.md) | **The Software Engineer** | *Endogenous × Structural* | The computational substrate and single source of financial truth. Builds pure, zero-I/O mathematical solvers (`quant/`, `risk/`), strict data ingress contracts (`pandera`), and BI export snapshots. Strict static typing (`mypy`). |
| **III** | [`lab/`](file:///C:/Users/Eric/PmStudio/lab/README.md) | **The Quant Researcher** | *Exogenous × Dynamic* | Formulates, tests, and aggressively falsifies quantitative anomalies and relative-value (RV) spikes in disposable research workspaces (`lab/wip_*`). Freezes inquiries to `done_*` or `dead_*`. Never imports into `engines/`. |
| **IV** | [`journal/`](file:///C:/Users/Eric/PmStudio/journal/README.md) | **The Portfolio Manager** | *Endogenous × Dynamic* | Governs the capital risk envelope, monitors fiduciary mandate headroom (`mandate.md`), stages trade execution tickets (Pydantic/Jinja2), and logs desk reality during morning setup and evening close. |

---

## Core Invariants

- **State vs. Code:** State lives exclusively in Snowflake; code and analytical artifacts live in Git. Local files must never persist portfolio state.
- **Zero-I/O Computational Substrate:** Mathematical and risk functions in [`engines/`](file:///C:/Users/Eric/PmStudio/engines/README.md) are strictly pure (zero network, zero disk, zero database I/O).
- **Promotion Gate:** Disposable exploratory code in [`lab/`](file:///C:/Users/Eric/PmStudio/lab/README.md) never touches production. Validated mathematical logic must be sanitized, strictly typed, and verified via `pytest-regressions` ($|\Delta| \le 10^{-8}$) before promotion into [`engines/`](file:///C:/Users/Eric/PmStudio/engines/README.md).
- **Display-Only Downstream Tools:** Presentation layers (Power BI, Excel) are display-only. No financial formulas or risk metrics are calculated in DAX or spreadsheets; all metrics derive deterministically in Python.
- **Strict OKF v0.2 Standard:** Every Markdown document adheres to the OKF v0.2 frontmatter schema (`.okf.schema.json`) with bidirectional relational graphing.

---

## Primary Workflows (PowerShell 5.1)

All routine desk actions are automated via typed PowerShell commands:

| Action | Command | Purpose |
| :--- | :--- | :--- |
| **Morning Desk Setup** | `.\tasks.ps1 morning` | Ingests Snowflake positions, evaluates mandate headroom, initializes daily log. |
| **Export BI Snapshot** | `.\tasks.ps1 export-bi` | Generates pre-calculated flat files for Power BI / Excel display. |
| **Targeted Code Check** | `.\tasks.ps1 check <path>` | Runs strict `ruff`, `mypy`, and targeted tests. |
| **Scaffold Research Spike** | `.\tasks.ps1 spike <name>` | Scaffolds a new disposable research workspace under `lab/wip_<name>/`. |
| **Initialize Hooks** | `.\tasks.ps1 setup-hooks` | Configures Git pre-commit hooks for secret scanning, linting, and OKF schema checks. |
