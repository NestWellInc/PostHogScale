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

## Live service catalog changed concurrently
A later Shopify reconciliation found six Foremanly service products became `ACTIVE` and published around `2026-08-19T00:25:20Z`–`00:25:23Z`:
- CSV Data Quality Audit — $19
- CSV & Spreadsheet Cleanup — $49
- Shopify Product CSV Preflight — $59
- CRM Contact CSV Cleanup — $59
- Multi-File Cleanup & Normalization — $99
- Import-Ready CSV Preparation — $79

QA on those live service variants found:
- `requiresShipping: false`
- inventory tracking off
- bounded row/file scopes in descriptions
- source-preservation language
- email intake instructions
- sensitive-data warning
- no universal-accuracy/import guarantee
- product SEO titles/descriptions already populated

Do not roll these activations back merely because earlier state called them drafts. Re-check live state before any future status mutation.

The two digital-download products remain `DRAFT` and non-shipping while download fulfillment is unfinished:
- CSV Quality Control Template Pack — $12
- Spreadsheet Data Quality Checklist — $9

## Staged Foremanly review theme
- Theme: `Foremanly Systems - Ready for Review`
- GID: `gid://shopify/OnlineStoreTheme/189403594795`
- Role: `UNPUBLISHED`
- Processing: false
- Processing failure: false

The staged homepage was successfully replaced through Shopify Admin GraphQL and then schema-QA'd against the actual Liquid sections.

### QA defect found and fixed
The first staged pass still had hidden contractor-era content in the `hero-proof` empty-image fallback (`Estimate`, `Margin clarity`, `Jobs and cashflow`, `Changes and operations`). That fallback and its schema defaults were replaced with data-quality language:
- Audit — Duplicates and gaps
- Clean — Explainable corrections
- Validate — Counts and rules

The homepage process section now supplies explicit Foremanly data-quality settings rather than inheriting old delivery defaults.

The empty customer-review section was removed from the homepage until genuine eligible reviews exist. The reusable verified-review section remains available for later use.

### Post-fix Shopify verification
`templates/index.json`:
- Shopify MD5: `7ff4896e5df13df47260fa421f92f32e`
- size: 4454 bytes
- updatedAt: `2026-08-19T00:28:21Z`
- order: hero → process → confidence → FAQ
- target heading: `Clean data. Documented changes. Original preserved.`

`sections/hero-proof.liquid`:
- Shopify MD5: `c411af76cb0d2605df2904962cb7ee70`
- size: 3091 bytes
- updatedAt: `2026-08-19T00:28:21Z`
- no contractor fallback/default copy remains in this staged section

## Dependency QA passed
The staged homepage references section/block/settings structures that exist in the duplicated theme. Verified section files include:
- `sections/hero-proof.liquid`
- `sections/verification-strip.liquid`
- `sections/shopping-confidence.liquid`
- `sections/faq.liquid`

Both homepage CTA targets are published:
- `/pages/how-data-services-work` — `CSV & Spreadsheet Data Services — Foremanly Systems`
- `/pages/contact` — `Contact Foremanly Systems`

## GitHub source synchronized
The staged Shopify changes are mirrored in the repo so another worker does not reintroduce the first-pass defects:
- `foremanly/shopify/theme/templates/index.json`
- `foremanly/shopify/theme/sections/hero-proof.liquid`
- `foremanly/shopify/theme/README.md`

## Remaining gate
Do not automatically claim the homepage is live. The customer-facing MAIN theme is still the legacy theme.

Next theme step: human/browser visual preview of the **unpublished** `Foremanly Systems - Ready for Review` theme, checking desktop/mobile rendering and navigation, followed by deliberate publication only if that review passes.

If another worker sees this file and the theme GID still exists as UNPUBLISHED, do not create another duplicate theme. Improve or QA this staged theme instead.
