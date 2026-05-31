# OneC Mapping Policy

## Purpose

This document defines safe mapping/default rules for 1C source data.

## Rules

When a ForPrint field does not match a 1C field:

1. never silently guess critical accounting values;
2. preserve raw source value in `OneCRawSnapshot`;
3. store normalized attempt in `OneCStagingRecord`;
4. record mapping issue if a required field is missing;
5. apply explicit default only if policy allows it;
6. mark default source clearly;
7. never overwrite source truth silently.

## Default categories

Allowed categories:

- `system_default`
- `configured_default`
- `source_default`
- `manual_review_required`
- `blocked_until_mapped`

Critical accounting fields should default to:

```text
manual_review_required

not automatic values.

Unknown fields

Unknown fields must be captured as unmapped fields.

They must not be discarded silently.