# Foremanly Systems — Spreadsheet Data Quality Checklist

A lightweight reusable checklist for reviewing CSV and spreadsheet data before cleanup, import, analysis, or handoff.

## Included
- `spreadsheet_data_quality_checklist.csv`

## How to use it
1. Preserve the original source file unchanged.
2. Create a working copy before making edits.
3. Complete the **Setup** rows first so the cleanup goal, required fields, and duplicate rule are explicit.
4. Work through the **Pre-clean** checks and record issue counts or notes where useful.
5. Perform only changes supported by the agreed rules.
6. Complete the **Post-clean** checks and reconcile any row removals or structural changes.
7. Document unresolved ambiguity rather than filling or removing data by assumption.

Suggested status values: `Not Started`, `Pass`, `Needs Review`, `Not Applicable`.

## What this product is
This is the checklist-only Foremanly resource. It is designed for a simple repeatable data-quality review process.

The larger **CSV Quality Control Template Pack** is a separate product and adds a quality-report template, structured change/exception log, duplicate-rule worksheet, validation worksheet, and intake/scope questionnaire.

## Important limitation
This checklist is a workflow aid. It does not guarantee an error-free dataset, regulatory compliance, security, or acceptance by a destination platform. Adapt each check to the actual data and project requirements.
