---
okf_version: "0.2"
id: "journal-retrospectives-context"
type: "procedure"
title: "Trade Retrospectives Workspace Context"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["journal", "retrospectives", "post-mortem", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "journal/CONTEXT.md"
summary: "Protocol for trade post-mortems, attribution audits, and mandate compliance reviews."
---

# Journal: Trade Retrospectives

Audits closed trades, mandate performance, and execution slippage.

## Inputs
- Layer 3 (reference): `journal/mandate.md`
- Layer 4 (working): Execution fills and trade logs from `journal/entries/`

## Process
1. Reconstruct lifecycle of closed positions.
2. Attribute realized PnL: carry, curve, spread, execution friction.
3. Compare realized outcome with original research hypothesis.

## Outputs
- `YYYY-MM-DD_[ticket-id]_retro.md`
