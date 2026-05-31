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
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceSafetyError,
    ensure_destructive_test_allowed,
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
) -> OneCWriteExperimentResult:
    """
    Run sandbox write experiment boundary.

    This does not mutate real source data.
    It returns a result record only.
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

    safety_checks.append(
        OneCWriteSafetyCheck(
            passed=True,
            message="Disposable sandbox write experiment allowed by explicit flag.",
        )
    )
    return OneCWriteExperimentResult(
        experiment_id=f"experiment-{plan.plan_id}",
        plan_id=plan.plan_id,
        applied=True,
        safety_checks=safety_checks,
        result_metadata={"disposable_source": True},
    )