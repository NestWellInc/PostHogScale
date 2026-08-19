# Foremanly Systems — Shopify Theme Patch

## Why this exists
A live theme audit on 2026-08-18 found that the current MAIN Shopify theme still uses contractor-era homepage copy and unsupported instant-download claims even though Foremanly Systems has pivoted to CSV and spreadsheet data-quality services.

The connected Shopify API can read the MAIN theme but blocks theme-file writes to a live theme. Therefore the corrected homepage template is stored here as the implementation-ready source of truth:

`foremanly/shopify/theme/templates/index.json`

## Live issue confirmed
Current MAIN theme:
- Shopify theme GID: `gid://shopify/OnlineStoreTheme/189308469291`
- Theme name: `projectscale-digital-systems-v1-0-1`
- Live file requiring replacement: `templates/index.json`

Legacy live copy found included:
- contractor-focused hero positioning
- contractor systems/catalog language
- claims of instant downloadable-file fulfillment that is not yet configured for the current Foremanly products
- spreadsheet-tool FAQs unrelated to the current data-quality service model

## Patch objective
Replace the live `templates/index.json` with the prepared file in this folder after a browser/Work session confirms the current live file has not materially changed since the audit.

The prepared replacement:
- uses the existing live theme section types, so it does not require a theme redesign
- removes contractor positioning
- removes unsupported instant-download claims
- centers source-file preservation, explicit rules, validation, documented changes, and ambiguity handling
- links to the existing published `How Data Services Work` and `Contact Foremanly Systems` pages
- omits the catalog showcase while the intentional Foremanly products remain DRAFT
- avoids fake reviews or unsupported guarantees

## Safe implementation sequence
1. Open the live Shopify theme editor/code editor for the MAIN theme.
2. Re-read the current `templates/index.json` and compare it to the version captured in the canonical state; if another automation or human changed it materially, merge rather than overwrite blindly.
3. Replace only the homepage template with `foremanly/shopify/theme/templates/index.json` or reproduce the same settings through the theme editor.
4. Preview desktop and mobile.
5. Confirm the hero buttons resolve to `/pages/how-data-services-work` and `/pages/contact`.
6. Confirm no contractor copy, instant-download promise, accounting-tool FAQ, or dead catalog CTA remains on the homepage.
7. Save/publish the theme change only after the preview passes.
8. Update `FOREMANLY_MASTER_STATE.md` with the verified implementation state and timestamp.

## Do not do
- do not activate draft products merely to populate the homepage
- do not claim instant digital delivery until download fulfillment is actually configured and tested
- do not reintroduce contractor products into Foremanly's primary positioning without evidence and an explicit strategy decision
- do not overwrite a newer live homepage blindly if the current theme has changed since this patch was prepared
