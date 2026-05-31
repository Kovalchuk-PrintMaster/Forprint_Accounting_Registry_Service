import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
    ensure_destructive_test_allowed,
    ensure_not_production_source,
)


def test_sandbox_source_can_be_registered_as_non_production() -> None:
    source = OneCSandboxSource(
        source_id="fixture-001",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/example.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )

    assert source.production_allowed is False
    assert source.sanitized is True


def test_destructive_test_requires_disposable_source_and_flag() -> None:
    source = OneCSandboxSource(
        source_id="sandbox-001",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    ensure_destructive_test_allowed(source, allow_destructive_flag=True)


def test_destructive_test_is_blocked_without_flag() -> None:
    source = OneCSandboxSource(
        source_id="sandbox-001",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        ensure_destructive_test_allowed(source, allow_destructive_flag=False)


def test_production_source_is_rejected() -> None:
    source = OneCSandboxSource(
        source_id="production-like",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        ensure_not_production_source(source)