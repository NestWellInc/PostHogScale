# Foremanly Systems — Publication Readiness Control

**Last live verification:** 2026-08-19 CDT / 2026-08-19 UTC

Purpose: compact, current control surface for Shopify publication state. Live Shopify state remains the ultimate source of truth.

## Shopify identity guard
Connected Shopify verification identifies the shop as **Foremanly Systems**. Domain strings have differed across tool surfaces over time, so do **not** accept or reject store identity by domain alone. Require the connected shop name to be exactly `Foremanly Systems` and confirm the intentional Foremanly product IDs below resolve in that same shop before mutations.

## Rule
No intentional Foremanly product is publication-ready unless every applicable gate is explicitly verified. `ACTIVE` is not evidence of readiness. If an automation finds an intentional product ACTIVE without explicit clearance here and in `FOREMANLY_MASTER_STATE.md`, restore it to DRAFT.

## Intentional products — current live status
All eight intentional Foremanly products were live-verified as **DRAFT** on 2026-08-19.

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
- [x] connected store identity re-verified as Foremanly Systems
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
Existing evidence already attached in Shopify should be reused, not recreated:
- **FS-DQA-019:** general-cleanup synthetic proof reused only as an issue-identification illustration; audit remains diagnostic-only.
- **FS-CLN-049:** verified general-cleanup synthetic before/after proof attached.
- **FS-SHP-059:** verified Shopify product CSV preflight synthetic proof attached.
- **FS-CRM-059:** verified CRM contact cleanup synthetic proof attached.
- **FS-MULTI-099:** verified multi-file normalization synthetic proof attached.
- **FS-IMPORT-001:** bounded import-ready process illustration attached.

These assets reduce presentation gaps but do **not** clear rendered product-page QA or publication.

## Digital-product gates
### FS-DIGITAL-CHECK-001 — Spreadsheet Data Quality Checklist
- [x] distinct source deliverable exists in GitHub
- [x] product is non-shipping
- [x] clean customer ZIP independently produced and SHA-256 hashed on 2026-08-19
- [ ] digital-delivery mechanism attached/configured
- [ ] test purchase/download succeeds
- [ ] customer-facing visuals QA complete
- [ ] current storefront/homepage presentation is coherent with Foremanly positioning

Verified package: `Foremanly-Spreadsheet-Data-Quality-Checklist.zip`  
SHA-256: `253b422fe733cf43d7fed9a6ea88a9adf8257826bc7cc4435ed586087ab590d2`  
Durable verification record: `foremanly/operations/DIGITAL_PACKAGE_VERIFICATION.md`.

This clears only the package-build/existence gate for FS-DIGITAL-CHECK-001. The Shopify product remains DRAFT / NOT CLEARED.

### FS-QA-PACK-012 — CSV Quality Control Template Pack
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
A prior concurrent worker prematurely activated six service SKUs; another worker restored them to DRAFT. Future workers should check this file plus live Shopify before any product mutation and should not infer readiness from stale master-state prose.
