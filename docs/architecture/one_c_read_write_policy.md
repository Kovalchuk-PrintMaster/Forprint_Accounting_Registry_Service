# OneC Read/Write Policy

## Read policy

Allowed in v0.3:

- local file exchange discovery;
- manual export/import discovery;
- direct DB read-only exploration on test copy only;
- sanitized sample data analysis;
- mapping experiments.

## Direct DB access rule

Direct database reading is allowed only for:

- test copy;
- local sandbox copy;
- read-only mode;
- sanitized sample data;
- reverse-engineering field mapping.

Direct DB access is forbidden for:

- live production write;
- uncontrolled live production read;
- changing 1C schema;
- writing into 1C tables directly;
- treating internal 1C tables as canonical ForPrint interface.

## Write policy

Real writes to live 1C are forbidden in v0.3.

Allowed:

- write policy documentation;
- export package model;
- dry-run export payload;
- export package structure validation.

Forbidden:

- real 1C write;
- direct DB write;
- production sync;
- automatic update of live 1C directories;
- automatic invoice posting;
- payment posting;
- document posting.