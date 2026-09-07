---
okf_version: "0.2"
id: "journal-entries-context"
type: "procedure"
title: "Daily Entries Workspace Context"
status: "active"
created: 2026-09-07
updated: 2026-09-07
tags: ["journal", "entries", "daily-log", "okf-v0.2"]
relations:
  - rel: "depends_on"
    ref: "journal/CONTEXT.md"
summary: "Operating protocol for recording daily desk setup, intraday risk headroom, and operational logs."
---

# Journal: Daily Entries

Records the operational day-to-day log of the Portfolio Manager.

## Inputs
- Layer 3 (reference): `journal/mandate.md`
- Layer 3 (reference): `journal/financing.md`
- Layer 4 (working): Live positions snapshot via `engines.cli.ops.morning_runner`

## Process
1. Initialize date-stamped log file: `YYYY-MM-DD_desk-log.md`.
2. Record starting headroom vs. mandate limits.
3. Log intraday staged execution tickets.
4. Record end-of-day summary and carry-forward notes.

## Outputs
- `YYYY-MM-DD_desk-log.md`
