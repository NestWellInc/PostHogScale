# Foremanly Systems — Synthetic Portfolio Index

This directory is the canonical index for reusable Foremanly Systems portfolio demonstrations. All examples are synthetic unless explicitly documented otherwise. They may support storefront screenshots, marketplace galleries, proposals, and educational content, but must never be presented as client work, testimonials, or guaranteed outcomes.

## Current verified examples

### 1. General CSV Cleanup
Path: `foremanly/portfolio/general-cleanup/`

Demonstrates:
- duplicate detection/removal under an explicit rule
- missing-value handling without fabrication
- formatting cleanup
- preserved source
- quality report + change log

Verified summary: 11 input rows → 10 output rows; 7 columns preserved.

### 2. Shopify Product CSV Preflight
Path: `foremanly/portfolio/shopify-product-csv/`

Demonstrates:
- destination-specific CSV preflight
- import-format normalization
- field-dependency checks
- source preservation
- documented corrections and caveats

Verified summary: 4 input rows → 4 output rows; 14 columns preserved.

Maintenance requirement: re-check current Shopify CSV guidance before using this sample as technical guidance because platform fields/rules can change.

### 3. CRM Contact CSV Cleanup
Path: `foremanly/portfolio/crm-contact-cleanup/`

Demonstrates:
- normalized-email duplicate logic
- email/phone/state/date formatting
- missing-contact-field exceptions without enrichment or guessing
- preserved source
- quality report + change/exception log

Verified summary: 12 input rows → 11 output rows; 8 columns preserved; one documented duplicate removal.

### 4. Multi-File Cleanup & Normalization
Path: `foremanly/portfolio/multi-file-normalization/`

Demonstrates:
- explicit schema mapping across two differently named CSV schemas
- source provenance retained in the combined output
- deterministic email/state/date/currency normalization
- cross-file duplicate-candidate detection without unauthorized deletion or merge
- missing values retained rather than fabricated
- source preservation and documented caveats

Verified summary: 2 source files; 8 total input rows → 8 output rows; 0 silently deleted rows; one cross-file duplicate candidate retained pending an explicit resolution rule.

## Portfolio expansion rule
Do not create more examples just to increase asset count. Add a new sample only when it proves a materially different buyer use case that existing examples do not cover. The multi-file normalization lane now covers the previously identified distinct merge-readiness use case; do not create another equivalent multi-file sample without a materially different buyer requirement.

## Concurrent-agent rule
Before creating a new portfolio asset, search this index and the target path first. If another scheduled Foremanly run already created equivalent proof, QA and improve that work rather than duplicating it.
