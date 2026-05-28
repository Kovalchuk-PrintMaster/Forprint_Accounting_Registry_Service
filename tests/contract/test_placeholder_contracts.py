from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PLACEHOLDER_CONTRACTS_DIR = PROJECT_ROOT / "contracts" / "placeholders"


def load_yaml(relative_path: str) -> dict[str, Any]:
    path = PROJECT_ROOT / relative_path
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_placeholder_contracts_exist() -> None:
    required_files = [
        "accounting.invoice_request.v1.yaml",
        "accounting.payment_status_reference.v1.yaml",
        "accounting.finance_summary.v1.yaml",
        "accounting.one_c_import_result.v1.yaml",
    ]

    for file_name in required_files:
        assert (PLACEHOLDER_CONTRACTS_DIR / file_name).exists()


def test_placeholder_contracts_are_marked_non_canonical() -> None:
    required_files = [
        "contracts/placeholders/accounting.invoice_request.v1.yaml",
        "contracts/placeholders/accounting.payment_status_reference.v1.yaml",
        "contracts/placeholders/accounting.finance_summary.v1.yaml",
        "contracts/placeholders/accounting.one_c_import_result.v1.yaml",
    ]

    for relative_path in required_files:
        contract = load_yaml(relative_path)
        assert contract["fixture_status"] == "placeholder"
        assert contract["canonical_contract_truth"] == "forprint_library_future"