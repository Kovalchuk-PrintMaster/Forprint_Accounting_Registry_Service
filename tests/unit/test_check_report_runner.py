from scripts.run_accounting_registry_checks import (
    CheckResult,
    all_checks_passed,
    build_report_payload,
    render_markdown_report,
)


def test_all_checks_passed_returns_true_when_everything_is_ok() -> None:
    results = [
        CheckResult(
            name="Ruff lint",
            expected="No lint errors",
            status="OK",
            duration_seconds=0.1,
        ),
        CheckResult(
            name="Pytest",
            expected="All tests pass",
            status="OK",
            duration_seconds=0.2,
        ),
    ]

    assert all_checks_passed(results) is True


def test_all_checks_passed_returns_false_when_any_check_fails() -> None:
    results = [
        CheckResult(
            name="Ruff lint",
            expected="No lint errors",
            status="OK",
            duration_seconds=0.1,
        ),
        CheckResult(
            name="Pytest",
            expected="All tests pass",
            status="FAIL",
            duration_seconds=0.2,
            details="example failure",
        ),
    ]

    assert all_checks_passed(results) is False


def test_build_report_payload_contains_project_status_and_checks() -> None:
    results = [
        CheckResult(
            name="Boundary files",
            expected="Files exist",
            status="OK",
            duration_seconds=0.01,
        )
    ]

    payload = build_report_payload(results)

    assert payload["project"] == "ForPrint Accounting Registry Service"
    assert payload["report_type"] == "boundary_check_report"
    assert payload["status"] == "OK"
    assert payload["checks"][0]["name"] == "Boundary files"


def test_render_markdown_report_contains_table_and_status() -> None:
    results = [
        CheckResult(
            name="Module manifest validation",
            expected="Manifest is valid",
            status="OK",
            duration_seconds=0.03,
        )
    ]

    markdown = render_markdown_report(results)

    assert "# ForPrint Accounting Registry Service — check report" in markdown
    assert "Overall status: **OK**" in markdown
    assert "| Перевірка | Очікуваний результат | Статус | Час |" in markdown
    assert "Module manifest validation" in markdown