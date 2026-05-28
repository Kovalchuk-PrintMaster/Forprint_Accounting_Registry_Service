from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def read_file(relative_path: str) -> str:
    return (PROJECT_ROOT / relative_path).read_text(encoding="utf-8")


def test_readme_explicitly_denies_crm_operational_registry_and_library_roles() -> None:
    readme = read_file("README.md")

    assert "It is not CRM." in readme
    assert "It is not Operational Registry." in readme
    assert "It is not ForPrint Library." in readme
    assert "It is not Integration Gateway." in readme
    assert "It is not Calculator." in readme


def test_boundary_docs_exist() -> None:
    required_docs = [
        "docs/architecture/accounting_registry_boundaries.md",
        "docs/architecture/one_c_boundary.md",
        "docs/architecture/accounting_vs_operational_registry.md",
        "docs/development/model_naming_rules.md",
    ]

    for relative_path in required_docs:
        assert (PROJECT_ROOT / relative_path).exists()


def test_accounting_registry_boundary_doc_forbids_operational_ownership() -> None:
    content = read_file("docs/architecture/accounting_registry_boundaries.md")

    forbidden_phrases = [
        "client registry",
        "order registry",
        "warehouse stock",
        "material catalog",
        "product catalog",
        "CRM dashboard state",
        "business workflow decisions",
        "integration routing",
        "architecture governance",
    ]

    for phrase in forbidden_phrases:
        assert phrase in content