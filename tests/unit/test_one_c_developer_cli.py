from pathlib import Path

from scripts.one_c_discover_source import run_discovery
from scripts.one_c_parse_export import parse_export
from scripts.one_c_run_import_pipeline import run_pipeline


def test_parse_export_script_function_is_safe_by_default() -> None:
    rows_count = parse_export(Path("tests/fixtures/one_c/exports/counterparties.json"))

    assert rows_count == 1


def test_discover_source_script_function_returns_status() -> None:
    status = run_discovery(Path("tests/fixtures/one_c/exports/counterparties.json"))

    assert status in {"completed", "unsupported_source"}


def test_import_pipeline_script_function_returns_status() -> None:
    status = run_pipeline()

    assert status in {
        "completed",
        "completed_with_warnings",
        "blocked_by_mapping_issues",
    }