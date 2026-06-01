from forprint_accounting_registry_service.repositories.mapping_issues import (
    get_mapping_issue,
    mapping_completion_is_blocked,
    save_mapping_issue,
    update_mapping_issue_status,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from forprint_accounting_registry_service.storage.mapping_models import (
    DefaultValueDecisionStorage,
    FieldTypeMismatchIssueStorage,
    MappingIssueStatus,
    MappingIssueStorage,
    RequiredFieldMissingIssueStorage,
    UnmappedFieldRecordStorage,
)
from sqlmodel import Session


def create_test_session() -> Session:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)
    return Session(engine)


def test_mapping_issue_persists_and_status_can_be_updated() -> None:
    with create_test_session() as session:
        issue = save_mapping_issue(
            session,
            MappingIssueStorage(
                issue_type="required_field_missing",
                status=MappingIssueStatus.MANUAL_REVIEW_REQUIRED,
                staging_record_id="staging-001",
                source_field="Код",
                target_field="one_c_code",
                message="Missing critical code",
            ),
        )

        assert get_mapping_issue(session, issue.id) is not None
        assert mapping_completion_is_blocked(session, "staging-001") is True

        update_mapping_issue_status(session, issue.id, MappingIssueStatus.RESOLVED)

        assert mapping_completion_is_blocked(session, "staging-001") is False


def test_unmapped_required_type_mismatch_and_default_decision_persist() -> None:
    with create_test_session() as session:
        unmapped = UnmappedFieldRecordStorage(
            staging_record_id="staging-001",
            field_name="Unknown",
            raw_value="value",
        )
        required = RequiredFieldMissingIssueStorage(
            staging_record_id="staging-001",
            source_field="Код",
            target_field="one_c_code",
            critical=True,
        )
        mismatch = FieldTypeMismatchIssueStorage(
            staging_record_id="staging-001",
            field_name="Amount",
            expected_type="number",
            actual_type="string",
            raw_value="not-a-number",
        )
        decision = DefaultValueDecisionStorage(
            staging_record_id="staging-001",
            target_field="currency",
            default_category="configured_default",
            default_value="UAH",
            approved=False,
        )

        session.add(unmapped)
        session.add(required)
        session.add(mismatch)
        session.add(decision)
        session.commit()

        assert unmapped.id
        assert required.critical is True
        assert mismatch.actual_type == "string"
        assert decision.default_value == "UAH"