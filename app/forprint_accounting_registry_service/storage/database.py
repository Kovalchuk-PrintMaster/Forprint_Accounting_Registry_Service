"""
Storage database helpers.

Purpose:
    Lightweight local SQLModel/SQLite foundation for Accounting Registry v0.2.

Boundary:
    This is not a production DB strategy.
    This is a small testable storage foundation for accounting-only and 1C-boundary data.
"""

from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

from forprint_accounting_registry_service.storage import models as _storage_models  # noqa: F401

DEFAULT_SQLITE_PATH = Path("data/accounting_registry.sqlite3")


def build_sqlite_url(db_path: Path) -> str:
    """Build SQLite URL for a filesystem database."""
    return f"sqlite:///{db_path}"


def create_sqlite_engine(db_path: Path | str = ":memory:"):
    """Create SQLite engine for test/local usage."""
    if str(db_path) == ":memory:":
        return create_engine("sqlite:///:memory:")

    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(build_sqlite_url(path))


def init_storage(engine) -> None:
    """Create all Accounting Registry storage tables."""
    SQLModel.metadata.create_all(engine)


def create_session(engine) -> Session:
    """Create SQLModel session."""
    return Session(engine)