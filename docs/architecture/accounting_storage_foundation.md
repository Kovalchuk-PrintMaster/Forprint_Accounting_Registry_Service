# Accounting Storage Foundation

## Purpose

This document describes the v0.2 storage foundation for `forprint_accounting_registry_service`.

The storage foundation is intentionally small.

It supports only Accounting Registry / 1C boundary data.

## Approved scope

The service may store:

- 1C raw snapshots;
- 1C staging records;
- 1C mapping records;
- import jobs;
- export jobs;
- reconciliation jobs;
- accounting document shells;
- invoice accounting references;
- payment accounting references;
- order accounting references.

## Not a production DB strategy

The current storage layer is a lightweight SQLModel/SQLite-compatible foundation.

It is intended for:

- schema creation tests;
- local development;
- repository/service tests;
- boundary validation.

It is not yet a finalized production database strategy.

## Ownership boundary

Accounting Registry stores accounting and 1C-boundary truth.

Operational Registry will store operational truth.

ForPrint Library will store canonical catalogs, contracts, semantic IDs, aliases, and versioning.

ForPrint CRM will own business workflow coordination and dashboard/human-facing workflow.

ForPrint Integration Gateway will route runtime commands later where validation, idempotency, and transport are required.

## Forbidden

This storage foundation must not become:

- CRM;
- Operational Registry;
- Library;
- warehouse service;
- product catalog truth;
- material catalog truth;
- client registry;
- order registry;
- production status registry;
- general business database;
- full 1C mirror for everything.