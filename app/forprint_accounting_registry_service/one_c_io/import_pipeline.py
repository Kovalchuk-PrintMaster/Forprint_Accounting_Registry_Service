"""
OneC sandbox import pipeline.

Purpose:
    Offline pipeline from sanitized export/test source to raw snapshot, staging,
    mapping issues, and import summary.

Boundary:
    No live 1C connection.
    No production sync.
    No foreign-domain ownership.
"""

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from pydantic import BaseModel, Field
from sqlmodel import Session

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
    parsed_export_batch_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.services.mapping_issue_registry import (
    persist_mapping_result,
)
from forprint_accounting_registry_service.storage.models import OneCRawSnapshot


class OneCImportPipelineStatus(str):
    """Pipeline status constants."""

    COMPLETED = "completed"
    COMPLETED_WITH_WARNINGS = "completed_with_warnings"
    BLOCKED_BY_MAPPING_ISSUES = "blocked_by_mapping_issues"
    UNSUPPORTED_SOURCE = "unsupported_source"
    FAILED = "failed"


class OneCImportPipelineResult(BaseModel):
    """Import pipeline result summary."""

    pipeline_run_id: str = Field(default_factory=lambda: str(uuid4()))
    source_id: str
    source_kind: str
    raw_snapshot_count: int = 0
    staging_record_count: int = 0
    mapping_issue_count: int = 0
    blocked_record_count: int = 0
    manual_review_required_count: int = 0
    status: str
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class OneCSandboxImportPipeline:
    """Offline sanitized source import pipeline."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def run_file_export_import(
        self,
        source: OneCSandboxSource,
        export_path: Path,
        mapping_definitions: list[FieldMappingDefinition],
        target_kind: str = "generic_accounting_table_export",
    ) -> OneCImportPipelineResult:
        """Run sanitized export import into raw snapshot/staging/mapping diagnostics."""
        try:
            ensure_not_production_source(source)
            assert_source_is_sanitized(
                OneCSanitizationMetadata(
                    status=(OneCSanitizationStatus.SANITIZED 
                            if source.sanitized 
                            else OneCSanitizationStatus.NOT_SANITIZED
                    ),
                    real_1c_data=True,
                    sanitized=source.sanitized,
                    production_allowed=source.production_allowed,
                )
            )
        except Exception as exc:  # noqa: BLE001
            return OneCImportPipelineResult(
                source_id=source.source_id,
                source_kind=source.source_kind,
                status=OneCImportPipelineStatus.FAILED,
                errors=[str(exc)],
            )

        parser_result = parse_one_c_export_file(export_path, target_kind=target_kind)

        if not parser_result.supported or parser_result.batch is None:
            return OneCImportPipelineResult(
                source_id=source.source_id,
                source_kind=source.source_kind,
                status=OneCImportPipelineStatus.UNSUPPORTED_SOURCE,
                errors=[issue.message for issue in parser_result.issues],
            )

        snapshot = OneCRawSnapshot(
            snapshot_type=f"file_export:{target_kind}",
            source_name=source.source_id,
            file_name=export_path.name,
            file_path=str(export_path),
            status="stored",
            raw_metadata={
                "source_kind": source.source_kind,
                "export_format": parser_result.batch.export_format,
                "sanitized": parser_result.batch.sanitized,
                "production_allowed": parser_result.batch.production_allowed,
            },
        )
        self.session.add(snapshot)
        self.session.commit()
        self.session.refresh(snapshot)

        staging_records = parsed_export_batch_to_staging_records(
            parser_result.batch,
            snapshot_id=snapshot.id,
        )

        mapping_issue_count = 0
        manual_review_count = 0
        blocked_count = 0

        for staging_record, parsed_row in zip(
                                            staging_records, 
                                            parser_result.batch.rows, 
                                            strict=False
        ):
            mapping_result = apply_mapping_policy(
                source_payload=parsed_row.raw_values,
                definitions=mapping_definitions,
            )
            staging_record.normalized_payload = mapping_result.mapped_payload
            self.session.add(staging_record)
            self.session.commit()
            self.session.refresh(staging_record)

            stored_issues = persist_mapping_result(
                self.session,
                mapping_result,
                staging_record_id=staging_record.id,
                raw_snapshot_id=snapshot.id,
            )
            mapping_issue_count += len(stored_issues)
            manual_review_count += sum(
                1 for issue in stored_issues if issue.status == "manual_review_required"
            )
            blocking_statuses = {
                "manual_review_required",
                "blocked_until_mapped",
            }
            blocked_count += sum(
                1 for issue in stored_issues if issue.status in blocking_statuses
            )

        status = OneCImportPipelineStatus.COMPLETED
        if mapping_issue_count:
            status = OneCImportPipelineStatus.COMPLETED_WITH_WARNINGS
        if blocked_count:
            status = OneCImportPipelineStatus.BLOCKED_BY_MAPPING_ISSUES

        return OneCImportPipelineResult(
            source_id=source.source_id,
            source_kind=source.source_kind,
            raw_snapshot_count=1,
            staging_record_count=len(staging_records),
            mapping_issue_count=mapping_issue_count,
            blocked_record_count=blocked_count,
            manual_review_required_count=manual_review_count,
            status=status,
            warnings=[issue.message for issue in parser_result.issues],
        )