# ForPrint Accounting Registry Service â€” Cross-Project Blueprint Reconciliation v0.1

## Result

`PASS_RECONCILIATION_READY_FOR_BOUNDED_CANONICAL_PREVIEW`

- Accounting source HEAD: `7315a7a6bd0a8f4e08385bdbd676edaf8aa25bb5`
- analysis authority only; `action_now: none`
- no new roadmap step IDs
- no approval-state changes
- no execution-authority changes
- no machine mutation recommended in this L0 closeout

## Core reconciliation decision

The current Blueprint Accounting direction is broadly correct. The audit does not justify reassigning invoice/payment/accounting ownership or rewriting the machine model. The main gap is **currentness precision**: the roadmap target is broader than the current v0.5 module implementation.

Therefore the recommended canonical action is a bounded enrichment of existing Accounting roadmap steps H01, H02, H03, H04, H06, H07, H09 and H10. H05 and H08 remain unchanged.

## Finding disposition matrix

| Finding | Classification | Roadmap | Machine | Canonical disposition |
|---|---|---|---|---|
| `ACC-F01` | `STRATEGIC_TARGET_AHEAD_OF_IMPLEMENTATION` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03 | `NO_CHANGE` | `REFINE_EXISTING_ROADMAP_STEPS` |
| `ACC-F02` | `CONTRACT_AUTHORITY_DRIFT` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10 | `DEFER_NO_EVIDENCE_OWNERSHIP_IS_WRONG` | `ADD_CONTRACT_AND_ROUTING_READINESS_TO_DEPENDENCY_GATE` |
| `ACC-F03` | `ACTIVE_TESTED_SEMANTIC_RESIDUE` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H02, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H04 | `NO_CHANGE` | `REFINE_OWNERSHIP_AND_CONTEXT_STEPS` |
| `ACC-F04` | `VALIDATOR_SEMANTIC_BLIND_SPOT` | â€” | `NO_CHANGE` | `NO_PORTFOLIO_ROADMAP_CHANGE` |
| `ACC-F05` | `IDENTITY_ALIAS_DRIFT` | â€” | `NO_CHANGE` | `NO_BLUEPRINT_IDENTITY_CHANGE` |
| `ACC-F06` | `DECLARED_OWNERSHIP_EXCEEDS_IMPLEMENTED_DOMAIN_RUNTIME` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03 | `DEFER_STATUS_CURRENTNESS_NOT_OWNERSHIP_ERROR` | `REFINE_CURRENTNESS_WITHOUT_REASSIGNING_OWNERSHIP` |
| `ACC-F07` | `ONE_C_CAPABILITY_NAMING_OVERSTATEMENT` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09 | `NO_CHANGE` | `REFINE_CURRENT_1C_MATURITY` |
| `ACC-F08` | `SANDBOX_WRITE_SIMULATION_SEMANTIC_MISMATCH` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09 | `NO_CHANGE` | `REFINE_H09_SAFETY_CURRENTNESS` |
| `ACC-F09` | `SOURCE_PROVENANCE_BINDING_GAP` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09 | `NO_CHANGE` | `REFINE_H09_WITH_SOURCE_BINDING_REQUIREMENT` |
| `ACC-F10` | `SANITIZATION_TRUSTS_DECLARED_METADATA` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09 | `NO_CHANGE` | `REFINE_H09_WITH_UNTRUSTED_INPUT_BOUNDARY` |
| `ACC-F11` | `STATUS_SURFACE_STALENESS` | â€” | `NO_CHANGE` | `NO_PORTFOLIO_ROADMAP_CHANGE` |
| `ACC-F12` | `OPERATOR_CHECK_SIDE_EFFECT` | â€” | `NO_CHANGE` | `NO_PORTFOLIO_ROADMAP_CHANGE` |
| `ACC-F13` | `PLACEHOLDER_SURFACE` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03 | `NO_CHANGE` | `REFINE_SELF_INVENTORY_LANGUAGE` |
| `ACC-F14` | `UNWIRED_STORAGE_SURFACES` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03 | `NO_CHANGE` | `REFINE_H03_IMPLEMENTED_VS_UNWIRED_INVENTORY` |
| `ACC-F15` | `PRODUCTION_RELIABILITY_GAP_EXPECTED` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09, FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10 | `NO_CHANGE` | `REFINE_MATURE_1C_AND_DEPENDENCY_GATES` |
| `ACC-F16` | `MACHINE_CURRENTNESS_GAP` | FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10 | `DEFERRED_RECONCILE_BEFORE_IMPLEMENTATION` | `DO_NOT_MUTATE_MACHINE_IN_L0_CLOSEOUT` |

## Proposed existing-step roadmap refinements

### ACC-R01 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01`

Record the exact current accepted local baseline as v0.5 offline/sandbox sanitized structured-export parsing -> raw snapshot/staging -> mapping/default/manual-review diagnostics with local persistence and governance overlay. Explicitly state that this does not establish production accounting runtime, live 1C integration, accounts-receivable automation or cross-module runtime integration. Include placeholder/currentness and validator-semantic gaps as evidence to reconcile, not as automatic repair instructions.

### ACC-R02 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H02`

Confirm Accounting ownership of accounting/financial facts, references, documents and reconciliation while treating generic Counterparty/Product fields as tested historical projection residue until stable Business Partner, Operations, CRM, Logistics, Library and Calculator boundaries are reconciled; do not adopt contact/delivery/catalog/pricing/production semantics as Accounting truth.

### ACC-R03 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03`

Inventory raw snapshots, staging, mapping/default/manual-review records, mapping issues, import/export/reconciliation job foundations, AccountingDocument, invoice/payment/order references and typed diagnostic storage with explicit implemented / shell / placeholder / unwired classifications rather than treating file presence as runtime capability.

