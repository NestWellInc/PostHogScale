# Foremanly Systems — CSV Quality Control Template Pack

## Start here
This pack is designed to make CSV and spreadsheet quality work more consistent, reviewable, and easier to explain. It does not clean data automatically. It gives you a repeatable workflow for defining rules, checking a working copy, recording changes, and validating the result.

## Recommended workflow
1. **Preserve the original.** Keep the source file unchanged and create a separate working copy.
2. **Define the job.** Use `intake_scope_questionnaire.md` to record the intended outcome, required fields, output format, duplicate logic, formatting standards, destination requirements, and any handling constraints.
3. **Define duplicate rules before deleting anything.** Use `duplicate_rule_worksheet.csv`. If the correct rule is uncertain, flag suspected duplicates instead of removing them.
4. **Run the pre-clean review.** Use `data_quality_audit_checklist.csv` to inspect structure, duplicates, missing values, formatting, and exceptions.
5. **Document material changes.** Record rules, affected counts, actions, and exceptions in `change_exception_log.csv` while you work.
6. **Validate the result.** Use `validation_checklist.csv` to compare the working file before and after cleanup and confirm the agreed checks still pass.
7. **Summarize the work.** Use `quality_report_template.md` to create a concise record of what was checked, what changed, what remained unresolved, and what was validated.

## Files in the full pack
- `data_quality_audit_checklist.csv` — structured pre-clean quality review
- `duplicate_rule_worksheet.csv` — define what counts as a duplicate and what action is allowed
- `change_exception_log.csv` — record changes, retained issues, and exceptions
- `validation_checklist.csv` — compare pre-clean and post-clean conditions
- `quality_report_template.md` — concise final quality report structure
- `intake_scope_questionnaire.md` — define scope and project-specific rules

## Suggested status values
For checklist `status` fields, use a small consistent vocabulary such as:
- `Not Started`
- `In Review`
- `Pass`
- `Issue Found`
- `Not Applicable`
- `Needs Decision`

For change/exception `status`, useful values include:
- `Corrected`
- `Retained`
- `Removed`
- `Flagged`
- `Needs Decision`

## Important operating rules
- Work on a copy, not the original source file.
- Record project-specific rules before applying destructive changes.
- Do not invent missing values unless an explicit deterministic fill rule has been authorized.
- Preserve leading zeros and identifiers when their formatting carries meaning.
- Treat ambiguous duplicates, mappings, and corrections as exceptions until a rule is defined.
- Re-run relevant checks after cleanup rather than assuming a transformation succeeded.
- Keep the completed quality report and change/exception log with the cleaned output when an audit trail matters.

## Scope limitation
These templates are workflow aids, not a guarantee that a dataset is universally error-free, compliant, secure, or accepted by a destination system. The checks must be adapted to the actual data, purpose, and agreed requirements.
