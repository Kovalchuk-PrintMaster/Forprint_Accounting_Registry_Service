# ForPrint Accounting Registry Service â€” L0 Comprehensive Semantic Audit v0.1

## Result

`PASS_COMPREHENSIVE_AUDIT_WITH_RECONCILIATION_REQUIRED`

- source HEAD: `7315a7a6bd0a8f4e08385bdbd676edaf8aa25bb5`
- analysis layer: `L0 â€” Baseline Reconstruction & Knowledge Stabilization`
- action now: `none`
- implementation / roadmap / machine / execution authority: `false`

## Executive conclusion

The module is a coherent, safety-conscious **offline 1C sandbox / import / staging / mapping foundation**. Its v0.5 baseline is real: structured export parsing, local SQLModel persistence, mapping diagnostics, fixture-driven directory/report extraction and strong no-production-write guards exist.

It is **not yet** the broader operational/commercial accounting registry described by current Blueprint Human Intent and the portfolio roadmap. Accounts receivable workflow, full invoice/payment lifecycle, supplier document OCR/goods receipt, bank/payment reconciliation, mature settlements, live 1C integration and cross-module runtime integration remain future work.

The correct L0 outcome is therefore **reconciliation**, not implementation.

## Current lineage

| Generation | Commit | Classification |
|---|---|---|
| `v0_1_boundary_correction_baseline` | `2e98a3a` | `CURRENT_LINEAGE_WITH_SEMANTIC_RESIDUE` |
| `v0_2_storage_foundation` | `ec46ef1` | `CURRENT_IMPLEMENTED_FOUNDATION` |
| `v0_3_one_c_io_adapter_strategy` | `009dfef` | `CURRENT_IMPLEMENTED_DISCOVERY_FOUNDATION` |
| `v0_4_sandbox_io_reports_directories` | `ab48ef1` | `CURRENT_SANDBOX_FIXTURE_CAPABILITY` |
| `v0_5_sanitized_import_pipeline` | `95d4a55` | `CURRENT_ACCEPTED_LOCAL_BASELINE` |
| `governance_alignment_v0_1` | `7315a7a` | `CURRENT_GOVERNANCE_OVERLAY` |

The six commits form one understandable evolutionary line. There is no evidence of
multiple competing runtime implementations, but early semantic objects remain in
the current tree and require ownership/currentness adjudication.

## Implemented capability baseline

- **CAP-01 â€” IMPLEMENTED_LOCAL**: minimal FastAPI service health surface.
- **CAP-02 â€” IMPLEMENTED_LOCAL**: SQLModel/SQLite local accounting and 1C-boundary storage foundation.
- **CAP-03 â€” IMPLEMENTED_LOCAL**: sanitized file export parsing for JSON/CSV/XML/YAML/TXT tabular data.
- **CAP-04 â€” IMPLEMENTED_LOCAL**: raw-snapshot metadata to staging conversion.
- **CAP-05 â€” IMPLEMENTED_LOCAL**: explicit mapping/default policy with unknown-field preservation and manual-review issues.
- **CAP-06 â€” IMPLEMENTED_LOCAL**: persisted import/mapping diagnostics.
- **CAP-07 â€” IMPLEMENTED_FIXTURE_SANDBOX**: directory and report snapshot abstractions mapped into staging.
- **CAP-08 â€” IMPLEMENTED_POLICY_AND_SIMULATION**: 1C adapter/version/channel policy and placeholder adapter registry.
- **CAP-09 â€” IMPLEMENTED_FIXTURE_SANDBOX**: fixture-driven schema discovery and raw extraction abstractions.
- **CAP-10 â€” IMPLEMENTED_POLICY_AND_SIMULATION**: dry-run export package and disposable working-copy write safety model.
- **CAP-11 â€” IMPLEMENTED_LOCAL**: developer smoke CLIs for parse/discovery/import pipeline.
- **CAP-12 â€” IMPLEMENTED_LOCAL_HISTORICAL_CHECK_EVIDENCE**: boundary-focused lint/test/check report runner.

## Explicitly not implemented

