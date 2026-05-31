# OneC Version Strategy

## Purpose

The system must not depend on one specific 1C version or department-specific export shape.

## Supported placeholders

Current v0.3 version markers:

- `one_c_8_2`
- `one_c_8_3`
- `unknown_future_version`

## Strategy

Different departments may use:

- different 1C versions;
- different export formats;
- different custom configurations;
- BAS-like future variants.

Therefore Accounting Registry uses an adapter registry:

version + channel → adapter
Boundary

Version-specific adapters must normalize only into Accounting Registry staging.

They must not create canonical CRM, Operational Registry, Library, or warehouse truth.