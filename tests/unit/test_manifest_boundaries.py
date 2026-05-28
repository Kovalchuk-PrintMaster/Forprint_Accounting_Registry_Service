from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = PROJECT_ROOT / "forprint_module_manifest.yaml"


def load_manifest() -> dict[str, Any]:
    return yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_manifest_declares_correct_module_id_and_role() -> None:
    manifest = load_manifest()

    assert manifest["module_id"] == "forprint_accounting_registry_service"
    assert manifest["role"] == "accounting_registry_and_one_c_boundary"
    assert manifest["status"] == "boundary_correction_development"


def test_manifest_declares_accounting_owns() -> None:
    manifest = load_manifest()
    owns = set(manifest["owns"])

    required = {
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

    assert required.issubset(owns)


def test_manifest_declares_must_not_own_operational_objects() -> None:
    manifest = load_manifest()
    must_not_own = set(manifest["must_not_own"])

    required_forbidden = {
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

    assert required_forbidden.issubset(must_not_own)