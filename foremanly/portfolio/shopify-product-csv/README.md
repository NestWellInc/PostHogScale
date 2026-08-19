# Foremanly Systems — Shopify Product CSV Preflight Portfolio Example

This folder is a fully synthetic demonstration of the Foremanly Systems Shopify product CSV preflight workflow. It contains no real merchant or customer information.

## Files
- `sample_dirty_shopify_products.csv` — synthetic source with import-format and rule-consistency problems
- `sample_clean_shopify_products.csv` — cleaned working copy
- `sample_quality_report.md` — rules, counts, exceptions, and post-cleaning validation
- `sample_change_log.csv` — structured change documentation

## What this demonstrates
- preserve the source and work on a copy
- validate against current destination-format guidance before changing data
- correct import-format problems without rewriting unrelated business content
- respect field dependencies when variant-related data is present
- distinguish platform-format rules from merchant-specific business rules
- document why publication/shipping decisions were changed rather than guessing
- validate the cleaned file against explicit checks

## Verified demo counts
- 4 input rows -> 4 output rows
- 14 columns before and after
- 3 URL-handle corrections
- 2 publication-value corrections/normalizations
- 2 status normalizations
- 1 row received the two missing default-option dependency cells
- 4 price-format corrections
- 1 charge-tax normalization
- 3 requires-shipping corrections/normalizations

## Approved reuse
This synthetic example may be adapted for the Foremanly Shopify storefront, Fiverr/Upwork portfolio material, proposals, social/educational content, and process explanations. Keep it clearly labeled as synthetic/demo data and do not describe it as a client result, testimonial, or proof of a guaranteed Shopify import.

## Maintenance rule
Shopify CSV fields and import behavior can change. Before using this example as technical guidance, re-check current Shopify documentation and update the sample if the platform's current field names or dependencies materially change.
