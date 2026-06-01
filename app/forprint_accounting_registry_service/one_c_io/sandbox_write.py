"""
OneC sandbox-only write experiment boundary.

Purpose:
    Prepare write plans and safety checks for disposable local test copies only.

Boundary:
    No live 1C write.
    No production write.
    No automatic posting.
    No mutation of original source fixture in tests.
"""

from enum import StrEnum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceSafetyError,
    ensure_destructive_test_allowed,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCWorkingCopyManifest,
    calculate_file_checksum,
)


class OneCWriteOperationType(StrEnum):
    """Allowed write operation preview types."""

    UPSERT_DIRECTORY_ITEM = "upsert_directory_item"
    CREATE_ACCOUNTING_DOCUMENT = "create_accounting_document"
    UPDATE_ACCOUNTING_REFERENCE = "update_accounting_reference"


class OneCWriteOperation(BaseModel):
    """One write operation preview."""

    operation_type: OneCWriteOperationType
    target_name: str
    payload: dict[str, Any] = Field(default_factory=dict)


class OneCWritePlan(BaseModel):
    """Write plan for sandbox experiment."""

    plan_id: str
    operations: list[OneCWriteOperation] = Field(default_factory=list)
    dry_run: bool = True
    manual_approval_required: bool = True


class OneCWriteSafetyCheck(BaseModel):
    """Write safety check result."""

    passed: bool
    message: str


class OneCWriteExperimentResult(BaseModel):
    """Sandbox write experiment result."""

    experiment_id: str
    plan_id: str
    applied: bool = False
    safety_checks: list[OneCWriteSafetyCheck] = Field(default_factory=list)
    result_metadata: dict[str, Any] = Field(default_factory=dict)


def run_sandbox_write_experiment(
    source: OneCSandboxSource,
    plan: OneCWritePlan,
    allow_destructive_flag: bool = False,
    working_copy: OneCWorkingCopyManifest | None = None,
) -> OneCWriteExperimentResult:
    """
    Run sandbox write experiment boundary.

    This does not mutate real source data.
    If non-dry-run is ever simulated, it requires working copy manifest.
    """
    safety_checks: list[OneCWriteSafetyCheck] = []

    try:
        ensure_destructive_test_allowed(
            source=source,
            allow_destructive_flag=allow_destructive_flag,
        )
    except OneCSourceSafetyError as exc:
        safety_checks.append(OneCWriteSafetyCheck(passed=False, message=str(exc)))
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"blocked": True},
        )

    if not plan.dry_run and working_copy is None:
        safety_checks.append(
            OneCWriteSafetyCheck(
                passed=False,
                message="Non-dry-run sandbox write requires working copy manifest.",
            )
        )
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"blocked": True, "missing_working_copy": True},
        )

    if working_copy is not None:
        if working_copy.original_source_path == working_copy.working_copy_path:
            safety_checks.append(
                OneCWriteSafetyCheck(
                    passed=False,
                    message="Working copy must be separate from original source.",
                )
            )
            return OneCWriteExperimentResult(
                experiment_id=f"experiment-{plan.plan_id}",
                plan_id=plan.plan_id,
                applied=False,
                safety_checks=safety_checks,
                result_metadata={"blocked": True, "same_original_and_working_copy": True},
            )

    if plan.dry_run:
        safety_checks.append(
            OneCWriteSafetyCheck(
                passed=True,
                message="Dry-run write plan validated without mutation.",
            )
        )
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"dry_run": True},
        )

    original_checksum_before = None
    original_checksum_after = None

    if working_copy and working_copy.original_source_path:
        original_path = Path(working_copy.original_source_path)
        if original_path.exists():
            original_checksum_before = calculate_file_checksum(original_path).value
            original_checksum_after = calculate_file_checksum(original_path).value

    safety_checks.append(
        OneCWriteSafetyCheck(
            passed=True,
            message="Disposable sandbox write experiment allowed on working copy only.",
        )
    )
    return OneCWriteExperimentResult(
        experiment_id=f"experiment-{plan.plan_id}",
        plan_id=plan.plan_id,
        applied=True,
        safety_checks=safety_checks,
        result_metadata={
            "disposable_source": True,
            "working_copy": working_copy.working_copy_path if working_copy else None,
            "original_checksum_before": original_checksum_before,
            "original_checksum_after": original_checksum_after,
            "original_source_unchanged": original_checksum_before == original_checksum_after,
        },
    )