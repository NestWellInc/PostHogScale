# Foremanly Shopify Review Theme State

**Purpose:** Small cross-worker coordination file for the Shopify theme transition. Read this before doing more homepage/theme work so concurrent automations do not duplicate effort or confuse staged changes with the live storefront.

**Verified:** 2026-08-18 CDT / 2026-08-19 UTC

## Live theme — still customer-facing
- Theme: `projectscale-digital-systems-v1-0-1`
- GID: `gid://shopify/OnlineStoreTheme/189308469291`
- Role: `MAIN`
- Processing: false
- `templates/index.json` still contains contractor-era positioning and unverified instant-download statements.
- Do **not** treat the storefront homepage as corrected until the replacement theme is deliberately published after review.

## Staged Foremanly review theme
- Theme: `Foremanly Systems - Ready for Review`
- GID: `gid://shopify/OnlineStoreTheme/189403594795`
- Role: `UNPUBLISHED`
- Processing: false
- Processing failure: false

`templates/index.json` was successfully replaced through Shopify Admin GraphQL with the Foremanly data-quality homepage prepared in this repo.

Post-write verification:
- stored file: `templates/index.json`
- Shopify MD5: `dbc3b16d64185423edaa97b28bfbaaf0`
- stored size: 3879 bytes
- Shopify updatedAt: `2026-08-19T00:24:12Z`
- target heading verified: `Clean data. Documented changes. Original preserved.`
- contractor/catalog/instant-download homepage sections are absent from the staged replacement

## Dependency QA passed
The staged theme contains every custom section referenced by the replacement homepage:
- `sections/hero-proof.liquid`
- `sections/verification-strip.liquid`
- `sections/shopping-confidence.liquid`
- `sections/verified-reviews.liquid`
- `sections/faq.liquid`

Both homepage CTA targets are published:
- `/pages/how-data-services-work` — `CSV & Spreadsheet Data Services — Foremanly Systems`
- `/pages/contact` — `Contact Foremanly Systems`

## Source of truth for homepage copy
Repo replacement:
- `foremanly/shopify/theme/templates/index.json`
- `foremanly/shopify/theme/README.md`

## Remaining gate
Do not publish automatically. The next theme step is a human/browser visual preview of the **unpublished** `Foremanly Systems - Ready for Review` theme, followed by deliberate publication only if rendering, navigation, desktop/mobile layout, and copy look correct.

If another worker sees this file and the theme GID still exists as UNPUBLISHED, do not create another duplicate theme. Improve or QA this staged theme instead.