- production invoice lifecycle
- production payment lifecycle
- accounts_receivable collection state machine
- payment/bank reconciliation runtime
- supplier PDF/Word/scan/OCR intake
- supplier alias learning against canonical Library material identity
- goods receipt accounting workflow
- management accounting and settlements
- real 1C connector
- real 1C direct database reader
- live 1C write or automatic posting
- production synchronization or conflict resolution
- Integration Gateway runtime command/event integration
- Operations Control Registry runtime integration
- Warehouse runtime integration
- Calculator runtime integration
- Contract Registry adoption
- production database/migrations
- outbox/inbox/idempotency/correlation/replay
- backup/restore and disaster recovery
- authenticated production API

## Semantic findings

### ACC-F01 â€” STRATEGIC_TARGET_AHEAD_OF_IMPLEMENTATION

Severity: `HIGH`

Current repository is a v0.5 offline 1C sandbox/staging foundation, while Blueprint target has expanded to a P0 operational/commercial accounting registry with receivables, supplier documents, settlements and mature accounting workflows.

Evidence:
- `coordination/status/current_status.md`
- `coordination/module_policy/forprint_accounting_registry_service/module_policy.md`
- `coordination/human_intent/modules/forprint_accounting_registry_service.yaml`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.yaml`

Disposition: `ROADMAP_RECONCILIATION_REQUIRED_NO_IMPLEMENTATION_NOW`

### ACC-F02 â€” CONTRACT_AUTHORITY_DRIFT

Severity: `HIGH`

Repository declares ForPrint Library as future canonical inter-module contract truth, but current Blueprint assigns versioned inter-module contract lifecycle/catalog authority to forprint_contract_registry.

Evidence:
- `forprint_module_manifest.yaml`
- `contracts/placeholders/accounting.invoice_request.v1.yaml`
- `contracts/placeholders/accounting.payment_status_reference.v1.yaml`
- `coordination/global_policy/ecosystem_module_map.md`
- `coordination/module_policy/module_policy_index.yaml`

Disposition: `DEFER_TO_CROSS_PROJECT_CONTRACT_AUTHORITY_RECONCILIATION`

### ACC-F03 â€” ACTIVE_TESTED_SEMANTIC_RESIDUE

Severity: `HIGH`

Generic Counterparty and Product models are tracked and tested as accounting projections but contain CRM/Operations/Logistics/Library/Calculator-like semantics including contacts/channels, delivery profile, manager/tags, price-group and price/production-affecting product attributes.

Evidence:
- `app/forprint_accounting_registry_service/models/counterparty.py`
- `app/forprint_accounting_registry_service/models/product.py`
- `tests/unit/test_counterparty_model.py`
- `tests/unit/test_product_model.py`
- `docs/development/model_naming_rules.md`
- `coordination/module_policy/forprint_accounting_registry_service/goods_receipt_automation_target_state_v0_1_20260826.md`

Disposition: `OWNERSHIP_RECONCILIATION_REQUIRED_PRESERVE_AS_EVIDENCE`

### ACC-F04 â€” VALIDATOR_SEMANTIC_BLIND_SPOT

Severity: `HIGH`

Boundary checker forbids generic Product/Client/Order names only in storage/models.py and one_c_io/*.py, while generic Product and Counterparty models live in models/ and therefore still pass the reported boundary checks.

Evidence:
- `scripts/run_accounting_registry_checks.py`
- `app/forprint_accounting_registry_service/models/counterparty.py`
- `app/forprint_accounting_registry_service/models/product.py`
- `reports/accounting_registry_check_report.json`

Disposition: `VALIDATOR_RECONCILIATION_CANDIDATE`

### ACC-F05 â€” IDENTITY_ALIAS_DRIFT

Severity: `MEDIUM`

Current repository manifest and local placeholder contract text still reference historical forprint_operational_registry naming although Blueprint canonical ID is forprint_operations_control_registry.

Evidence:
- `forprint_module_manifest.yaml`
- `contracts/placeholders/accounting.payment_status_reference.v1.yaml`
- `coordination/machine/module_identity_registry.yaml`

Disposition: `BOUNDED_IDENTITY_RECONCILIATION_CANDIDATE`

### ACC-F06 â€” DECLARED_OWNERSHIP_EXCEEDS_IMPLEMENTED_DOMAIN_RUNTIME

Severity: `HIGH`

Manifest and Blueprint declare invoice/payment/accounting truth ownership, but current persistent implementation provides AccountingDocument plus InvoiceAccountingReference and PaymentAccountingReference shells rather than full invoice/payment or receivable lifecycles.

Evidence:
- `forprint_module_manifest.yaml`
- `app/forprint_accounting_registry_service/storage/models.py`
- `coordination/machine/data_objects.yaml`
- `coordination/human_intent/modules/forprint_accounting_registry_service.yaml`

Disposition: `CAPABILITY_CURRENTNESS_RECONCILIATION_REQUIRED`

### ACC-F07 â€” ONE_C_CAPABILITY_NAMING_OVERSTATEMENT

Severity: `HIGH`

v0.4/v0.5 'direct DB/direct I/O' surfaces are fixture-driven inspection abstractions; binary/database-like .1CD/.dt/.db sources are explicitly unsupported and no real 1C connection is implemented.

Evidence:
- `app/forprint_accounting_registry_service/one_c_io/direct_db.py`
- `app/forprint_accounting_registry_service/one_c_io/schema_probe.py`
- `docs/architecture/one_c_sandbox_direct_io.md`

Disposition: `DOCUMENT_CURRENTNESS_AND_ROADMAP_REFINEMENT_CANDIDATE`

### ACC-F08 â€” SANDBOX_WRITE_SIMULATION_SEMANTIC_MISMATCH

Severity: `HIGH`

Non-dry-run sandbox write experiment can return applied=true after safety checks without executing the declared operations against the working copy; current semantics represent authorization/simulation, not an actual write.

Evidence:
- `app/forprint_accounting_registry_service/one_c_io/sandbox_write.py`
- `tests/unit/test_one_c_sandbox_write_hardening.py`

Disposition: `SEMANTIC_NAMING_AND_TEST_RECONCILIATION_CANDIDATE`

### ACC-F09 â€” SOURCE_PROVENANCE_BINDING_GAP

Severity: `HIGH`

Import pipeline validates a OneCSandboxSource object but accepts a separate export_path without proving the path corresponds to the validated source; raw snapshot file_hash is also not populated in the pipeline.

Evidence:
- `app/forprint_accounting_registry_service/one_c_io/import_pipeline.py`
- `app/forprint_accounting_registry_service/storage/models.py`
- `app/forprint_accounting_registry_service/one_c_io/test_database_registry.py`

Disposition: `FUTURE_SECURITY_AND_PROVENANCE_HARDENING_CANDIDATE`

### ACC-F10 â€” SANITIZATION_TRUSTS_DECLARED_METADATA

Severity: `MEDIUM`

Sanitization layer validates metadata flags rather than sanitizing content; parsers commonly default batches to sanitized/non-production. This is acceptable for current controlled fixtures but must not be interpreted as proof that arbitrary external files are safe.

Evidence:
- `app/forprint_accounting_registry_service/one_c_io/sanitization.py`
- `app/forprint_accounting_registry_service/one_c_io/export_parsers.py`
- `app/forprint_accounting_registry_service/one_c_io/sandbox_sources.py`

Disposition: `CURRENT_SANDBOX_ASSUMPTION_FUTURE_EXTERNAL_INPUT_GATE_REQUIRED`

### ACC-F11 â€” STATUS_SURFACE_STALENESS

Severity: `MEDIUM`

coordination/status/current_status.yaml contains literal {now}/{branch}/{commit} placeholders and marks checks pending, while repository carries an older generated check report with status OK; neither should be treated as a fresh authoritative current verification.

Evidence:
- `coordination/status/current_status.yaml`
- `coordination/status/current_status.md`
- `reports/accounting_registry_check_report.json`

Disposition: `CURRENT_STATUS_GENERATION_RECONCILIATION_CANDIDATE`

### ACC-F12 â€” OPERATOR_CHECK_SIDE_EFFECT

Severity: `MEDIUM`

Make governance-check invokes blueprint-pull and status-report; therefore a nominal check may mutate sibling Blueprint checkout and generated report files instead of being purely non-mutating validation.

Evidence:
- `Makefile`

Disposition: `INTERNAL_SERVICE_IMPROVEMENT_CANDIDATE`

### ACC-F13 â€” PLACEHOLDER_SURFACE

Severity: `MEDIUM`

Several surfaces remain empty placeholders: docs/ARCHITECTURE.md, two app contract schema JSON files, scripts/dev_check.sh and tests/contract/test_contract_files_exist.py.

Evidence:
- `docs/ARCHITECTURE.md`
- `app/forprint_accounting_registry_service/contracts/incoming/accounting_export_requested.v1.schema.json`
- `app/forprint_accounting_registry_service/contracts/outgoing/library_change_request_submitted.v1.schema.json`
- `scripts/dev_check.sh`
- `tests/contract/test_contract_files_exist.py`

Disposition: `CLASSIFY_AS_PLACEHOLDER_DO_NOT_TREAT_AS_CAPABILITY`

### ACC-F14 â€” UNWIRED_STORAGE_SURFACES

Severity: `MEDIUM`

RequiredFieldMissingIssueStorage, FieldTypeMismatchIssueStorage and DefaultValueDecisionStorage exist, but current mapping policy/service does not create these typed records; current persistence primarily uses MappingIssueStorage and UnmappedFieldRecordStorage.

Evidence:
- `app/forprint_accounting_registry_service/storage/mapping_models.py`
- `app/forprint_accounting_registry_service/services/mapping_issue_registry.py`
- `app/forprint_accounting_registry_service/one_c_io/mapping.py`

Disposition: `PARTIAL_FOUNDATION_NOT_CURRENT_RUNTIME_CAPABILITY`

### ACC-F15 â€” PRODUCTION_RELIABILITY_GAP_EXPECTED

Severity: `MEDIUM`

No production migrations, transactional batch boundary, outbox/inbox/idempotency/correlation/replay, backup/restore or live integration resilience exists; this matches the sandbox stage but is a hard gate before production accounting automation.

Evidence:
- `app/forprint_accounting_registry_service/storage/database.py`
- `app/forprint_accounting_registry_service/one_c_io/import_pipeline.py`
- `docs/architecture/accounting_storage_foundation.md`

Disposition: `FUTURE_OPERATIONAL_FITNESS_GATE`

### ACC-F16 â€” MACHINE_CURRENTNESS_GAP

Severity: `MEDIUM`

Blueprint machine marks accounting_to_crm_financial_status and associated data flow active_development, but repository has no cross-module runtime endpoint/transport integration beyond health and local placeholder contracts.

Evidence:
- `coordination/machine/contracts.yaml`
- `coordination/machine/data_flows.yaml`
- `app/forprint_accounting_registry_service/main.py`
- `contracts/placeholders/accounting.payment_status_reference.v1.yaml`

Disposition: `MACHINE_STATUS_RECONCILIATION_CANDIDATE`

## Roadmap reconciliation candidates

These are candidate refinements to existing H-steps. They do not create new execution authority.

### ACC-R01 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01`

