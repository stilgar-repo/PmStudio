---
okf_version: "0.2"
id: "findings-template"
type: "inquiry"
title: "Findings: [Hypothesis Title]"
status: "draft"
created: 2026-09-07
updated: 2026-09-07
tags: ["research-findings", "verdict", "substrate-audit"]
relations:
  - rel: "validates"
    ref: "PRP.md"
summary: "Empirical findings, realized metrics, and substrate promotion audit for [Hypothesis Title]."
---

# Findings: [Hypothesis Title]

## 1. Empirical Verdict
- Realized Net Return / Spread Performance:
- Net Sharpe / Information Ratio (after haircut drag & trading frictions):
- Maximum Observed Drawdown:
- Terminal Verdict: `[validated | falsified | inconclusive]`

## 2. Structural Takeaways
- Did institutional market plumbing behave as expected?
- Observed financing frictions (repo availability, margin call stability):

## 3. Substrate Nomination Audit (60/30/10 Compliance)
- [ ] **60% Infrastructure:** Data queried live from Snowflake/Bloomberg; zero local disk caching.
- [ ] **30% Ingress Contract:** Input DataFrames validated against Pandera schemas.
- [ ] **30% Single Source of Truth:** Mathematical calculations match production formulas in `engines/quant/`.
- [ ] **30% Orchestration:** Pure functions isolated; inputs parameterized.
- [ ] **30% Typing:** Strict typing verified with `uv run mypy <module_path>`.
- [ ] **30% Parity:** Analytical benchmark parity verified ($|\Delta| \le 10^{-8}$) via `pytest-regressions`.
- [ ] **30% Tests:** Targeted unit test written for test suite.
- [ ] **10% AI:** Model restricted to hypothesis framing and summary synthesis; no runtime calculation.

## 4. Promotion Sign-off
- Promoted to `engines/`: `[Yes | No]`
- Destination Target: `engines/<module_name>.py`