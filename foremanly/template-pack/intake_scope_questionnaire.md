# Foremanly Systems — Data Cleanup Intake & Scope Questionnaire

## Files and size
1. What file type(s) are you providing? CSV, XLSX, Google Sheets export, or other?
2. How many files are included?
3. Approximately how many rows and columns are in each file?
4. What output format do you need?

## Cleanup goal
5. What problem are you trying to solve with this data?
6. Which checks do you want performed: duplicates, missing values, formatting, structural issues, or all of these?
7. Is the file being prepared for a specific system or import? If yes, provide the destination and its current field/import specification.

## Duplicate rules
8. What should count as a duplicate?
9. If duplicate records are found, should they be removed, retained, merged under an explicit rule, or only flagged?
10. If one duplicate record is kept, what rule determines which record wins?

## Missing values
11. Which fields are required?
12. Are blank values acceptable in any columns?
13. Should missing values ever be filled automatically? If yes, provide the exact deterministic rule. Otherwise they will be flagged, not invented.

## Formatting
14. What date format should be used?
15. Are there required standards for phone numbers, currency, decimals, booleans, casing, or identifiers?
16. Should leading zeros in identifiers be preserved?

## Structural rules
17. Are there expected headers or a target column order?
18. Are rows allowed to be deleted, or should suspect rows only be flagged?
19. Are files supposed to be merged or kept separate?

## Data handling
20. Does the dataset contain confidential, regulated, or sensitive personal/business information that changes how it must be handled?
21. Do you have the right and authorization to provide this data for processing?
22. Is enrichment or external lookup requested? If yes, describe the authorized source and permitted use. Foremanly will not scrape or infer personal data without clear authorization and a legitimate source/license.

## Delivery
23. What is the required deadline?
24. Are there acceptance checks the finished file must pass?
25. Who should decide unresolved or ambiguous cases?

## Foremanly default
Unless specifically agreed otherwise, Foremanly Systems will preserve the original source file unchanged, work on a copy, apply only bounded and explainable corrections, flag ambiguous cases, and deliver the cleaned file with a concise quality report and change/exception documentation.
