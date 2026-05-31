import pytest
from forprint_accounting_registry_service.one_c_io.direct_db import (
    OneCSandboxDirectDbInspector,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
)


def build_readonly_source() -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="sandbox-fixture",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/sanitized.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )


def test_direct_db_inspector_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="production",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        OneCSandboxDirectDbInspector(source)


def test_schema_discovery_report_can_be_created_from_fixture() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    report = inspector.discover_schema_from_fixture(
        {
            "Counterparties": [
                {"Code": "000001", "Name": "ТОВ Приклад"},
            ]
        }
    )

    assert report.source_id == "sandbox-fixture"
    assert report.canonical_truth is False
    assert report.tables[0].table_name == "Counterparties"
    assert report.tables[0].records_count == 1


def test_raw_extract_batch_can_be_created_from_fixture() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    batch = inspector.extract_raw_batch_from_fixture(
        table_name="Counterparties",
        records=[{"Code": "000001", "Unknown": "preserve"}],
    )

    assert batch.table_name == "Counterparties"
    assert batch.records[0]["Unknown"] == "preserve"


def test_readonly_inspector_has_no_write_method() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    assert not hasattr(inspector, "write")
    assert not hasattr(inspector, "post")