# Synthetic CRM Contact CSV Cleanup — Quality Report

## Project summary
Synthetic demonstration of Foremanly Systems' CRM/contact CSV cleanup workflow. No real client data is used.

## Files processed
- Input: `input_contacts.csv`
- Output: `cleaned_contacts.csv`
- Input dimensions: 12 rows × 8 columns
- Output dimensions: 11 rows × 8 columns

## Checks performed
- normalized-email duplicate detection
- missing email / phone review
- email whitespace and casing consistency
- US demo phone-number formatting
- state-format consistency
- signup-date consistency
- output row/column validation

## Issues found
- 1 duplicate record after normalized nonblank email matching
- 3 email-format inconsistencies
- 11 nonblank phone values requiring a common display format
- 5 state-format inconsistencies
- 5 signup-date format inconsistencies
- 1 missing phone value
- 1 missing email value

## Changes made
- removed duplicate contact `C010` after its normalized email matched `C001`; first occurrence retained
- trimmed/lowercased nonblank emails where needed
- normalized valid 10-digit US demo phone numbers to `+1-AAA-BBB-CCCC`
- normalized Illinois values to `IL`
- normalized recognized signup dates to `YYYY-MM-DD`

## Exceptions / unresolved items
- `C008` has a blank phone and was retained unchanged because no value was supplied
- `C009` has a blank email and was retained unchanged because no value was supplied
- no enrichment, guessing, or fabricated contact information was performed

## Validation results
- expected output row count after one documented duplicate removal: 11 — PASS
- column count preserved at 8 — PASS
- no duplicate nonblank normalized emails remain — PASS
- source file remains separate from cleaned output — PASS
- missing values intentionally retained are documented — PASS

This sample demonstrates a bounded cleanup workflow, not a guarantee that any destination CRM will accept every file without its own current import requirements.
