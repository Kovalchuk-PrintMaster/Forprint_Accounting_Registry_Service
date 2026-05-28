# 1C Boundary

## Purpose

This document defines how `forprint_accounting_registry_service` treats 1C.

1C is an external accounting reality.

1C is not the owner of the whole ForPrint system.

## Allowed 1C responsibilities inside this service

The service may work with:

- 1C raw snapshot files;
- 1C staging records;
- 1C import batches;
- 1C export packages;
- 1C object mappings;
- 1C accounting reconciliation;
- accounting references imported from 1C.

## Raw snapshot rule

Raw 1C snapshot data must be preserved as-is.

Raw data should not be manually rewritten to fit internal assumptions.

Normalization must happen in a separate staging or projection layer.

## Mapping rule

The service may store mappings such as:

```text
internal_accounting_id <-> one_c_id
internal_accounting_code <-> one_c_code

These mappings do not make 1C the canonical owner of the ForPrint system.

They only support accounting synchronization and reconciliation.

Projection rule

The service may keep accounting projections of external objects.

Examples:

AccountingCounterpartyReference
OneCCounterpartySnapshot
AccountingCounterpartyProjection
OneCNomenclatureSnapshot
AccountingProductReference
AccountingNomenclatureProjection

These objects must remain accounting-only.

Deferred

Do not implement yet:

real 1C API integration;
full 1C production import;
full 1C mirror;
database-heavy migration layer;
production payment synchronization;
warehouse integration.

---