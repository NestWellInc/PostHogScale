# Foremanly Systems — Publication Readiness Control

**Last live verification:** 2026-08-18 CDT / 2026-08-19 UTC

Purpose: compact, current control surface for Shopify publication state. This file resolves stale narrative elsewhere; live Shopify state remains the ultimate source of truth.

## Rule
No intentional Foremanly product is publication-ready unless every applicable gate below is explicitly verified. `ACTIVE` is not evidence of readiness. If an automation finds an intentional product ACTIVE without explicit clearance here and in `FOREMANLY_MASTER_STATE.md`, restore it to DRAFT.

## Intentional products — current live status
All eight intentional Foremanly products were live-verified as **DRAFT** on this checkpoint.

| SKU | Offer | Price | Status | Publication clearance |
|---|---|---:|---|---|
| FS-DQA-019 | CSV Data Quality Audit — 1 File / Up to 1,000 Rows | $19 | DRAFT | NOT CLEARED |
| FS-CLN-049 | CSV & Spreadsheet Cleanup — 1 File / Up to 5,000 Rows | $49 | DRAFT | NOT CLEARED |
| FS-SHP-059 | Shopify Product CSV Preflight — 1 File / Up to 5,000 Rows | $59 | DRAFT | NOT CLEARED |
| FS-CRM-059 | CRM Contact CSV Cleanup — 1 File / Up to 5,000 Rows | $59 | DRAFT | NOT CLEARED |
| FS-MULTI-099 | Multi-File Cleanup & Normalization — Up to 3 Files / 10,000 Rows | $99 | DRAFT | NOT CLEARED |
| FS-IMPORT-001 | Import-Ready CSV Preparation — 1 File / Up to 5,000 Rows | $79 | DRAFT | NOT CLEARED |
| FS-QA-PACK-012 | CSV Quality Control Template Pack | $12 | DRAFT | NOT CLEARED |
| FS-DIGITAL-CHECK-001 | Spreadsheet Data Quality Checklist | $9 | DRAFT | NOT CLEARED |

Archived experiments and legacy contractor products remain archived and are not publication candidates.

## Service-offer gates
Before clearing any service SKU:
- [ ] connected store identity re-verified as Foremanly Systems
- [x] bounded scope and price defined
- [x] source-preservation and ambiguity rules present
- [x] product is non-shipping
- [x] inventory tracking is not required
- [ ] secure/intended intake path implemented and tested end-to-end
- [ ] checkout behavior tested
- [ ] post-purchase instructions tested
- [ ] customer-facing visual/product presentation QA complete
- [ ] current storefront/homepage presentation is coherent with Foremanly positioning

## Per-SKU presentation evidence
### FS-CLN-049 — CSV & Spreadsheet Cleanup
A synthetic before/after proof image based on the already-verified `foremanly/portfolio/general-cleanup/` example was attached to the DRAFT Shopify product on 2026-08-18 CDT / 2026-08-19 UTC.

Verified live after attachment:
- product remains `DRAFT`
- featured image exists on Shopify CDN
- image alt text identifies it as a synthetic before-and-after CSV cleanup example
- underlying demonstration remains 11 input rows → 10 output rows, 7 columns preserved, one explicit duplicate removal, formatting normalization, and unknown values left unguessed

This reduces the presentation gap for FS-CLN-049 but **does not clear the visual gate**. Customer-facing rendered product-page QA is still required, and the other service SKUs still need appropriate non-duplicative visuals or deliberate evidence that a shared visual is sufficient.

### FS-SHP-059 — Shopify Product CSV Preflight
A synthetic before/after proof image based on the existing verified `foremanly/portfolio/shopify-product-csv/` example was attached to the DRAFT Shopify product on 2026-08-18 CDT / 2026-08-19 UTC after re-checking current Shopify Help Center product-CSV guidance.

Verified live after attachment:
- product remains `DRAFT`
- featured image exists on Shopify CDN
- alt text clearly identifies the image as a synthetic Shopify product CSV preflight example
- visual reflects the existing 4-row / 14-column demonstration: rows and columns preserved, handles/price/status/publication/default-option/tax/shipping formatting normalized under explicit scenario rules, and no titles/SKUs/vendors invented
- the visual explicitly states that import acceptance depends on the buyer file, store configuration, and current Shopify requirements

This reduces the presentation gap for FS-SHP-059 but **does not clear the visual or publication gate**. Rendered product-page QA, secure intake, checkout/post-purchase QA, and coherent storefront/theme presentation are still required.

### FS-CRM-059 — CRM Contact CSV Cleanup
A synthetic before/after proof image based on the already-verified `foremanly/portfolio/crm-contact-cleanup/` example was attached to the DRAFT Shopify product on 2026-08-18 CDT / 2026-08-19 UTC.

Verified live after attachment:
- product remains `DRAFT`
- featured image exists on Shopify CDN
- alt text identifies it as a synthetic CRM contact CSV cleanup example
- the visual matches the verified portfolio result: 12 input rows → 11 output rows, 8 columns preserved, one duplicate removed under normalized nonblank-email exact-match logic, deterministic email/phone/state/date formatting, and blank contact fields retained rather than invented
- the visual explicitly states that it is synthetic and is not client data, a testimonial, enrichment, or guaranteed CRM import acceptance

This reduces the presentation gap for FS-CRM-059 but **does not clear the visual or publication gate**. Rendered product-page QA, secure intake, checkout/post-purchase QA, and coherent storefront/theme presentation are still required.

## Digital-product gates
Before clearing either digital SKU:
- [x] distinct source deliverable exists in GitHub
- [x] product is non-shipping
- [ ] customer ZIP/package independently verified
- [ ] digital-delivery mechanism attached/configured
- [ ] test purchase/download succeeds
- [ ] customer-facing visuals QA complete
- [ ] current storefront/homepage presentation is coherent with Foremanly positioning

## Theme dependency
Use the existing unpublished theme `Foremanly Systems — Data Quality Preview` (`gid://shopify/OnlineStoreTheme/189403922475`). It remains UNPUBLISHED pending authenticated desktop/mobile visual QA. Do not create another preview unless the existing one is missing, corrupted, or deliberately superseded with documentation.

## Concurrency note
A prior concurrent worker prematurely activated six service SKUs; another worker restored them to DRAFT. See `foremanly/operations/CONCURRENT_DRIFT_LOG.md`. Future workers should check this file plus live Shopify before any product mutation and should not infer readiness from stale master-state prose.
