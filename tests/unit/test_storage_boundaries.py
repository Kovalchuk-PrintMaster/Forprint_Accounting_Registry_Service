from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
STORAGE_MODELS_PATH = (
    PROJECT_ROOT
    / "app"
    / "forprint_accounting_registry_service"
    / "storage"
    / "models.py"
)


def test_storage_models_do_not_introduce_forbidden_canonical_model_names() -> None:
    content = STORAGE_MODELS_PATH.read_text(encoding="utf-8")

    forbidden_class_markers = [
        "class Client(",
        "class Customer(",
        "class Order(",
        "class Product(",
        "class Material(",
        "class Invoice(",
        "class Payment(",
    ]

    for marker in forbidden_class_markers:
        assert marker not in content


def test_storage_models_use_explicit_accounting_and_one_c_names() -> None:
    content = STORAGE_MODELS_PATH.read_text(encoding="utf-8")

    required_names = [
        "OneCRawSnapshot",
        "OneCStagingRecord",
        "OneCMappingRecord",
        "OneCImportJob",
        "OneCExportJob",
        "AccountingReconciliationJob",
        "AccountingDocument",
        "InvoiceAccountingReference",
        "PaymentAccountingReference",
        "OrderAccountingReference",
    ]

    for name in required_names:
        assert name in content


def test_storage_boundary_docs_exist() -> None:
    required_docs = [
        "docs/architecture/accounting_storage_foundation.md",
        "docs/architecture/one_c_snapshot_staging_flow.md",
        "docs/architecture/accounting_storage_boundaries.md",
    ]

    for relative_path in required_docs:
        assert (PROJECT_ROOT / relative_path).exists()