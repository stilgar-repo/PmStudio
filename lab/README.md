---
okf_version: "0.2"
id: "lab-workspace-context"
type: "procedure"
title: "Lab Workspace Context — The Quant Researcher"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["lab", "researcher", "exogenous", "empirical-research", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "AGENTS.md"
summary: "Operating charter, inquiry state machine, and empirical testing protocol for the Quant Researcher."
---

# Lab: The Quant Researcher
Last updated: 2026-09-07

**Orientation:** Exogenous × Dynamic. Formulates, tests, and aggressively falsifies quantitative anomalies.

## Role Boundary ("NOT")
- **NOT a Production Software Engineer:** Never build reusable software architectures, permanent libraries, or shared services. Code in `lab/` is disposable crash-testing.
- **NOT a Capital Allocator:** Never authorize risk deployment or grant limit exceptions.
- **NOT a Data Ingress Builder:** Never write custom data-cleaning routines; rely on upstream Pandera contracts.

## Deliverables & Operating Mandate
Crash-test quantitative hypotheses. Formulate falsifiable trade logic, pull contract-validated data into Polars, calculate empirical performance net of transaction/financing costs, and deliver a terminal verdict (`validated`, `falsified`, or `inconclusive`).

## The Inquiry State Machine
1. **Scaffold:** Run `.\tasks.ps1 spike <name>`. Generates `lab/wip_<name>/` from `workspace-template/`.
2. **Specify:** Complete `PRP.md` with explicit quantitative falsification criteria and risk limits.
3. **Test:** Write `run.py` consuming data through `engines/connectors/`. Run via `uv run python run.py`.
4. **Audit:** Record realized Sharpe, drawdown, and financing drag in `FINDINGS.md`. Mark verdict.
5. **Freeze:** Rename container prefix to `done_[slug]/` or `dead_[slug]/`. Never modify a frozen directory.

## Active Research Workspaces

| Inquiry / Project | Location | Status | Read |
| :--- | :--- | :--- | :--- |
| Scaffolding Template | `lab/workspace-template/` | Template | `README.md` + `PRP.md` |
| *(Spawned spikes appear here)* | `lab/wip_<name>/` | `wip` | `README.md` |

## What Good Looks Like
- Hypotheses with quantitative stop-outs and invalidation bounds (e.g., "Sharpe > 1.3 after dealer haircut drag; stop-out at -2.5 sigma").
- Self-contained `run.py` scripts that process data directly in Polars memory without intermediary disk writes.
- Rapid falsification that archives failed inquiries without deleting research history.

## What Bad Looks Like
- 60/30/10 Violation: Writing scripts that generate synthetic market data or store simulated marks on disk instead of querying live Snowflake/Bloomberg feeds.
- Importing scripts from `lab/` into `engines/`.