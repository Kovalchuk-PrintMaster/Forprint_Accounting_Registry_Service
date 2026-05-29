# OneC Snapshot Staging Flow

## Purpose

This document describes the approved v0.2 1C snapshot/staging flow.

## Flow

```text
1C export file / snapshot source
  ↓
OneCRawSnapshot
  ↓
OneCImportJob
  ↓
OneCStagingRecord
  ↓
validation / normalization candidate
  ↓
OneCMappingRecord
Raw snapshot rule

Raw snapshot metadata is stored in OneCRawSnapshot.

Raw data must not be treated as clean canonical ForPrint data.

Staging rule

OneCStagingRecord is a temporary/staging representation.

It may contain:

raw 1C payload;
normalized candidate payload;
validation status;
1C identifiers.

It must not become:

CRM client profile;
Library catalog truth;
Operational Registry entity;
warehouse stock truth.
Mapping rule

OneCMappingRecord connects accounting/internal references with 1C identifiers.

Mapping exists for accounting synchronization and reconciliation only.

Deferred

Do not implement yet:

real 1C API integration;
full 1C import;
production 1C synchronization;
payment import;
warehouse integration;
full 1C mirror.

---