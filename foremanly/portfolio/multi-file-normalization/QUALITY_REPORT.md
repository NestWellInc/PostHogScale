# Synthetic Multi-File Cleanup & Normalization — Quality Report

**Use:** synthetic demonstration for Foremanly Systems. This is not client work, a testimonial, or a guaranteed outcome.

## Scope
Two CSV source files with different header names and inconsistent representations were normalized into one consistent output schema. Both source files remain unchanged.

## Input / output verification
- source files: 2
- input rows: 4 + 4 = 8
- output rows: 8
- output columns: 7, including explicit source provenance fields
- rows silently deleted: 0
- missing emails fabricated: 0

## Explicit mapping
- `record_id` / `id` → `source_record_id`
- `customer_name` / `name` → `customer_name`
- `email` / `email_address` → `email`
- `state` / `region` → `state`
- `signup_date` / `joined` → `signup_date`
- `amount` / `total_value` → `amount`
- source filename added as `source_file`

## Deterministic normalization
- email values trimmed and lowercased when present
- state names/codes normalized to two-letter codes for the demonstrated values
- dates normalized to `YYYY-MM-DD`
- currency symbols and thousands separators removed; amounts rendered with two decimal places
- blank emails retained as blank

## Duplicate finding
`Blue Mesa Co` appears once in each source with the same normalized email, date, state, and amount. It is flagged as a cross-file duplicate candidate, but both rows are retained because this demonstration does not assume authorization to delete or merge cross-file records.

## Exceptions / caveats
- Cross-file duplicate resolution requires an explicit client rule before deletion or merge.
- No missing contact data was enriched or guessed.
- This example demonstrates schema alignment and normalization, not guaranteed compatibility with a particular destination system.
