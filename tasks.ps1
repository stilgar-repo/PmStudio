# Requires Windows PowerShell 5.1
param (
    [Parameter(Position=0, Mandatory=$true)]
    [ValidateSet("morning", "reconcile", "export-bi", "check", "spike", "setup-hooks")]
    [string]$Action,

    [Parameter(Position=1)]
    [string]$Target
)

$ErrorActionPreference = "Stop"

switch ($Action) {
    "morning" {
        Write-Host "Running 07:30 Morning Setup..." -ForegroundColor Cyan
        uv run python -m engines.cli.ops.morning_runner
    }
    "reconcile" {
        Write-Host "Reconciling portfolio fills against intent..." -ForegroundColor Cyan
        uv run python -m engines.cli.ops.reconcile
    }
    "export-bi" {
        Write-Host "Exporting Python-calculated snapshot for Power BI / Excel..." -ForegroundColor Cyan
        uv run python -m engines.cli.ops.export_bi
    }
    "check" {
        if (-not $Target) { $Target = "engines/" }
        Write-Host "Running targeted validation on $Target..." -ForegroundColor Cyan
        uv run ruff check $Target
        uv run mypy $Target
    }
    "spike" {
        if (-not $Target) { 
            throw "Specify research inquiry name. Usage: .\tasks.ps1 spike <inquiry_name>" 
        }
        $dest = "lab\wip_$Target"
        if (Test-Path -Path $dest) {
            throw "Target directory $dest already exists."
        }
        Copy-Item -Recurse -Path "lab\workspace-template" -Destination $dest
        Write-Host "Spawned new research workspace: $dest" -ForegroundColor Green
    }
    "setup-hooks" {
        Write-Host "Installing pre-commit hooks into .git/..." -ForegroundColor Cyan
        uv run pre-commit install
        if (-not (Test-Path -Path ".secrets.baseline")) {
            Write-Host "Generating initial secrets baseline..." -ForegroundColor Cyan
            uv run detect-secrets scan > .secrets.baseline
        }
        Write-Host "[SUCCESS] Pre-commit boundary hooks armed." -ForegroundColor Green
    }
}