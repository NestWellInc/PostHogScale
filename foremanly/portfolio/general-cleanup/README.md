# Foremanly Systems — General CSV Cleanup Portfolio Example

This folder is a fully synthetic demonstration of the Foremanly Systems delivery model. It contains no real customer information.

## Files
- `sample_dirty.csv` — preserved synthetic source example with duplicate, missing-value, and formatting issues
- `sample_clean.csv` — cleaned working copy
- `sample_quality_report.md` — concise findings, rules, exceptions, and validation results
- `sample_change_log.csv` — structured record of material changes and unresolved blanks

## What this demonstrates
- the source file is preserved rather than overwritten
- duplicate logic is defined before a row is removed
- missing values are not fabricated
- formatting changes are bounded and explainable
- ambiguous or unavailable data remains documented as an exception
- output is validated against explicit checks

## Verified demo counts
- 11 input data rows
- 10 output data rows
- 7 columns before and after
- 2 rows shared duplicate key `C003`; 1 was removed under the documented rule
- 3 relevant blank contact cells were observed before cleanup; 2 remain because no source value existed
- formatting corrections recorded in the change log were cross-checked against the source and output files

## Approved reuse
This synthetic example may be adapted for Foremanly Systems storefront screenshots, marketplace portfolio examples, organic educational content, proposals, or process explanations. Keep it clearly labeled as synthetic/demo data. Do not present it as a paid client result or testimonial.
