from pathlib import Path

import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSourceSafetyError,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationError,
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCTestDatabaseManifest,
    OneCTestDatabaseSource,
    calculate_file_checksum,
    create_working_copy_manifest,
    register_sanitized_test_database_source,
)


def test_sanitized_test_db_source_can_be_registered(tmp_path: Path) -> None:
    source_path = tmp_path / "sanitized.1CD"
    source_path.write_text("synthetic sanitized db", encoding="utf-8")

    source = register_sanitized_test_database_source(
        source_path=source_path,
        source_id="sanitized-db",
    )

    manifest = OneCTestDatabaseManifest()
    manifest.register(source)

    assert manifest.get_source("sanitized-db") is not None
    assert source.checksum is not None


def test_unsanitized_source_is_rejected_for_processing() -> None:
    metadata = OneCSanitizationMetadata(
        status=OneCSanitizationStatus.NOT_SANITIZED,
        real_1c_data=True,
        sanitized=False,
    )

    with pytest.raises(OneCSanitizationError):
        assert_source_is_sanitized(metadata)


def test_production_source_is_rejected() -> None:
    source = OneCTestDatabaseSource(
        source_id="prod",
        source_path="/production/one_c.1CD",
        is_sanitized=True,
        production_allowed=True,
    )

    manifest = OneCTestDatabaseManifest()

    with pytest.raises(OneCSourceSafetyError):
        manifest.register(source)


def test_non_disposable_source_rejects_destructive_write_mode() -> None:
    source = OneCTestDatabaseSource(
        source_id="unsafe-write",
        source_path="local_sandbox/one_c_databases/test.1CD",
        is_sanitized=True,
        is_disposable=False,
        writes_allowed=True,
        destructive_write_allowed=True,
        metadata={"sandbox_mode": True},
    )

    manifest = OneCTestDatabaseManifest()

    with pytest.raises(OneCSourceSafetyError):
        manifest.register(source)


def test_source_checksum_is_recorded_if_sample_file_exists(tmp_path: Path) -> None:
    source_path = tmp_path / "sample.1CD"
    source_path.write_text("sample", encoding="utf-8")

    checksum = calculate_file_checksum(source_path)

    assert checksum.value
    assert checksum.file_path == str(source_path)


def test_working_copy_manifest_references_original_but_is_separate(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    working = tmp_path / "working_copies" / "copy.1CD"
    original.write_text("original", encoding="utf-8")

    source = register_sanitized_test_database_source(
        source_path=original,
        source_id="source-001",
    )
    manifest = create_working_copy_manifest(source, working, copy_file=True)

    assert manifest.original_source_path != manifest.working_copy_path
    assert working.exists()
    assert original.read_text(encoding="utf-8") == "original"