Record exact current generation as v0.5 offline sanitized import/staging foundation plus governance overlay, and distinguish current local capability from broader strategic accounting target.

### ACC-R02 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H02`

Explicitly reconcile generic Counterparty/Product/ExternalMapping residue with stable Business Partner, Library catalog/material semantics, Operations identities and accounting-only projections.

### ACC-R03 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03`

Classify raw snapshot, staging, mapping, mapping diagnostics, import/export/reconciliation jobs, AccountingDocument and invoice/payment/order references as implemented foundation versus shell/placeholder.

### ACC-R04 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H04`

Use existing Counterparty fields as evidence for required billing/customer/responsibility decomposition rather than adopting them as canonical accounting ownership.

### ACC-R05 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H06`

State that current parsers cover structured JSON/CSV/XML/YAML/TXT exports only; PDF/Word/scans/OCR, supplier-template learning and canonical material alias mapping remain future target capabilities.

### ACC-R06 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H07`

Record that invoice/payment references exist only as shells; accounts-receivable state machine, promises, disputes, partial payment and bank/payment reconciliation remain unimplemented.

### ACC-R07 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09`

Clarify actual 1C maturity: fixture/manual export parsing and safe sandbox abstractions exist; real direct DB/API connection, source binding, idempotency, recovery/conflict rules and live writes do not.

