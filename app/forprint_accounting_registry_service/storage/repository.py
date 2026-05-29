"""
Small storage repository helpers.

Purpose:
    Minimal repository helpers for v0.2 tests and local storage foundation.

Boundary:
    This is not a full domain repository layer yet.
"""

from typing import TypeVar

from sqlmodel import Session, SQLModel

StorageModelT = TypeVar("StorageModelT", bound=SQLModel)


def save_record(session: Session, record: StorageModelT) -> StorageModelT:
    """Save one SQLModel record and return refreshed instance."""
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


def get_record_by_id(
    session: Session,
    model_type: type[StorageModelT],
    record_id: str,
) -> StorageModelT | None:
    """Get one record by primary key."""
    return session.get(model_type, record_id)