# Quantitative Portfolio Studio

Analytical copilot and macro scribe for a multi-asset quantitative investment portfolio.
Advisory and staging only; zero automated execution authority. Snowflake is the sole book of record.
Every markdown file must begin with an OKF v0.2 frontmatter block (`okf_version: "0.2"`).

## Environment

- OS: Windows 11 | Shell: Windows PowerShell 5.1 (`$env:VAR`, no `&&`)
- Python: 3.14 via `uv` | VCS: Azure DevOps Git (conventional commits)
- Local Gates: `pre-commit` (Ruff, secret detection, OKF frontmatter checks)
- Type Checking: `uv run mypy <path>` (strict) | Tests: `uv run pytest <path>` (targeted only)
- Feeds & Storage: Bloomberg API (`localhost:8194`), Snowflake CLI (`snow`)

## Root Routing

| Task | Go to | Read |
| :--- | :--- | :--- |
| Portfolio setup, risk audit, staging | /journal | CONTEXT.md + mandate.md |
| Quantitative research or RV spike | /lab | CONTEXT.md + workspace-template/PRP.md |
| Market structure, reg rules, proofs | /commons | CONTEXT.md |
| Pure math, connectors, BI exports | /engines | CONTEXT.md + pyproject.toml |

## Primary Tasks (PowerShell 5.1)

| Action | Command |
| :--- | :--- |
| Morning desk setup | `.\tasks.ps1 morning` |
| Export BI flat snapshot | `.\tasks.ps1 export-bi` |
| Run targeted code checks | `.\tasks.ps1 check <path>` |
| Scaffold research spike | `.\tasks.ps1 spike <name>` |
| Initialize git pre-commit hooks | `.\tasks.ps1 setup-hooks` |

## Invariants

- State lives only in Snowflake; code lives in Git. Never persist portfolio state in local files.
- Math functions in `engines/` are pure and zero-I/O; code in `engines/` never imports from `lab/`.
- Downstream tools (Power BI, Excel) are display-only; all metrics derive in Python.