### ACC-R08 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10`

Add Contract Registry and Integration Gateway readiness to dependency gating, alongside Operations, Library, Warehouse and Calculator; stable Business Partner reference boundary must also be resolved.

## Machine / cross-project reconciliation candidates

- **ACC-M01 â€” machine/contracts.yaml + machine/data_flows.yaml**: accounting_to_crm_financial_status active_development has no corresponding runtime integration in module code. (`action_now: none`)
- **ACC-M02 â€” machine/modules.yaml + machine/ownership.yaml + machine/data_objects.yaml**: Declared invoice/payment/accounting ownership is strategically valid but implementation maturity is only document/reference shells; avoid reading machine ownership as proof of implemented lifecycle. (`action_now: none`)
- **ACC-M03 â€” contract authority**: Repository points canonical contract truth to Library while Blueprint has Contract Registry as interface contract authority. (`action_now: none`)
- **ACC-M04 â€” module identity references**: Repository still contains historical forprint_operational_registry references that should eventually reconcile to canonical forprint_operations_control_registry while preserving history. (`action_now: none`)
- **ACC-M05 â€” 1C capability/state representation**: Machine/roadmap should distinguish offline sandbox export parsing from production synchronization/live connector capability. (`action_now: none`)
- **ACC-M06 â€” party and catalog references**: Generic Counterparty/Product models require alignment with stable Business Partner and Library canonical identities before they can influence machine ownership. (`action_now: none`)

