# Foremanly Systems — Synthetic Data Quality Report

**Project type:** General CSV cleanup and normalization demo  
**Source:** `sample_dirty.csv`  
**Output:** `sample_clean.csv`  
**Data:** Fully synthetic demonstration data; no real client information.

## Project summary
Foremanly Systems reviewed one synthetic customer CSV for duplicate records, missing values, inconsistent formatting, and structural consistency. The original sample is preserved separately and all cleanup was applied to a working copy.

## Counts
- Input data rows: **11**
- Output data rows: **10**
- Columns: **7** before and after
- Duplicate-key rows identified: **2 rows sharing `customer_id=C003`**
- Duplicate records removed after rule application: **1**
- Blank cells observed in relevant contact fields before cleanup: **3**
- Blank cells remaining after cleanup: **2**

## Duplicate rule
`customer_id` is treated as the record key for this demonstration.

When duplicate rows share the same `customer_id`, retain the more complete record only when the competing values are consistent and the rule is unambiguous. For `C003`, the second row contained the same name, phone identity, date, status, and amount plus the missing email address, so that more complete row was retained.

## Issues found and changes made
- Trimmed leading/trailing whitespace in names, emails, and status values.
- Standardized email addresses to lowercase.
- Standardized U.S. phone values to `+1##########` where a phone value was present.
- Standardized dates to ISO `YYYY-MM-DD`.
- Standardized status values to lowercase `active` / `inactive`.
- Standardized monetary values to plain numeric values with two decimal places.
- Normalized name presentation where inconsistent casing was clearly formatting-only.
- Removed one duplicate `C003` row under the documented key/completeness rule.

## Missing values / exceptions
- `C002.phone` remains blank because no source value was supplied.
- `C006.email` remains blank because no source value was supplied.
- No value was invented to fill either missing field.

## Validation results
- Output contains exactly one row per `customer_id`.
- Output column count matches the source schema.
- No new customer IDs were introduced.
- Output row count equals input row count minus the one documented duplicate removal.
- All populated dates follow `YYYY-MM-DD`.
- All populated statuses use the agreed normalized values.
- All populated amount values use two decimal places.

## Scope note
This sample demonstrates a bounded cleanup workflow. Real projects require agreed duplicate logic, required-field rules, destination requirements, and handling instructions before ambiguous transformations are made.
