---
okf_version: "0.2"
id: "workspace-template-context"
type: "procedure"
title: "Child Workspace Context Template"
status: "draft"
created: 2026-09-07
updated: 2026-09-07
tags: ["template", "research", "inquiry", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "lab/README.md"
summary: "Local operating context and rules for this empirical research workspace."
---

# Research Workspace: [Inquiry Title]

## Mandate & Scope
[2-3 sentences defining the core dislocation, asset class, and structural hypothesis being tested.]

## Workspace Invariants
- Execution Script: `run.py`
- Hypothesis Protocol: `PRP.md`
- Audit & Verdict: `FINDINGS.md`
- Data Ingress: Directly via `engines/connectors/` into in-memory Polars DataFrames.
- Artifact Destination: In-memory or terminal `output.parquet`.

## Current Phase
[wip | done | dead]