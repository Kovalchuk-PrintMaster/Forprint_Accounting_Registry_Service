"""
OneC source manifest.

Purpose:
    Serialize/read local sandbox source declarations.
"""

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
)


class OneCSourceManifest(BaseModel):
    """Manifest of local/test 1C-like sources."""

    fixture_status: str = "example"
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False
    sources: list[OneCSandboxSource] = Field(default_factory=list)

    def add_source(self, source: OneCSandboxSource) -> None:
        """Add sandbox source to manifest."""
        self.sources.append(source)

    def get_source(self, source_id: str) -> OneCSandboxSource | None:
        """Get sandbox source by ID."""
        for source in self.sources:
            if source.source_id == source_id:
                return source
        return None

    def to_json_string(self) -> str:
        """Serialize manifest to JSON."""
        return self.model_dump_json(indent=2)

    @classmethod
    def from_json_string(cls, value: str) -> "OneCSourceManifest":
        """Deserialize manifest from JSON."""
        return cls.model_validate_json(value)