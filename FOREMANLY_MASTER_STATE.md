# Foremanly Systems — Canonical Master State

**Purpose:** authoritative cross-chat operating state for Foremanly Systems. Read before material decisions; persist material verified changes.

**Parent Factory:** `FACTORY_MASTER_STATE.md`  
**Publication control:** `foremanly/operations/PUBLICATION_READINESS.md`  
**Concurrent drift log:** `foremanly/operations/CONCURRENT_DRIFT_LOG.md`  
**Shopify preview:** `foremanly/shopify/theme/UNPUBLISHED_PREVIEW_STATUS.md`  
**Portfolio index:** `foremanly/portfolio/README.md`  
**Digital package verification:** `foremanly/operations/DIGITAL_PACKAGE_VERIFICATION.md`

## Operating doctrine
**Goal:** build Foremanly Systems into a successful, profitable, durable business by the end of 2026.

Every run should complete concrete revenue-relevant or operationally durable work when available. Re-read live state before mutations because concurrent workers may have changed it. Preserve newer valid work; fix material defects rather than recreating equivalent assets.

## Company
Foremanly Systems is a CSV and spreadsheet data-quality company. Core work: identify duplicates, missing values, formatting inconsistencies, and structural problems; clean and normalize bounded CSV/spreadsheet projects; preserve the original source file unchanged; document material changes, exceptions, and unresolved ambiguity.

Standard deliverables: cleaned CSV/spreadsheet when cleanup is in scope, concise quality report, and change/exception documentation.

Positioning: **Foremanly Systems cleans and validates CSV and spreadsheet data while preserving the original source file and documenting exactly what changed.**

Hard delivery rules: work from a copy; define duplicate/removal logic before deletion; do not fabricate missing values without an explicitly authorized deterministic rule; flag ambiguity instead of guessing; use synthetic/authorized proof only; avoid unsupported accuracy, guaranteed-import, security/compliance, or business-outcome claims.

## Shopify — verified store and publication state
Last live verification: **2026-08-19 CDT**.
- Store: **Foremanly Systems**
- Shopify-reported `.myshopify.com` domain: `bqme5r-yp.myshopify.com`
- Identity guard: verify exact store name and known Foremanly product IDs before mutations; do not rely on historical domain strings alone.

Live self-healing publication check on 2026-08-19 verified **all eight intentional products are DRAFT**:
1. FS-DQA-019 — CSV Data Quality Audit — $19 — `gid://shopify/Product/8053958508587`
2. FS-CLN-049 — CSV & Spreadsheet Cleanup — $49 — `gid://shopify/Product/8053958705195`
3. FS-SHP-059 — Shopify Product CSV Preflight — $59 — `gid://shopify/Product/8053958770731`
4. FS-CRM-059 — CRM Contact CSV Cleanup — $59 — `gid://shopify/Product/8053958901803`
5. FS-MULTI-099 — Multi-File Cleanup & Normalization — $99 — `gid://shopify/Product/8053959032875`
6. FS-IMPORT-001 — Import-Ready CSV Preparation — $79 — `gid://shopify/Product/8053966995499`
7. FS-QA-PACK-012 — CSV Quality Control Template Pack — $12 — `gid://shopify/Product/8053959229483`
8. FS-DIGITAL-CHECK-001 — Spreadsheet Data Quality Checklist — $9 — `gid://shopify/Product/8053967093803`

**None is publication-cleared.** If any becomes ACTIVE without explicit readiness clearance in this file and `foremanly/operations/PUBLICATION_READINESS.md`, restore it to DRAFT immediately, verify, and log only the material regression.

Archived duplicate experiments and legacy contractor products must remain archived unless deliberately supported by new evidence.

## Product readiness
All intentional products are non-shipping. Service copy has bounded scope, source-preservation language, ambiguity/non-guarantee boundaries, and intake instructions, but services still require secure/intended intake, checkout behavior, configured/tested post-purchase routing, rendered presentation QA, and coherent storefront/theme QA before publication.

Synthetic proof already exists for multiple service lanes; search `foremanly/portfolio/README.md` and publication readiness before creating more.

## Digital products — VERIFIED PACKAGE STATE
This section supersedes older notes saying package artifacts were unverified.

### FS-DIGITAL-CHECK-001 — $9 Spreadsheet Data Quality Checklist
Canonical sources: `foremanly/checklist-product/`.
A clean customer ZIP was independently produced from canonical sources.
- Package: `Foremanly-Spreadsheet-Data-Quality-Checklist.zip`
- SHA-256: `253b422fe733cf43d7fed9a6ea88a9adf8257826bc7cc4435ed586087ab590d2`
- Package-build/existence gate: **CLEARED**

### FS-QA-PACK-012 — $12 CSV Quality Control Template Pack
Canonical sources: `foremanly/template-pack/`.
A clean seven-file customer ZIP was independently produced and ZIP-integrity tested.
- Package: `Foremanly-CSV-Quality-Control-Template-Pack.zip`
- SHA-256: `ddeb0732dd15ff204c7b39d0fe31268a7529abef68d3febdf4e7ddeda5d2495e`
- ZIP integrity: **PASS**
- Package-build/existence gate: **CLEARED**

