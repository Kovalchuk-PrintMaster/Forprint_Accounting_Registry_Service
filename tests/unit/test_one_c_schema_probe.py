import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.schema_probe import (
    probe_sanitized_source_schema,
)


def test_direct_discovery_handles_synthetic_fixture() -> None:
    source = OneCSandboxSource(
        source_id="fixture",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/exports/counterparties.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )

    result = probe_sanitized_source_schema(
        source,
        fixture_tables={"Counterparties": [{"Code": "000001", "Unknown": "preserve"}]},
    )

    assert result.supported is True
    assert result.report is not None
    assert result.report.canonical_truth is False


def test_direct_discovery_handles_unsupported_file_gracefully() -> None:
    source = OneCSandboxSource(
        source_id="unsupported",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/missing.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_READONLY,
    )

    result = probe_sanitized_source_schema(source)

    assert result.supported is False
    assert result.status == "unsupported_source"
    assert result.diagnostics


def test_direct_discovery_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="prod",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        probe_sanitized_source_schema(source)