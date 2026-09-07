---
okf_version: "0.2"
id: "portfolio-mandate"
type: "covenant"
title: "Fiduciary Portfolio Mandate & Risk Covenants"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["governance", "mandate", "risk-limits", "covenants"]
relations:
  - rel: "depends_on"
    ref: "journal/README.md"
summary: "Constitutional risk envelope, maximum leverage, factor constraints, and capital drawdown stop-outs."
---

# Fiduciary Mandate & Risk Limits

## 1. Capital Preservation & Drawdown Bounds
- Maximum Drawdown (Trailing Peak-to-Trough): 5.0% (Triggers mandatory portfolio de-risking by 50%).
- Terminal Stop-Out: 8.0% (Triggers liquidation to cash and formal investment committee review).
- Unencumbered Cash Reserve Floor: Minimum 15.0% of total Net Asset Value (NAV).

## 2. Sensitivity & Factor Limits
- Portfolio Net DV01: Bound strictly within [-USD 25,000, +USD 25,000] per 1 bp parallel shift.
- Portfolio Gross DV01: Bound within [USD 0, USD 120,000].
- Maximum Curve Convexity Exposure: USD 5,000 per 1 bp butterfly shift.
- Maximum Single-Sovereign Concentration: 35.0% of total Gross Notional Exposure.

## 3. Leverage & Financing Bounds
- Maximum Gross Regulatory Leverage: 8.0x NAV.
- Overnight Repo Concentration: No single counterparty may exceed 30.0% of total financing volume.