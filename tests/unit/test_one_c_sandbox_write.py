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


def build_write_plan(dry_run: bool = True) -> OneCWritePlan:
    return OneCWritePlan(
        plan_id="write-plan-001",
        dry_run=dry_run,
        operations=[
            OneCWriteOperation(
                operation_type=OneCWriteOperationType.UPSERT_DIRECTORY_ITEM,
                target_name="Counterparties",
                payload={"Code": "000001"},
            )
        ],
    )


def test_write_experiment_is_blocked_by_default() -> None:
    source = OneCSandboxSource(
        source_id="sandbox",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(),
        allow_destructive_flag=False,
    )

    assert result.applied is False
    assert result.safety_checks[0].passed is False


def test_write_experiment_requires_disposable_source() -> None:
    source = OneCSandboxSource(
        source_id="readonly",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/readonly.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        disposable=False,
        write_tests_allowed=False,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(),
        allow_destructive_flag=True,
    )

    assert result.applied is False
    assert result.result_metadata["blocked"] is True


def test_write_experiment_dry_run_does_not_mutate_source() -> None:
    source = OneCSandboxSource(
        source_id="disposable",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(dry_run=True),
        allow_destructive_flag=True,
    )

    assert result.applied is False
    assert result.result_metadata["dry_run"] is True


def test_write_experiment_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="production",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
    )

    assert result.applied is False