from pathlib import Path

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.sandbox_write import (
    OneCWriteOperation,
    OneCWriteOperationType,
    OneCWritePlan,
    run_sandbox_write_experiment,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCTestDatabaseSource,
    create_working_copy_manifest,
)


def build_source() -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="disposable",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
        production_allowed=False,
    )


def build_write_plan(dry_run: bool) -> OneCWritePlan:
    return OneCWritePlan(
        plan_id="write-plan",
        dry_run=dry_run,
        operations=[
            OneCWriteOperation(
                operation_type=OneCWriteOperationType.UPSERT_DIRECTORY_ITEM,
                target_name="Counterparties",
                payload={"Code": "000001"},
            )
        ],
    )


def test_write_requires_working_copy_for_non_dry_run() -> None:
    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=None,
    )

    assert result.applied is False
    assert result.result_metadata["missing_working_copy"] is True


def test_write_refuses_original_source_as_working_copy(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    original.write_text("original", encoding="utf-8")

    db_source = OneCTestDatabaseSource(
        source_id="source",
        source_path=str(original),
        is_sanitized=True,
    )
    working_copy = create_working_copy_manifest(
        db_source,
        working_copy_path=original,
        copy_file=False,
    )

    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=working_copy,
    )

    assert result.applied is False
    assert result.result_metadata["same_original_and_working_copy"] is True


def test_original_source_checksum_remains_unchanged(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    working = tmp_path / "working" / "copy.1CD"
    original.write_text("original", encoding="utf-8")

    db_source = OneCTestDatabaseSource(
        source_id="source",
        source_path=str(original),
        is_sanitized=True,
    )
    working_copy = create_working_copy_manifest(
        db_source,
        working_copy_path=working,
        copy_file=True,
    )

    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=working_copy,
    )

    assert result.applied is True
    assert result.result_metadata["original_source_unchanged"] is True