## Verification interpretation

The repository contains a historical generated check report with overall `OK`, and the clean corpus contains 117 test functions. That is useful evidence, but it is not treated as fresh verification of the current audit moment because `coordination/status/current_status.yaml` still marks checks pending and contains literal generation placeholders.

Strong existing verification themes:
- sandbox production-write refusal
- mapping/manual-review behavior
- local SQLModel storage
- structured export parsing
- placeholder contract markers
- boundary documentation presence

Verification gaps:
- boundary validator misses generic models package
- no adversarial external-input corpus
- no cross-module contract tests
- no production idempotency/retry/recovery tests
- no accounts-receivable workflow tests
- no supplier PDF/OCR workflow tests
- no live 1C integration tests by design

## Methodology improvements learned from this module

### METH-ACC-01

Problem: Initial preflight included virtualenv dependency tree and distorted semantic source counts.

Proposal: Standard L0 inventory must exclude all recognized virtualenv/generated package metadata before semantic segmentation.

Applied to current analysis: `true`

### METH-ACC-02

Problem: v0.1 porcelain parser stripped the leading status space of first Git record.

Proposal: Preserve raw leading spaces when parsing git status --porcelain and test staged/unstaged/deleted/untracked cases.

Applied to current analysis: `true`

### METH-ACC-03

Problem: v0.2 clean-current archive still captured .git metadata/object files although semantic packet selection did not use them.

Proposal: Exclude .git from inventory/archive corpus itself, not only from semantic packet selection; report semantic module file count separately from transport/provenance metadata.

Applied to current analysis: `false`

### METH-ACC-04

Problem: A green validator can hide semantic blind spots when it checks only selected directories.

Proposal: L0 semantic audit should compare validator coverage scope against actual risky semantic surfaces and record validator-semantic gaps.

Applied to current analysis: `true`

## L0 decision

The module is **knowledge-stable enough to proceed to cross-project reconciliation**.

Do not implement or clean the module in this analysis contour.

Next:

`BUILD_CROSS_PROJECT_BLUEPRINT_RECONCILIATION_PACKET`
