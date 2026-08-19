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