The GitHub Actions workflow's own artifacts do not need to be treated as a publication blocker because equivalent clean packages have now been independently produced and verified. Do not waste runs repeatedly trying to prove workflow artifact existence unless the packaging workflow itself is being changed.

**Both digital products remain DRAFT / NOT CLEARED.** Remaining gates: attach/configure a reliable Shopify-compatible digital-delivery mechanism, successful test purchase/download, rendered customer-facing visual/product QA, and coherent storefront/theme QA.

## Storefront/theme
Customer-facing MAIN theme remains `gid://shopify/OnlineStoreTheme/189308469291` and historically contains contractor-era positioning/unsupported instant-download language. Do not scale traffic while that remains the live customer experience.

Canonical unpublished preview: **Foremanly Systems — Data Quality Preview**, `gid://shopify/OnlineStoreTheme/189403922475`. Reuse it; do not create another unless missing/corrupted/intentionally superseded. It remains UNPUBLISHED pending authenticated desktop/mobile visual QA, navigation/link verification, legacy-copy check, and deliberate publication decision.

## Collections/navigation
Canonical collections:
- Foremanly Data Quality Services — `gid://shopify/Collection/690943492139`
- Foremanly Data Quality Resources — `gid://shopify/Collection/690943524907`

Main menu: Home; Data Services; How Data Services Work; Contact. Generic Catalog link removed. Legacy contractor explainer page unpublished.

## Pricing ladder
$9–$12 digital self-service; $19 diagnostic audit; $49 core one-file cleanup; $59 verticalized cleanup/preflight; $79 destination-spec import-ready preparation; $99 multi-file cleanup/normalization. Larger automation/workflow work must be separately scoped; recurring maintenance only after repeat need is demonstrated.

## Commercial evidence
Historical audit: 96 online-store sessions with zero cart additions/checkouts/completed storefront checkouts, much likely setup/internal. Do not treat this as validated demand evidence. Owner-associated test orders are not external revenue.

**Verified external Foremanly revenue: $0 at this checkpoint.**

## Service intake and post-purchase operations
Implementation-ready intake specification exists at `foremanly/intake/service_intake_fields.csv` and `foremanly/intake/SERVICE_INTAKE_SPEC.md`, covering order matching, file scope, output format, duplicate rules/actions, missing values, destination specs, deletion authorization, merge keys, sensitive-data/data-authorization gates, deadline, acceptance checks, ambiguity, and file upload. Secure implementation/testing remains a launch gate.

Post-purchase operating logic is now defined at `foremanly/intake/POST_PURCHASE_INTAKE_RUNBOOK.md`. It specifies the paid-order → intake → triage → ready/clarification/rescope/handling-review state machine, SKU routing, project-record creation, completion QA, and consistent internal project statuses. This clears the missing operating-design portion of post-purchase readiness, but not the actual configured/tested customer routing gate.

## Marketplace/channel assets
Prepared core-cleanup launch assets exist for Fiverr and Upwork. Launch one focused core offer per marketplace first; do not proliferate near-duplicate listings before response evidence. TikTok is an organic education/attention lane unless current eligibility explicitly supports the exact commerce use. Secondary rails must not incur fees/subscriptions without approval.

## Metrics
Track qualified leads, quotes, jobs won, gross cash, fees, verified net cash, AOV, delivery time, revisions, repeats, source channel, Shopify funnel metrics, rows processed, duplicates/missing-value/format/structure issues, exceptions, and validation failures.

## Report Queue — human / external actions
Surface when the owner says `Report`.

1. **Authenticated visual QA + publication decision for canonical Foremanly preview — CRITICAL.** Check desktop/mobile rendering, navigation/links, legacy copy, and unsupported claims before any publish.
2. **Shopify secure service intake — HIGH.** Implement/test prepared intake schema in a suitable secure form/upload system; confirm sensitive-data suitability.
3. **Shopify digital fulfillment — HIGH.** Both customer packages are now independently verified; attach/configure delivery and perform a successful test purchase/download before either digital SKU can clear publication.
4. **Service checkout/post-purchase QA — HIGH.** Post-purchase operating runbook now exists; configure the actual customer routing/intake flow, then test purchase flow, non-shipping behavior, order matching, and customer instructions before service publication clearance.
5. **Rendered product/gallery QA — HIGH.** Reuse existing synthetic/authorized proof and inspect actual customer rendering; do not create redundant proof merely to fill time.
6. **Fiverr/Upwork authenticated publication — HIGH after core owned-store credibility gates.** Owner/browser/account verification and live platform fields remain external gates.
7. **Any KYC/tax/bank/payout, CAPTCHA, binding legal acceptance, paid listing/setup/subscription/upgrade, or spend decision — OWNER REQUIRED.**

## Immediate priorities
1. Keep all eight intentional products DRAFT until explicit SKU-level readiness clearance.
2. Complete authenticated visual QA of the canonical unpublished preview and resolve the live contractor-era homepage.
3. Implement/test secure service intake and configure/test post-purchase routing using the completed runbook.
4. Configure/test digital delivery using the already-verified $9 and $12 packages; do not repeat package-build verification work.
5. Reuse existing proof to finish rendered product-page QA.
6. Publish one focused Fiverr and one focused Upwork offer only through authenticated owner/browser flow when ready.
7. Once credible channels are live, prioritize qualified acquisition and first verified external cash over expanding the SKU count.
