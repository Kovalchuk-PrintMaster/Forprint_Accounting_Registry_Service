from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_example_fixtures_are_sanitized_and_non_production() -> None:
    fixture_paths = [
        PROJECT_ROOT / "examples/one_c/directories/counterparty_directory.yaml",
        PROJECT_ROOT / "examples/one_c/reports/payment_register_snapshot.yaml",
        PROJECT_ROOT / "examples/one_c/export_packages/invoice_dry_run_export.yaml",
        PROJECT_ROOT / "examples/one_c/write_experiments/write_experiment_example.yaml",
    ]

    for path in fixture_paths:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert payload["fixture_status"] == "example"
        assert payload["real_1c_data"] is False
        assert payload["sanitized"] is True
        assert payload["production_allowed"] is False


def test_local_sandbox_paths_are_gitignored() -> None:
    gitignore = (PROJECT_ROOT / ".gitignore").read_text(encoding="utf-8")

    required_patterns = [
        "local_sandbox/",
        "*.1CD",
        "*.dt",
        "*.cf",
        "*.bak",
        "*.dump",
        "*.sqlite",
        "*.db",
    ]

    for pattern in required_patterns:
        assert pattern in gitignore