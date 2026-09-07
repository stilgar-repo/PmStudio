---
okf_version: "0.2"
id: "financing-matrix"
type: "covenant"
title: "Counterparty Credit Facilities & Haircut Matrix"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["financing", "repo", "haircuts", "prime-broker"]
relations:
  - rel: "depends_on"
    ref: "journal/README.md"
summary: "Active counterparty credit terms, baseline repo haircuts, and facility capacity limits."
---

# Counterparty Credit & Financing Matrix

## 1. Haircut Schedule by Asset Class
- Sovereign Debt (0-3Y Maturity): 0.50% - 1.00%
- Sovereign Debt (3-10Y Maturity): 1.50% - 2.00%
- Sovereign Debt (10-30Y Maturity): 3.00% - 4.00%
- Investment Grade Supranationals: 2.50% - 3.50%

## 2. Counterparty Facilities

| Dealer / Custodian | Facility Type | Limit (USD) | Benchmark Spread | Status |
| :--- | :--- | :--- | :--- | :--- |
| Dealer A | Bilateral Repo | 150M | SOFR + 8 bps | Active |
| Dealer B | Tri-party Repo | 200M | SOFR + 6 bps | Active |
| Dealer C | Sponsored FICC Repo | 100M | SOFR + 4 bps | Active |