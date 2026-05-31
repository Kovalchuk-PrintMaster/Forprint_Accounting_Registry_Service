# OneC Directory Exchange

## Purpose

This document defines v0.4 accounting directory exchange.

Directories here are accounting/reference directories from 1C-like context.

They are not canonical ForPrint Library catalogs.

## Allowed directory concepts

- counterparty accounting references;
- nomenclature accounting references;
- invoice/accounting document references;
- payment/accounting status references;
- unit/code/tax/accounting codes as references.

## Forbidden interpretation

Directory exchange must not become:

- canonical CRM client registry;
- canonical product catalog;
- canonical material catalog;
- Library replacement;
- Operational Registry order truth.

## Flow

```text
OneC directory fixture/export
  ↓
OneCDirectorySnapshot
  ↓
OneCDirectoryImportBatch
  ↓
OneCStagingRecord
  ↓
mapping/default policy
Export rule

Directory exports are dry-run by default.

Production writes are forbidden in v0.4.


## `docs/architecture/one_c_report_extraction.md`

```markdown
# OneC Report Extraction

## Purpose

This document defines v0.4 report extraction interface.

The goal is to extract accounting report-like outputs from test/sandbox data without depending on fragile UI screens.

## Initial report categories

- counterparty balance snapshot;
- invoice register snapshot;
- payment register snapshot;
- sales turnover snapshot;
- mutual settlement snapshot;
- nomenclature turnover snapshot.

## Boundary

These are Accounting Registry report snapshots.

They are not:

- CRM analytics dashboards;
- Operational Registry reports;
- full 1C report engine replacement.

## Flow

```text
report definition
  ↓
report request
  ↓
report snapshot
  ↓
report rows
  ↓
staging records / mapping issues
Raw value rule

Report rows preserve raw source values.

Normalization must not overwrite source truth silently.