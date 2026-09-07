---
okf_version: "0.2"
id: "prp-template"
type: "inquiry"
title: "PRP: [Hypothesis Title]"
status: "draft"
created: 2026-09-07
updated: 2026-09-07
tags: ["research", "hypothesis", "empirical-test"]
relations:
  - rel: "depends_on"
    ref: "README.md"
summary: "Empirical hypothesis protocol, risk bounds, target metrics, and falsification triggers."
---

# PRP: [Hypothesis Title]

## 1. Economic Thesis & Structural Mechanism
- Primary trade expression:
- Structural driver causing the mispricing (concession, balance sheet constraint, collateral squeeze):
- Relevant institutional rules documented in `commons/`:

## 2. Quantitative Targets & Falsification Bounds
- Target Net Sharpe / Information Ratio:
- Maximum Net Risk Allocation (DV01 / Notional):
- Drawdown Invalidation Stop-Loss:
- Statistical Falsification Trigger (e.g., half-life > N days, basis widening > X bps):

## 3. Computational Blueprint
- Upstream Connectors: `engines/connectors/` (using `xbbg` for Bloomberg feeds)
- Applied Substrate Math: `engines/quant/` (using `OpenSourceRisk` / pure Polars)
- Execution Script: `run.py`