# Foremanly Systems — CSV Quality Control Template Pack

This pack provides a reusable, auditable workflow for reviewing and cleaning CSV/spreadsheet data without silently changing the source.

## Included files
- `data_quality_audit_checklist.csv` — pre-clean issue review
- `quality_report_template.md` — concise client-facing quality report
- `change_exception_log.csv` — record what changed, what was retained, and why
- `duplicate_rule_worksheet.csv` — define duplicate logic before removal
- `validation_checklist.csv` — pre-clean/post-clean acceptance checks
- `intake_scope_questionnaire.md` — scope and client-rule intake

## Core rules
1. Preserve the original source file exactly as received.
2. Work from a copy.
3. Define duplicate/removal rules before deleting records.
4. Do not invent values for missing data unless a deterministic rule is explicitly authorized.
5. Flag ambiguous cases rather than making silent assumptions.
6. Document material changes and exceptions.
7. Validate the cleaned output against agreed checks.

## Important limitation
These templates are workflow aids. They do not guarantee an error-free dataset, regulatory compliance, security, or acceptance by a destination platform. Adapt checks to the actual dataset and client requirements.
