"""
Mapping issue registry service.

Purpose:
    Convert mapping policy issues into persisted storage diagnostics.
"""

from sqlmodel import Session

from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingResult,
    MappingIssueType,
)
from forprint_accounting_registry_service.repositories.mapping_issues import save_mapping_issue
from forprint_accounting_registry_service.storage.mapping_models import (
    MappingIssueStatus,
    MappingIssueStorage,
    UnmappedFieldRecordStorage,
)


def status_from_issue_type(issue_type: MappingIssueType) -> MappingIssueStatus:
    """Map policy issue type to storage status."""
    if issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED:
        return MappingIssueStatus.MANUAL_REVIEW_REQUIRED

    if issue_type == MappingIssueType.BLOCKED_UNTIL_MAPPED:
        return MappingIssueStatus.BLOCKED_UNTIL_MAPPED

    return MappingIssueStatus.NEW


def persist_mapping_result(
    session: Session,
    result: FieldMappingResult,
    staging_record_id: str | None = None,
    raw_snapshot_id: str | None = None,
) -> list[MappingIssueStorage]:
    """Persist mapping issues and unmapped field records."""
    stored_issues: list[MappingIssueStorage] = []

    for issue in result.issues:
        stored_issue = save_mapping_issue(
            session,
            MappingIssueStorage(
                issue_type=issue.issue_type,
                status=status_from_issue_type(issue.issue_type),
                severity=issue.severity,
                raw_snapshot_id=raw_snapshot_id,
                staging_record_id=staging_record_id,
                source_field=issue.source_field,
                target_field=issue.target_field,
                message=issue.message,
            ),
        )
        stored_issues.append(stored_issue)

    for unmapped_field in result.unmapped_fields:
        session.add(
            UnmappedFieldRecordStorage(
                staging_record_id=staging_record_id,
                field_name=unmapped_field.field_name,
                raw_value=unmapped_field.value,
            )
        )

    session.commit()
    return stored_issues