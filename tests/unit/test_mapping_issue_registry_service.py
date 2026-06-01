from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality
from forprint_accounting_registry_service.services.mapping_issue_registry import (
    persist_mapping_result,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session


def test_mapping_issue_registry_persists_policy_result() -> None:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    with Session(engine) as session:
        result = apply_mapping_policy(
            source_payload={"Unknown": "preserve"},
            definitions=[
                FieldMappingDefinition(
                    source_field="Код",
                    target_field="one_c_code",
                    required=True,
                    criticality=FieldCriticality.CRITICAL,
                )
            ],
        )

        stored = persist_mapping_result(session, result, staging_record_id="staging-001")

        assert len(stored) == 2
        assert any(issue.status == "manual_review_required" for issue in stored)