from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ONE_C_IO_ROOT = (
    PROJECT_ROOT
    / "app"
    / "forprint_accounting_registry_service"
    / "one_c_io"
)


def test_required_one_c_io_docs_exist() -> None:
    required_docs = [
        "docs/architecture/one_c_io_strategy.md",
        "docs/architecture/one_c_adapter_boundary.md",
        "docs/architecture/one_c_mapping_policy.md",
        "docs/architecture/one_c_read_write_policy.md",
        "docs/architecture/one_c_version_strategy.md",
        "docs/architecture/one_c_test_copy_policy.md",
    ]

    for relative_path in required_docs:
        assert (PROJECT_ROOT / relative_path).exists()


def test_one_c_io_package_does_not_introduce_forbidden_canonical_models() -> None:
    content = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ONE_C_IO_ROOT.glob("*.py")
    )

    forbidden_markers = [
        "class Client(",
        "class Customer(",
        "class Order(",
        "class Product(",
        "class Material(",
        "class WarehouseStock(",
        "class ProductionStatus(",
    ]

    for marker in forbidden_markers:
        assert marker not in content


def test_one_c_io_docs_document_test_copy_policy() -> None:
    content = (
        PROJECT_ROOT / "docs" / "architecture" / "one_c_test_copy_policy.md"
    ).read_text(encoding="utf-8")

    assert "test copy" in content
    assert "read_only: true" in content
    assert "production_allowed: false" in content
    assert "writes_allowed: false" in content
    assert "requires_test_copy: true" in content