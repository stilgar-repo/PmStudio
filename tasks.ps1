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
        Write-Host "07:30 Morning Setup: [TODO] Ingest positions, verify headroom, initialize daily desk log." -ForegroundColor Yellow
    }
    "reconcile" {
        Write-Host "Reconcile: [TODO] Reconcile fills against staged intent and attribute variance." -ForegroundColor Yellow
    }
    "export-bi" {
        Write-Host "Export BI: [TODO] Generate flat calculation snapshot for Power BI / Excel." -ForegroundColor Yellow
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
        Write-Host "Setup Hooks: [TODO] Initialize git pre-commit hooks (waiting on uv setup)." -ForegroundColor Yellow
    }
}
