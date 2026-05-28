from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
NAMING_RULES_PATH = PROJECT_ROOT / "docs" / "development" / "model_naming_rules.md"


def test_model_naming_rules_document_risky_names() -> None:
    content = NAMING_RULES_PATH.read_text(encoding="utf-8")

    risky_names = [
        "Client",
        "Customer",
        "Counterparty",
        "Product",
        "Material",
        "ProductTemplate",
        "CatalogItem",
    ]

    for name in risky_names:
        assert name in content


def test_model_naming_rules_define_preferred_accounting_projection_names() -> None:
    content = NAMING_RULES_PATH.read_text(encoding="utf-8")

    preferred_names = [
        "AccountingCounterpartyReference",
        "OneCCounterpartySnapshot",
        "AccountingCounterpartyProjection",
        "OneCNomenclatureSnapshot",
        "AccountingProductProjection",
        "InvoiceLineNomenclatureReference",
        "OrderAccountingReference",
        "InvoiceSourceReference",
        "ExternalOrderReference",
    ]

    for name in preferred_names:
        assert name in content