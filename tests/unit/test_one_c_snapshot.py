from pathlib import Path

from forprint_accounting_registry_service.services.one_c_snapshot import (
    ALLOWED_SNAPSHOT_EXTENSIONS,
    list_snapshot_files,
    validate_snapshot_file,
)


def test_validate_snapshot_file_rejects_missing_file() -> None:
    assert validate_snapshot_file(Path("/tmp/not-existing-file.csv")) is False


def test_validate_snapshot_file_accepts_allowed_extensions(tmp_path: Path) -> None:
    allowed_files = [
        tmp_path / "counterparties.csv",
        tmp_path / "nomenclature.xlsx",
        tmp_path / "snapshot.xml",
        tmp_path / "snapshot.json",
    ]

    for path in allowed_files:
        path.write_text("test", encoding="utf-8")
        assert validate_snapshot_file(path) is True


def test_validate_snapshot_file_rejects_disallowed_extension(tmp_path: Path) -> None:
    path = tmp_path / "readme.txt"
    path.write_text("ignore", encoding="utf-8")

    assert validate_snapshot_file(path) is False


def test_list_snapshot_files_returns_only_allowed_extensions(tmp_path: Path) -> None:
    valid_csv = tmp_path / "counterparties.csv"
    valid_json = tmp_path / "snapshot.json"
    invalid_txt = tmp_path / "readme.txt"

    valid_csv.write_text("name\nТОВ Тест\n", encoding="utf-8")
    valid_json.write_text("{}", encoding="utf-8")
    invalid_txt.write_text("ignore", encoding="utf-8")

    result = list_snapshot_files(tmp_path)

    assert valid_csv in result
    assert valid_json in result
    assert invalid_txt not in result


def test_list_snapshot_files_returns_empty_list_for_missing_directory(tmp_path: Path) -> None:
    missing_dir = tmp_path / "missing"

    assert list_snapshot_files(missing_dir) == []


def test_allowed_snapshot_extensions_are_controlled() -> None:
    assert ALLOWED_SNAPSHOT_EXTENSIONS == {".csv", ".xlsx", ".xml", ".json"}