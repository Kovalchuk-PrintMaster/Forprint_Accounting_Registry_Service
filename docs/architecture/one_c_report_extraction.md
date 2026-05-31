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

## Raw value rule

Report rows preserve raw source values.

Normalization must not overwrite source truth silently.