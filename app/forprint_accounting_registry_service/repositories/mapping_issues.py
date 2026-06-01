"""
Mapping issue repository.

Purpose:
    Small repository for mapping issue persistence tests and local pipeline.

Boundary:
    Mapping issues are accounting import diagnostics only.
"""

from datetime import UTC, datetime

from sqlmodel import Session, select

from forprint_accounting_registry_service.storage.mapping_models import (
    MappingIssueStatus,
    MappingIssueStorage,
)

BLOCKING_STATUSES = {
    MappingIssueStatus.MANUAL_REVIEW_REQUIRED,
    MappingIssueStatus.BLOCKED_UNTIL_MAPPED,
}


def save_mapping_issue(session: Session, issue: MappingIssueStorage) -> MappingIssueStorage:
    """Persist mapping issue."""
    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue


def get_mapping_issue(session: Session, issue_id: str) -> MappingIssueStorage | None:
    """Get mapping issue by ID."""
    return session.get(MappingIssueStorage, issue_id)


def update_mapping_issue_status(
    session: Session,
    issue_id: str,
    status: MappingIssueStatus,
) -> MappingIssueStorage:
    """Update issue status."""
    issue = session.get(MappingIssueStorage, issue_id)
    if issue is None:
        raise KeyError(f"Mapping issue not found: {issue_id}")

    issue.status = status
    if status in {MappingIssueStatus.RESOLVED, MappingIssueStatus.IGNORED}:
        issue.resolved_at = datetime.now(UTC)

    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue


def mapping_completion_is_blocked(session: Session, staging_record_id: str) -> bool:
    """Return True when unresolved blocking issues exist for staging record."""
    statement = select(MappingIssueStorage).where(
        MappingIssueStorage.staging_record_id == staging_record_id
    )
    issues = session.exec(statement).all()
    return any(issue.status in BLOCKING_STATUSES for issue in issues)