from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_detection import detect_export_format
from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
    parsed_export_batch_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_json_export_fixture_parses() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.json")

    assert result.batch is not None
    assert result.batch.sanitized is True
    assert result.batch.production_allowed is False
    assert result.batch.rows[0].raw_values["Код"] == "000001"


def test_csv_export_fixture_parses() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.csv")

    assert result.batch is not None
    assert result.batch.export_format == OneCExportFormat.CSV
    assert result.batch.rows[0].raw_values["НевідомеПоле"] == "preserve-me"


def test_xml_export_fixture_parses_or_returns_supported_batch() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.xml")

    assert result.batch is not None
    assert result.batch.rows[0].raw_values["Код"] == "000001"


def test_unknown_format_returns_explicit_unsupported_result(tmp_path: Path) -> None:
    path = tmp_path / "export.bin"
    path.write_text("unknown", encoding="utf-8")

    assert detect_export_format(path) == OneCExportFormat.UNKNOWN_RAW_TEXT

    result = parse_one_c_export_file(path)

    assert result.supported is False
    assert result.batch is None


def test_parsed_export_maps_to_staging_records() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.json")
    assert result.batch is not None

    records = parsed_export_batch_to_staging_records(result.batch, snapshot_id="snapshot-001")

    assert records[0].record_type.startswith("parsed_export:")
    assert records[0].raw_payload["row"]["НевідомеПоле"] == "preserve-me"