---
okf_version: "0.2"
id: "engines-workspace-context"
type: "procedure"
title: "Engines Workspace Context — The Software Engineer"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["engines", "engineer", "endogenous", "computational-substrate", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "AGENTS.md"
summary: "Engineering invariants, golden path libraries, promotion gates, and negative boundaries."
---

# Engines: The Software Engineer
Last updated: 2026-09-07

**Orientation:** Endogenous × Structural. Builds deterministic numerical math, live data connectors, risk solvers, and ops CLIs.

## Role Boundary ("NOT")
- **NOT an Enterprise Web / Security Architect:** Never spend cycles on authentication, OAuth, CORS, public API security, or penetration hardening. Tools run on **local loopback (`localhost:8501`) on a secured Windows 11 PC inside a protected corporate network**, or internally on Streamlit in Snowflake (SiS).
- **NOT a Snowflake DBA:** Never manage database clusters, tune SQL warehouse compute, or author complex stored procedures. Query Snowflake as an append-only data store using standard SQL.
- **NOT a Financial Theorist:** Never invent financial models; implement specifications into deterministic code.

## Golden Path Libraries

Use verified libraries instead of writing procedural custom code:

- **`xbbg` (Market Data Feeds):** Preferred programmatic Bloomberg connector for fetching reference, market, and intraday data into Polars/pandas. Prefer `xbbg` over low-level, procedural `blpapi` calls.
- **`OpenSourceRisk` / `open-source-risk-engine` (ORE):** Preferred industry-standard framework for financial instrument valuation, curve construction, sensitivity analytics, and collateral/margin risk modeling. Prefer high-level ORE interfaces over raw, unparameterized `QuantLib` bindings.
- **`pandera[polars]` (Ingress Contracts):** Enforce strict schemas on all raw data streaming through `connectors/` before passing to solvers or research.
- **`pydantic` (Data & Rule Modeling):** Model trade tickets, portfolio limits, and financing terms with declarative validators.
- **`typer` + `rich` (Operational CLIs):** Build typed PowerShell commands and styled output tables for `tasks.ps1`.
- **`jinja2` (Document Rendering):** Render Markdown tickets and logs from version-controlled templates instead of long f-strings.
- **`pytest-regressions` (Numerical Parity):** Use `num_regression` to verify promotion parity against benchmark proofs ($|\Delta| \le 10^{-8}$).
- **`hypothesis` (Property Fuzzing):** Fuzz numerical solvers against degenerate mathematical states (zero vol, inverted curves, negative yields).

## Engineering Invariants
- **Substrate Zero-I/O Purity:** Functions in `quant/` and `risk/` are pure transformations on in-memory Polars DataFrames or NumPy arrays. Zero disk, network, or database I/O.
- **Single Source of Truth for BI:** All financial math originates here. Expose pre-calculated snapshots via `export_bi.py` for Power BI and Excel.
- **Strict Typing:** All code must pass `uv run mypy engines/` in strict mode with zero errors.

## The Promotion Gate (Lab -> Engines)
1. Extract calculation logic from `lab/<inquiry>/run.py`.
2. Parameterize inputs; remove hardcoded identifiers, dates, and network calls.
3. Apply static types and verify with `uv run mypy engines/<module>.py`.
4. Author targeted parity tests via `pytest-regressions` proving $|\Delta| \le 10^{-8}$ against analytical proofs.
5. Re-point research scripts to `engines.<module>` and verify identical outputs.

## Child Workspaces (Packages)

| Package / Domain | Location | Read |
| :--- | :--- | :--- |
| *(Spawn packages dynamically)* | `engines/<package>/` | `CONTEXT.md` |

## What Good Looks Like
- 100% statically typed, zero-I/O mathematical functions.
- Client-side Pandera validation schemas that reject malformed ticks at connector boundaries.
- Rapid, single-command PowerShell workflows via `tasks.ps1`.

## What Bad Looks Like
- 60/30/10 Violation: Putting heuristic LLM logic or text reasoning inside pricing or risk solvers.
- Writing boilerplate, manual event-loop `blpapi` code instead of using `xbbg`.
- Hand-crafting custom valuation models via low-level `QuantLib` primitives instead of leveraging `OpenSourceRisk` (ORE).
- Building enterprise web authentication or CORS layers for internal desktop tools.
- Importing unverified code from `lab/` into `engines/`.