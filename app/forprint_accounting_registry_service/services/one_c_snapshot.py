"""
1C snapshot service.

Purpose:
    Базова логіка для роботи зі snapshot-файлами з 1С.

Important:
    Raw snapshot не редагується.
    Нормалізація виконується пізніше через staging/projection layer.
"""

from pathlib import Path

ALLOWED_SNAPSHOT_EXTENSIONS = {".csv", ".xlsx", ".xml", ".json"}


def validate_snapshot_file(path: Path) -> bool:
    """Перевіряє, чи snapshot-файл існує і має дозволене розширення."""
    return path.exists() and path.is_file() and path.suffix.lower() in ALLOWED_SNAPSHOT_EXTENSIONS


def list_snapshot_files(raw_dir: Path) -> list[Path]:
    """Повертає список snapshot-файлів у raw-директорії."""
    if not raw_dir.exists():
        return []

    return [
        item
        for item in raw_dir.iterdir()
        if item.is_file() and item.suffix.lower() in ALLOWED_SNAPSHOT_EXTENSIONS
    ]