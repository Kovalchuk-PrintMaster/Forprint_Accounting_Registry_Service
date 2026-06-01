"""
OneC sanitized test database registry.

Purpose:
    Register local sanitized/disposable test DB copies safely.

Boundary:
    Real or copied DB files must stay in gitignored local_sandbox paths.
    Original source must never be mutated by tests.
"""

import hashlib
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSourceKind,
    OneCSourceSafetyError,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


def utc_now() -> datetime:
    """Return timezone-aware UTC datetime."""
    return datetime.now(UTC)


class OneCSourceChecksum(BaseModel):
    """Checksum metadata for local test source files."""

    algorithm: str = "sha256"
    value: str
    file_path: str


class OneCTestDatabaseSource(BaseModel):
    """Sanitized local/test 1C database source declaration."""

    source_id: str = Field(default_factory=lambda: str(uuid4()))
    source_kind: OneCSourceKind = OneCSourceKind.FILE_DATABASE_COPY
    one_c_version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION
    source_path: str

    is_sanitized: bool = True
    is_disposable: bool = False
    production_allowed: bool = False
    read_only: bool = True
    writes_allowed: bool = False
    destructive_write_allowed: bool = False

    checksum: OneCSourceChecksum | None = None
    created_at: datetime = Field(default_factory=utc_now)
    notes: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class OneCTestDatabaseManifest(BaseModel):
    """Manifest of registered sanitized local test DB sources."""

    fixture_status: str = "local_manifest"
    production_allowed: bool = False
    sources: list[OneCTestDatabaseSource] = Field(default_factory=list)

    def register(self, source: OneCTestDatabaseSource) -> None:
        """Register source after safety validation."""
        validate_test_database_source(source)
        self.sources.append(source)

    def get_source(self, source_id: str) -> OneCTestDatabaseSource | None:
        """Find source by ID."""
        for source in self.sources:
            if source.source_id == source_id:
                return source
        return None


class OneCWorkingCopyManifest(BaseModel):
    """Working copy declaration separate from original source."""

    working_copy_id: str = Field(default_factory=lambda: str(uuid4()))
    original_source_id: str
    original_source_path: str
    working_copy_path: str
    original_checksum: OneCSourceChecksum | None = None
    working_copy_checksum: OneCSourceChecksum | None = None
    disposable: bool = True
    created_at: datetime = Field(default_factory=utc_now)


def calculate_file_checksum(path: Path, algorithm: str = "sha256") -> OneCSourceChecksum:
    """Calculate file checksum if file exists."""
    digest = hashlib.new(algorithm)

    with path.open("rb") as file_obj:
        for chunk in iter(lambda: file_obj.read(1024 * 1024), b""):
            digest.update(chunk)

    return OneCSourceChecksum(
        algorithm=algorithm,
        value=digest.hexdigest(),
        file_path=str(path),
    )


def validate_test_database_source(source: OneCTestDatabaseSource) -> None:
    """Validate sanitized test DB source safety."""
    if source.production_allowed:
        raise OneCSourceSafetyError("Production source is forbidden.")

    metadata = OneCSanitizationMetadata(
        status=(OneCSanitizationStatus.SANITIZED 
                if source.is_sanitized 
                else OneCSanitizationStatus.NOT_SANITIZED
        ),
        real_1c_data=True,
        sanitized=source.is_sanitized,
        production_allowed=source.production_allowed,
    )
    assert_source_is_sanitized(metadata)

    if source.writes_allowed or source.destructive_write_allowed:
        if not source.is_disposable:
            raise OneCSourceSafetyError(
                "Write-enabled test DB source must be disposable."
            )

        if not source.metadata.get("sandbox_mode", False):
            raise OneCSourceSafetyError(
                "Write-enabled test DB source requires sandbox_mode metadata."
            )

    if not source.read_only and not source.is_disposable:
        raise OneCSourceSafetyError("Non-read-only source must be disposable.")


def register_sanitized_test_database_source(
    source_path: Path,
    source_id: str,
    is_disposable: bool = False,
    sandbox_mode: bool = False,
) -> OneCTestDatabaseSource:
    """Register sanitized test DB source and calculate checksum if file exists."""
    checksum = calculate_file_checksum(source_path) if source_path.exists() else None

    source = OneCTestDatabaseSource(
        source_id=source_id,
        source_path=str(source_path),
        is_sanitized=True,
        is_disposable=is_disposable,
        checksum=checksum,
        metadata={"sandbox_mode": sandbox_mode},
    )
    validate_test_database_source(source)
    return source


def create_working_copy_manifest(
    source: OneCTestDatabaseSource,
    working_copy_path: Path,
    copy_file: bool = False,
) -> OneCWorkingCopyManifest:
    """
    Declare working copy separate from original source.

    If copy_file=True and original exists, copy source to working path.
    Tests should use small synthetic files only.
    """
    original_path = Path(source.source_path)

    if copy_file and original_path.exists():
        working_copy_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original_path, working_copy_path)

    original_checksum = (
        calculate_file_checksum(original_path) if original_path.exists() else source.checksum
    )
    working_checksum = (
        calculate_file_checksum(working_copy_path) if working_copy_path.exists() else None
    )

    return OneCWorkingCopyManifest(
        original_source_id=source.source_id,
        original_source_path=source.source_path,
        working_copy_path=str(working_copy_path),
        original_checksum=original_checksum,
        working_copy_checksum=working_checksum,
        disposable=True,
    )