### ACC-R04 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H04`

Define billing/customer/responsibility contexts on stable external Business Partner/operational references; explicitly exclude current generic Counterparty contact channels, delivery profile, manager/tags and Product price/production attributes from becoming canonical Accounting ownership. Preserve proof/sample billing policy as an independent financial classification.

### ACC-R05 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H06`

Distinguish current structured sanitized export parsing (JSON/CSV/XML/YAML/TXT) from the future supplier-document target. Plan Excel/structured supplier files, PDF, Word-like documents and scan/photo OCR into reviewable staging with preserved source/provenance, confidence and human confirmation; supplier alias/SKU mapping resolves to canonical Library material identity and never silently posts uncertain financial facts.

### ACC-R06 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H07`

Record that current invoice/payment objects are storage/reference foundations rather than a complete accounts-receivable lifecycle. Define future receivable/payment reconciliation views around the agreed DUE -> overdue/promise/human-attention state model and side states, with CRM/Telegram as communication/read surfaces and any conditional payment mandate explicitly later, preauthorized, limited, idempotent and auditable.

### ACC-R07 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09`

Define current 1C maturity precisely: manual/sanitized structured-file parsing, fixture-driven schema/discovery abstractions, dry-run export packaging and disposable working-copy safety/authorization simulation exist; real 1C connector/direct database reader/live write/synchronization do not. Mature exchange requires source-to-export provenance binding, untrusted-input controls, idempotency/correlation, retry/replay/conflict handling, migrations, rollback/recovery and backup/restore evidence before live activation.

### ACC-R08 â†’ `FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10`

Keep automation expansion gated until Operations, Library, Warehouse and Calculator boundaries are ready, and additionally require Contract Registry contract readiness plus Integration Gateway routing/runtime readiness. A stable Business Partner/customer/billing identity reference boundary must be resolved before cross-module automation. Do not interpret machine active_development flow status as proof that Accounting currently exposes a live financial-status runtime.

Dependency-gate additions: `forprint_contract_registry`, `forprint_integration_gateway`

## Machine decision

All six machine candidates remain deferred/no-change. In particular, `accounting_to_crm_financial_status.v1` being `active_development` while the module has no live runtime surface is a real currentness question, but changing that state requires a project-wide definition of machine currentness/status semantics. This L0 module audit must not invent that policy.

## Dependency refinement

Current Accounting dependency lists contain Operations Control Registry, Library, Warehouse and Calculator. The audit adds two clear readiness dependencies for mature cross-module automation: `forprint_contract_registry` for accepted versioned contracts and `forprint_integration_gateway` for routed runtime integration. Stable Business Partner/customer/billing identity remains a required boundary to resolve, but this packet does not invent a canonical owner for that identity.

## Deferred module-local remediation

- **ACC-LOCAL-01** `module_semantic_reconciliation` â€” generic Counterparty/Product models contain cross-domain semantics (`action_now: none`)
- **ACC-LOCAL-02** `validator_semantic_coverage` â€” boundary validator does not cover models/ generic projection surfaces (`action_now: none`)
- **ACC-LOCAL-03** `identity_alias_reconciliation` â€” historical forprint_operational_registry references remain in manifest/contracts (`action_now: none`)
- **ACC-LOCAL-04** `contract_authority_reconciliation` â€” local canonical_contract_truth still points to Library instead of current Contract Registry direction (`action_now: none`)
- **ACC-LOCAL-05** `sandbox_write_semantics` â€” applied=true may represent authorization/simulation rather than an executed write (`action_now: none`)
- **ACC-LOCAL-06** `source_provenance_security` â€” validated source is not strongly bound to export_path and snapshot hash is not populated by pipeline (`action_now: none`)
- **ACC-LOCAL-07** `external_input_trust` â€” sanitization trusts declared metadata and parser defaults within controlled sandbox (`action_now: none`)
- **ACC-LOCAL-08** `status_generation` â€” current_status contains literal placeholders and stale/pending verification semantics (`action_now: none`)
- **ACC-LOCAL-09** `operator_surface_side_effect` â€” governance-check invokes potentially mutating blueprint-pull/status-report (`action_now: none`)
- **ACC-LOCAL-10** `placeholder_and_unwired_surface` â€” empty placeholders and typed but unwired mapping diagnostic storage must not be counted as active capability (`action_now: none`)

## Methodology observations

- **METH-ACC-01** â€” Standard L0 inventory must exclude all recognized virtualenv/generated package metadata before semantic segmentation.
- **METH-ACC-02** â€” Preserve raw leading spaces when parsing git status --porcelain and test staged/unstaged/deleted/untracked cases.
- **METH-ACC-03** â€” Exclude .git from inventory/archive corpus itself, not only from semantic packet selection; report semantic module file count separately from transport/provenance metadata.
- **METH-ACC-04** â€” L0 semantic audit should compare validator coverage scope against actual risky semantic surfaces and record validator-semantic gaps.

## Exact next boundary

Build a read-only canonical preview against exactly four Blueprint roadmap files:

- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.md`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.yaml`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.md`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.yaml`

The preview must prove:

- only Accounting H01/H02/H03/H04/H06/H07/H09/H10 are refined;
- H05 and H08 are unchanged;
- no new Accounting step IDs are created;
- no non-Accounting module steps change;
- no approval/source-basis/execution-authority state changes;
- only approved dependency additions are introduced;
- no machine/Human Intent/module-policy/CF-10/current-execution-focus mutation occurs.

Next:

`BUILD_EXACT_BOUNDED_CANONICAL_ENRICHMENT_PREVIEW`
