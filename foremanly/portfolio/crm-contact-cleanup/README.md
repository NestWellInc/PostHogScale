# CRM Contact CSV Cleanup — Synthetic Portfolio Example

This folder is a synthetic demonstration for Foremanly Systems' `CRM Contact CSV Cleanup` offer. It contains no client data and must never be presented as a testimonial or real customer result.

## Files
- `input_contacts.csv` — intentionally inconsistent synthetic source data
- `cleaned_contacts.csv` — bounded cleaned output
- `quality_report.md` — issue counts, corrections, exceptions, and validation
- `change_exception_log.csv` — auditable rule/change summary

## Demonstrated rules
- preserve the original source separately
- define duplicate logic explicitly: normalized nonblank email exact-match, retain first occurrence
- normalize only deterministic formatting
- retain and document missing values instead of inventing contact information
- validate row/column counts after cleanup

## Verified result
- input: 12 rows × 8 columns
- output: 11 rows × 8 columns
- duplicate removed: `C010`, matching `C001` after email normalization
- blank phone retained: `C008`
- blank email retained: `C009`

## Marketing use
May be used for Foremanly product screenshots, marketplace galleries, proposals, and educational content when clearly labeled `Synthetic Demo` or equivalent. Do not imply the example is client work or proof of guaranteed CRM import acceptance.
