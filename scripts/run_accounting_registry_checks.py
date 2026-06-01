# python scripts/run_accounting_registry_checks.py

"""
Script name:
    run_accounting_registry_checks.py

Description:
    Boundary-focused check runner for ForPrint Accounting Registry Service.

Purpose:
    Runs lint, tests, boundary validations, storage checks, OneC I/O checks,
    v0.5 parser/pipeline/fixture checks, and generates terminal, JSON, and Markdown reports.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.table import Table

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"
JSON_REPORT_PATH = REPORTS_DIR / "accounting_registry_check_report.json"
MARKDOWN_REPORT_PATH = REPORTS_DIR / "accounting_registry_check_report.md"

REQUIRED_BOUNDARY_FILES = [
    "README.md",
    "forprint_module_manifest.yaml",
    "docs/architecture/accounting_registry_boundaries.md",
    "docs/architecture/one_c_boundary.md",
    "docs/architecture/accounting_vs_operational_registry.md",
    "docs/development/model_naming_rules.md",
    "docs/architecture/accounting_storage_foundation.md",
    "docs/architecture/one_c_snapshot_staging_flow.md",
    "docs/architecture/accounting_storage_boundaries.md",
    "docs/architecture/one_c_io_strategy.md",
    "docs/architecture/one_c_adapter_boundary.md",
    "docs/architecture/one_c_mapping_policy.md",
    "docs/architecture/one_c_read_write_policy.md",
    "docs/architecture/one_c_version_strategy.md",
    "docs/architecture/one_c_test_copy_policy.md",
    "docs/architecture/one_c_directory_exchange.md",
    "docs/architecture/one_c_report_extraction.md",
    "docs/architecture/one_c_sandbox_direct_io.md",
    "contracts/placeholders/accounting.invoice_request.v1.yaml",
    "contracts/placeholders/accounting.payment_status_reference.v1.yaml",
    "contracts/placeholders/accounting.finance_summary.v1.yaml",
    "contracts/placeholders/accounting.one_c_import_result.v1.yaml",
]

REQUIRED_V05_FILES = [
    "app/forprint_accounting_registry_service/one_c_io/sanitization.py",
    "app/forprint_accounting_registry_service/one_c_io/test_database_registry.py",
    "app/forprint_accounting_registry_service/one_c_io/file_formats.py",
    "app/forprint_accounting_registry_service/one_c_io/export_detection.py",
    "app/forprint_accounting_registry_service/one_c_io/export_parsers.py",
    "app/forprint_accounting_registry_service/one_c_io/schema_probe.py",
    "app/forprint_accounting_registry_service/one_c_io/import_pipeline.py",
    "app/forprint_accounting_registry_service/storage/mapping_models.py",
    "app/forprint_accounting_registry_service/repositories/mapping_issues.py",
    "app/forprint_accounting_registry_service/services/mapping_issue_registry.py",
    "scripts/one_c_discover_source.py",
    "scripts/one_c_parse_export.py",
    "scripts/one_c_run_import_pipeline.py",
]

REQUIRED_MANIFEST_OWNS = {
    "invoice",
    "payment",
    "payment_status",
    "accounting_document",
    "one_c_raw_snapshot",
    "one_c_staging_record",
    "one_c_mapping_record",
    "accounting_reconciliation_report",
    "accounting_reference_projection",
}

REQUIRED_MANIFEST_MUST_NOT_OWN = {
    "client_registry",
    "order_registry",
    "operational_task_registry",
    "production_status",
    "warehouse_stock",
    "material_catalog",
    "product_catalog",
    "price_calculation",
    "crm_dashboard_state",
    "customer_interaction_history",
    "business_workflow_decisions",
    "integration_routing",
    "architecture_governance",
}

PLACEHOLDER_CONTRACTS = [
    "contracts/placeholders/accounting.invoice_request.v1.yaml",
    "contracts/placeholders/accounting.payment_status_reference.v1.yaml",
    "contracts/placeholders/accounting.finance_summary.v1.yaml",
    "contracts/placeholders/accounting.one_c_import_result.v1.yaml",
]

STORAGE_MODELS_PATH = (
    PROJECT_ROOT / "app" / "forprint_accounting_registry_service" / "storage" / "models.py"
)
ONE_C_IO_ROOT = PROJECT_ROOT / "app" / "forprint_accounting_registry_service" / "one_c_io"

FORBIDDEN_MODEL_MARKERS = [
    "class Client(",
    "class Customer(",
    "class Order(",
    "class Product(",
    "class Material(",
    "class WarehouseStock(",
    "class ProductionStatus(",
]

SANITIZED_FIXTURE_FILES = [
    "examples/one_c/directories/counterparty_directory.yaml",
    "examples/one_c/reports/payment_register_snapshot.yaml",
    "examples/one_c/export_packages/invoice_dry_run_export.yaml",
    "examples/one_c/write_experiments/write_experiment_example.yaml",
]

TEST_FIXTURE_FILES = [
    "tests/fixtures/one_c/exports/counterparties.json",
    "tests/fixtures/one_c/exports/counterparties.csv",
    "tests/fixtures/one_c/exports/counterparties.xml",
    "tests/fixtures/one_c/exports/payment_register.yaml",
]

REQUIRED_GITIGNORE_PATTERNS = [
    "local_sandbox/",
    "local_sandbox/one_c_working_copies/",
    "*.1CD",
    "*.dt",
    "*.cf",
    "*.bak",
    "*.dump",
    "*.sqlite",
    "*.db",
]


@dataclass(frozen=True)
class CheckResult:
    """One check result for terminal, JSON, and Markdown reports."""

    name: str
    expected: str
    status: str
    duration_seconds: float
    details: str = ""


def run_subprocess_check(name: str, expected: str, command: list[str]) -> CheckResult:
    """Run a subprocess check and return structured result."""
    started_at = time.perf_counter()
    result = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    duration = time.perf_counter() - started_at

    details = ""
    if result.returncode != 0:
        details = "\n".join(
            item for item in [result.stdout.strip(), result.stderr.strip()] if item
        )

    return CheckResult(
        name=name,
        expected=expected,
        status="OK" if result.returncode == 0 else "FAIL",
        duration_seconds=duration,
        details=details,
    )


def validate_required_files(name: str, expected: str, files: list[str]) -> CheckResult:
    """Validate list of required files."""
    started_at = time.perf_counter()
    missing = [
            relative_path 
            for relative_path in files 
            if not (PROJECT_ROOT / relative_path).exists()
    ]

    return CheckResult(
        name=name,
        expected=expected,
        status="OK" if not missing else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details=", ".join(missing),
    )


def load_yaml_file(relative_path: str) -> dict[str, Any]:
    """Load YAML file from project root."""
    path = PROJECT_ROOT / relative_path
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_module_manifest() -> CheckResult:
    """Validate Accounting Registry module manifest boundary markers."""
    started_at = time.perf_counter()
    errors: list[str] = []

    try:
        manifest = load_yaml_file("forprint_module_manifest.yaml")
    except Exception as exc:  # noqa: BLE001
        return CheckResult(
            name="Module manifest validation",
            expected="Manifest is valid YAML and declares accounting boundary",
            status="FAIL",
            duration_seconds=time.perf_counter() - started_at,
            details=str(exc),
        )

    if manifest.get("module_id") != "forprint_accounting_registry_service":
        errors.append("module_id mismatch")

    if manifest.get("role") != "accounting_registry_and_one_c_boundary":
        errors.append("role mismatch")

    owns = set(manifest.get("owns", []))
    must_not_own = set(manifest.get("must_not_own", []))

    missing_owns = sorted(REQUIRED_MANIFEST_OWNS - owns)
    missing_forbidden = sorted(REQUIRED_MANIFEST_MUST_NOT_OWN - must_not_own)

    if missing_owns:
        errors.append(f"missing owns: {', '.join(missing_owns)}")

    if missing_forbidden:
        errors.append(f"missing must_not_own: {', '.join(missing_forbidden)}")

    return CheckResult(
        name="Module manifest validation",
        expected="Manifest declares accounting role, owns, and must_not_own",
        status="OK" if not errors else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details="; ".join(errors),
    )


def validate_placeholder_contracts() -> CheckResult:
    """Validate that placeholder contracts are marked as non-canonical."""
    started_at = time.perf_counter()
    errors: list[str] = []

    for relative_path in PLACEHOLDER_CONTRACTS:
        try:
            contract = load_yaml_file(relative_path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{relative_path}: {exc}")
            continue

        if contract.get("fixture_status") != "placeholder":
            errors.append(f"{relative_path}: fixture_status is not placeholder")

        if contract.get("canonical_contract_truth") != "forprint_library_future":
            errors.append(f"{relative_path}: canonical_contract_truth mismatch")

    return CheckResult(
        name="Placeholder contract validation",
        expected="Local contracts are placeholders and non-canonical",
        status="OK" if not errors else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details="; ".join(errors),
    )


def validate_no_forbidden_storage_models() -> CheckResult:
    """Validate that storage models do not introduce forbidden canonical classes."""
    started_at = time.perf_counter()

    if not STORAGE_MODELS_PATH.exists():
        return CheckResult(
            name="Storage model boundary validation",
            expected="Storage models exist and avoid forbidden canonical names",
            status="FAIL",
            duration_seconds=time.perf_counter() - started_at,
            details=f"Missing: {STORAGE_MODELS_PATH}",
        )

    content = STORAGE_MODELS_PATH.read_text(encoding="utf-8")
    forbidden_found = [marker for marker in FORBIDDEN_MODEL_MARKERS if marker in content]

    return CheckResult(
        name="Storage model boundary validation",
        expected="No canonical Client/Order/Product/Material/Warehouse/Production models",
        status="OK" if not forbidden_found else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details=", ".join(forbidden_found),
    )


def validate_one_c_io_boundary() -> CheckResult:
    """Validate that OneC I/O package does not introduce forbidden ownership."""
    started_at = time.perf_counter()

    if not ONE_C_IO_ROOT.exists():
        return CheckResult(
            name="OneC I/O boundary validation",
            expected="OneC I/O package exists and avoids forbidden canonical models",
            status="FAIL",
            duration_seconds=time.perf_counter() - started_at,
            details=f"Missing: {ONE_C_IO_ROOT}",
        )

    content = "\n".join(
        path.read_text(encoding="utf-8") for path in ONE_C_IO_ROOT.glob("*.py")
    )
    forbidden_found = [marker for marker in FORBIDDEN_MODEL_MARKERS if marker in content]

    return CheckResult(
        name="OneC I/O boundary validation",
        expected="No canonical Client/Order/Product/Material/Warehouse/Production models",
        status="OK" if not forbidden_found else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details=", ".join(forbidden_found),
    )


def validate_fixture_safety() -> CheckResult:
    """Validate committed examples are sanitized and non-production."""
    started_at = time.perf_counter()
    errors: list[str] = []

    for relative_path in SANITIZED_FIXTURE_FILES:
        path = PROJECT_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing fixture: {relative_path}")
            continue

        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        if payload.get("fixture_status") != "example":
            errors.append(f"{relative_path}: fixture_status mismatch")
        if payload.get("real_1c_data") is not False:
            errors.append(f"{relative_path}: real_1c_data must be false")
        if payload.get("sanitized") is not True:
            errors.append(f"{relative_path}: sanitized must be true")
        if payload.get("production_allowed") is not False:
            errors.append(f"{relative_path}: production_allowed must be false")

    return CheckResult(
        name="Fixture safety validation",
        expected="Committed examples are sanitized, examples and non-production",
        status="OK" if not errors else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details="; ".join(errors),
    )


def validate_test_fixtures_exist() -> CheckResult:
    """Validate parser/import test fixtures exist."""
    return validate_required_files(
        name="v0.5 test fixture validation",
        expected="Sanitized parser/import fixtures exist",
        files=TEST_FIXTURE_FILES,
    )


def validate_gitignore_sandbox_rules() -> CheckResult:
    """Validate local sandbox and large DB-like files are ignored."""
    started_at = time.perf_counter()
    gitignore_path = PROJECT_ROOT / ".gitignore"

    if not gitignore_path.exists():
        return CheckResult(
            name="Gitignore sandbox validation",
            expected="Local sandbox paths and DB files are ignored",
            status="FAIL",
            duration_seconds=time.perf_counter() - started_at,
            details="Missing .gitignore",
        )

    content = gitignore_path.read_text(encoding="utf-8")
    missing = [pattern for pattern in REQUIRED_GITIGNORE_PATTERNS if pattern not in content]

    return CheckResult(
        name="Gitignore sandbox validation",
        expected="local_sandbox and DB-like files are ignored",
        status="OK" if not missing else "FAIL",
        duration_seconds=time.perf_counter() - started_at,
        details=", ".join(missing),
    )


def all_checks_passed(results: list[CheckResult]) -> bool:
    """Return True if all checks passed."""
    return all(result.status == "OK" for result in results)


def build_report_payload(results: list[CheckResult]) -> dict[str, Any]:
    """Build JSON-serializable report payload."""
    return {
        "project": "ForPrint Accounting Registry Service",
        "report_type": "boundary_check_report",
        "status": "OK" if all_checks_passed(results) else "FAIL",
        "checks": [asdict(result) for result in results],
    }


def render_markdown_report(results: list[CheckResult]) -> str:
    """Render Markdown report."""
    lines = [
        "# ForPrint Accounting Registry Service — check report",
        "",
        f"Overall status: **{'OK' if all_checks_passed(results) else 'FAIL'}**",
        "",
        "| Перевірка | Очікуваний результат | Статус | Час |",
        "|---|---|---:|---:|",
    ]

    for result in results:
        lines.append(
            "| "
            f"{result.name} | "
            f"{result.expected} | "
            f"{result.status} | "
            f"{result.duration_seconds:.2f}s |"
        )

    failed_details = [result for result in results if result.status != "OK" and result.details]

    if failed_details:
        lines.extend(["", "## Failure details", ""])
        for result in failed_details:
            lines.extend([f"### {result.name}", "", "```text", result.details, "```", ""])

    return "\n".join(lines) + "\n"


def write_reports(results: list[CheckResult]) -> None:
    """Write JSON and Markdown reports to reports directory."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    JSON_REPORT_PATH.write_text(
        json.dumps(build_report_payload(results), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    MARKDOWN_REPORT_PATH.write_text(render_markdown_report(results), encoding="utf-8")


def render_terminal_table(results: list[CheckResult]) -> None:
    """Render a readable terminal table."""
    console = Console()

    table = Table(title="ForPrint Accounting Registry Service — check report")
    table.add_column("Перевірка", style="cyan", no_wrap=True)
    table.add_column("Очікуваний результат", style="white")
    table.add_column("Статус", justify="center")
    table.add_column("Час", justify="right")

    for result in results:
        status_text = "[green]OK[/green]" if result.status == "OK" else "[red]FAIL[/red]"
        table.add_row(
            result.name,
            result.expected,
            status_text,
            f"{result.duration_seconds:.2f}s",
        )

    console.print(table)


def run_all_checks() -> list[CheckResult]:
    """Run all local checks."""
    return [
        run_subprocess_check(
            name="Ruff lint",
            expected="Немає lint-помилок у app/tests/scripts",
            command=[sys.executable, "-m", "ruff", "check", "app", "tests", "scripts"],
        ),
        run_subprocess_check(
            name="Pytest",
            expected="Усі тести проходять",
            command=[sys.executable, "-m", "pytest", "-q"],
        ),
        validate_required_files(
            name="Boundary, storage and OneC files",
            expected="Boundary docs, storage docs, OneC docs, manifest and placeholders exist",
            files=REQUIRED_BOUNDARY_FILES,
        ),
        validate_required_files(
            name="v0.5 implementation files",
            expected="Sanitized source intake, export parser and pipeline files exist",
            files=REQUIRED_V05_FILES,
        ),
        validate_module_manifest(),
        validate_placeholder_contracts(),
        validate_no_forbidden_storage_models(),
        validate_one_c_io_boundary(),
        validate_fixture_safety(),
        validate_test_fixtures_exist(),
        validate_gitignore_sandbox_rules(),
    ]


def main() -> int:
    """Run checks and generate reports."""
    console = Console()
    console.print("🔎 Running ForPrint Accounting Registry Service checks...")

    results = run_all_checks()

    for result in results:
        style = "green" if result.status == "OK" else "red"
        console.print(
            f"  - {result.name}: [{style}]{result.status}[/{style}] "
            f"({result.duration_seconds:.2f}s)"
        )

    render_terminal_table(results)
    write_reports(results)

    console.print(f"📄 JSON report: {JSON_REPORT_PATH}")
    console.print(f"📄 Markdown report: {MARKDOWN_REPORT_PATH}")

    if all_checks_passed(results):
        console.print("✅ Check report completed successfully.")
        return 0

    console.print("❌ Check report failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())