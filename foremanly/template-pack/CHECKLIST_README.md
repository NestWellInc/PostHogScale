# Foremanly Systems — Spreadsheet Data Quality Checklist

This is the lightweight checklist product for reviewing one CSV or spreadsheet before cleanup, import, analysis, or handoff.

## Included file
- `data_quality_audit_checklist.csv`

## How to use it
1. Preserve the original source file and work from a copy.
2. Open `data_quality_audit_checklist.csv` in Excel, Google Sheets, LibreOffice Calc, or another CSV-compatible spreadsheet tool.
3. Work through each row and update the `status`, `issue_count`, and `notes` fields.
4. Define any duplicate/removal rule before deleting records. If the right rule is unclear, mark the item as needing a decision rather than guessing.
5. Re-run relevant checks after cleanup if you use the checklist as part of a data-cleaning workflow.

## Suggested status values
- `Not Started`
- `In Review`
- `Pass`
- `Issue Found`
- `Not Applicable`
- `Needs Decision`

## What this checklist covers
- original/working-copy integrity
- delimiter, headers, row width, and malformed-row checks
- data-type review
- exact and suspected duplicates
- missing and required-field values
- whitespace, dates, numbers, currency, booleans, identifiers, and casing
- initial row/column counts
- client/project constraints
- ambiguous cases and unsupported assumptions

## What it does not include
The lightweight checklist does not include the full quality-report template, change/exception log, duplicate-rule worksheet, validation worksheet, or intake/scope questionnaire contained in the CSV Quality Control Template Pack.

## Scope limitation
This checklist is a workflow aid. It does not guarantee that a dataset is universally error-free, compliant, secure, or accepted by a destination system. Adapt the checks to the actual dataset and intended use.
