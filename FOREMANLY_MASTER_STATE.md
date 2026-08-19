# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating state for Foremanly Systems. Read this file before advancing Foremanly and update it after material changes.

**Parent Factory:** `FACTORY_MASTER_STATE.md`  
**Detailed channel research:** `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`

## Operating doctrine
**Goal:** build Foremanly Systems into a successful, profitable business by the end of 2026.

**ALWAYS PROGRESS:** every run must complete at least one concrete revenue-relevant or operationally durable action when one is available. Never create cosmetic churn, duplicate research, filler assets, or pretend progress. If no meaningful action can be completed, record the exact blocker or missing capability and stop.

**Quality loop:** after meaningful changes, check for mistakes, duplicated positioning, mixed legacy branding, pricing conflicts, fulfillment gaps, unsupported claims, broken assumptions, and conversion friction. Fix what can be fixed safely, then move to the next highest-value action.

**Report protocol:** maintain the persistent human/external-action queue below. When the owner personally messages `Report`, return a concise status report with verified progress, current commercial state, revenue/traction, blockers, and every pending human/external action ranked by impact.

## Company
Foremanly Systems is a CSV and spreadsheet data-quality company.

Core work:
- identify duplicates, missing values, formatting inconsistencies, and structural problems
- clean and normalize bounded CSV/spreadsheet projects
- preserve the original source file unchanged
- document material changes, exceptions, and unresolved ambiguity

Standard deliverables:
1. cleaned CSV/spreadsheet
2. concise quality report
3. change/exception documentation

Positioning:
**Foremanly Systems cleans and validates CSV and spreadsheet data while preserving the original source file and documenting exactly what changed.**

Operating rules:
- work from a copy; never silently mutate the source
- define duplicate/removal logic before deleting records
- do not fabricate missing values unless the client explicitly authorizes a deterministic rule
- flag ambiguity instead of guessing
- use synthetic or explicitly authorized data for marketing examples
- avoid unsupported “100% accurate,” guaranteed-import, compliance, security, or business-outcome claims

## Delivery workflow
1. Preserve original.
2. Inspect schema, headers, dimensions, encoding/delimiters, and data types.
3. Define duplicate rules.
4. Identify missing values.
5. Detect formatting inconsistencies.
6. Detect structural defects.
7. Apply bounded explainable corrections.
8. Flag unresolved ambiguity.
9. Revalidate counts, uniqueness, formats, missing values, and client-defined checks.
10. Deliver cleaned output + quality report + change/exception log.

## Shopify — verified connection
Verified live 2026-08-18:
- Store: **Foremanly Systems**
- Domain: `foremanlysystems.myshopify.com`
- Plan: Basic
- Currency: USD
- Time zone: CDT
- Country: United States

**Guardrail:** verify the connected shop is Foremanly Systems before every Shopify mutation.

### Intentional DRAFT catalog
Keep drafts unpublished until fulfillment, intake, visuals, non-shipping/digital configuration, and checkout behavior are verified.

1. **CSV Data Quality Audit — $19** — `gid://shopify/Product/8053958508587` — `FS-DQA-019`
2. **CSV & Spreadsheet Cleanup — $49** — `gid://shopify/Product/8053958705195` — `FS-CLN-049`
3. **Shopify Product CSV Preflight & Cleanup — $59** — `gid://shopify/Product/8053958770731` — `FS-SHP-059`
4. **CRM Contact CSV Cleanup — $59** — `gid://shopify/Product/8053958901803` — `FS-CRM-059`
5. **Multi-File Cleanup & Normalization — $99** — `gid://shopify/Product/8053959032875` — `FS-MULTI-099`
6. **CSV Quality Control Template Pack — $12** — `gid://shopify/Product/8053959229483` — `FS-QA-PACK-012`
7. **Import-Ready CSV Preparation — $79** — `gid://shopify/Product/8053966995499` — `FS-IMPORT-001`
8. **Spreadsheet Data Quality Checklist — $9** — `gid://shopify/Product/8053967093803` — `FS-DIGITAL-CHECK-001`

The $79 import-prep offer has explicit source preservation, destination-spec intake, deliverables, missing-data rules, import caveats, and separate-scope boundaries.

The $9 checklist is explicitly checklist-only; the $12 toolkit is the fuller package with report/change-log/duplicate-rule/intake assets. Do not create more overlapping low-ticket products without evidence.

### Archived catalog
Archived overlapping Foremanly experiments:
- `gid://shopify/Product/8053966536747`
- `gid://shopify/Product/8053966635051`
- `gid://shopify/Product/8053966798891`
- `gid://shopify/Product/8053967290411`

Six active contractor spreadsheet products were archived on 2026-08-18 because they conflicted with current data-quality positioning and had no verified external revenue evidence. This was reversible. Do not reactivate without evidence for a separate strategy.

### Canonical collections
- **Foremanly Data Quality Services** — `gid://shopify/Collection/690943492139` — currently linked from main navigation; six service offers
- **Foremanly Data Quality Resources** — `gid://shopify/Collection/690943524907` — two digital resources

Additional redundant/unlinked collections currently exist from earlier automation (`CSV & Spreadsheet Data Quality Services`, `Data Cleanup Services`, `CSV Quality Control Tools`, contractor collection). Do not spend time deleting backend-only duplicates unless they become customer-facing or create operational errors. Main navigation should use the canonical collections above.

### Main navigation — corrected 2026-08-18
Main menu is now verified as:
1. Home
2. Data Services → `Foremanly Data Quality Services`
3. How Data Services Work
4. Contact

The generic `Catalog` link was removed because intentional Foremanly offers remain DRAFT and the old active contractor products were archived. This prevents a likely empty/irrelevant customer path.

Footer remains Search + Shopify privacy choices.

### Published pages — audited 2026-08-18
- `Contact Foremanly Systems` — published and aligned with current intake/sensitive-data rules
- `How Foremanly Systems Data Services Work` — published and aligned with current service workflow
- Shopify `Your Privacy Choices` — published
- `Foremanly Systems Contractor Tools — What They Are & Which One Fits` — legacy page was found published and was successfully **unpublished** on 2026-08-18

### Live theme/homepage — CRITICAL verified issue
Current MAIN theme:
- theme GID: `gid://shopify/OnlineStoreTheme/189308469291`
- theme name: `projectscale-digital-systems-v1-0-1`

A direct MAIN-theme file audit found `templates/index.json` still contains contractor-era homepage positioning and unsupported instant-download claims, including a contractor-focused hero/catalog and spreadsheet-tool FAQs. This is the highest-impact remaining storefront consistency defect.

The connected Shopify mutation tool **blocks writes to live/MAIN theme files**, so it cannot be corrected directly from this chat.

Implementation-ready replacement is committed at:
- `foremanly/shopify/theme/templates/index.json`
- `foremanly/shopify/theme/README.md`

The replacement uses the live theme's existing section types; removes contractor positioning, catalog CTA, and unverified instant-download claims; centers data quality/source preservation/documented changes; and links to the existing How It Works + Contact pages.

Do not drive serious external traffic until this homepage is patched or otherwise replaced with current Foremanly positioning.

### Pricing ladder
- $9–$12 digital self-service entry
- $19 diagnostic audit
- $49 core one-file cleanup
- $59 verticalized import cleanup
- $79 destination-spec import-ready preparation
- $99 multi-file cleanup/normalization
- $95+ reusable workflow/script
- $150–$300+ scoped business-data automation when complexity warrants it
- recurring maintenance only after repeat need is demonstrated

Do not silently expand starter scope to absorb larger files, more files, heavy ambiguity resolution, destination mapping, or sensitive-data requirements.

### Storefront evidence
A 2026-08-18 live audit found 96 online-store sessions in the prior 30 days with zero cart additions, zero checkout starts, and zero completed checkouts. Much of this may be setup/internal traffic, so do not treat 0% conversion as proof the offers failed. Owner-associated paid/fulfilled orders must not be counted as external Foremanly revenue unless separately verified.

## Digital products / fulfillment assets
### $12 CSV Quality Control Template Pack
Source/customer-facing files exist under `foremanly/template-pack/`:
- `README.md`
- `data_quality_audit_checklist.csv`
- `quality_report_template.md`
- `change_exception_log.csv`
- `duplicate_rule_worksheet.csv`
- `validation_checklist.csv`
- `intake_scope_questionnaire.md`

### $9 Spreadsheet Data Quality Checklist
Customer-facing product now exists under `foremanly/checklist-product/`:
- `spreadsheet_data_quality_checklist.csv`
- `README.md`

This closes the prior gap where the $9 Shopify product had positioning but no distinct deliverable.

### Automated packaging
GitHub Actions workflow committed:
`.github/workflows/foremanly-package-digital-products.yml`

Purpose:
- build `Foremanly-Spreadsheet-Data-Quality-Checklist.zip`
- build `Foremanly-CSV-Quality-Control-Template-Pack.zip`
- generate SHA-256 checksums
- upload the package files as GitHub Actions artifacts on relevant source changes / manual dispatch

The workflow uses current GitHub-hosted action major versions verified on 2026-08-18. The connected GitHub app does not expose listing/dispatching ordinary push-triggered workflow runs, so the first successful packaging run has **not yet been independently verified** in this chat. Do not claim the ZIP artifacts exist until a run/artifact is verified.

Remaining sellability requirements:
- verify successful package workflow/artifacts or produce equivalent clean ZIPs another way
- configure Shopify digital fulfillment
- remove physical shipping where appropriate
- test purchase/download delivery
- add synthetic/authorized visuals

## Service intake system
Implementation-ready intake specification exists under `foremanly/intake/`:
- `service_intake_fields.csv`
- `SERVICE_INTAKE_SPEC.md`

It defines form-ready fields and conditional triage for order matching, file scope, output format, duplicate rules/actions, required/acceptable blanks, destination specifications, row-deletion authorization, merge keys, sensitive-data gating, data authorization, external enrichment, deadline, acceptance checks, ambiguity handling, and file upload.

It also defines routing/rescope rules for $19/$49/$59/$79/$99 services, hard-stop conditions, project-record fields, and completion gates. Future Shopify/form implementations should reproduce this logic rather than using only a generic upload box.

## Synthetic portfolio — verified 2026-08-18
### General cleanup example
Folder: `foremanly/portfolio/general-cleanup/`
Verified: 11 input rows → 10 output rows; 7 columns; one documented `C003` duplicate removal; blank-value exceptions retained; correction counts cross-checked.

### Shopify product CSV preflight example
Folder: `foremanly/portfolio/shopify-product-csv/`
Built after checking then-current official Shopify product CSV guidance. Verified: 4 input rows → 4 output rows; 14 columns; handle/publication/status/default-option/price/tax/shipping corrections documented; no unrelated business content invented.

Portfolio samples may be reused for storefront screenshots, marketplaces, proposals, and educational content only when clearly labeled synthetic/demo. Never present them as client results, testimonials, or proof of guaranteed imports.

Create additional CRM/import-ready/multi-file portfolio examples only when each adds distinct buyer proof; do not manufacture an endless sample library.

## Marketplace launch assets
Prepared and committed:
- `foremanly/marketplaces/FIVERR_CSV_CLEANUP_GIG.md`
- `foremanly/marketplaces/UPWORK_PROJECT_CATALOG_CSV_CLEANUP.md`

Both use the same bounded $19 audit / $49 cleanup / $99 multi-file core ladder, buyer requirements, preserved-source rule, ambiguity handling, synthetic gallery plan, and non-guarantee language.

Do not create many near-duplicate gigs/projects. Launch one focused core cleanup listing per marketplace first, observe response, then add verticalized offers only when evidence supports it.

## Channel strategy — verified 2026-08-18
- **Shopify:** primary owned storefront; fix live homepage and fulfillment before serious acquisition.
- **TikTok:** organic education/attention; do not assume TikTok Shop can sell ordinary services or Foremanly digital goods without applicable current eligibility.
- **Etsy:** digital-download lane only; spend approval required before fee-incurring setup/listings.
- **Gumroad / Payhip / Ko-fi:** secondary rails when current terms/account eligibility fit; do not incur new paid plans/fees without approval.
- **Fiverr / Upwork Project Catalog:** one focused core-cleanup listing prepared for each; owner-authenticated publication remains external gate.

## Metrics
Track qualified leads, quotes, jobs won, gross cash, fees, verified net cash, average order value, delivery time, revisions, repeat customers, source channel, Shopify funnel metrics, rows processed, duplicates found, missing-value issues, formatting defects, structural repairs, exceptions, and validation failures.

## Pending Human / External Actions
Surface this section when the owner says `Report`.

1. **Patch live Shopify homepage — CRITICAL / highest impact.** MAIN theme still contains contractor-era positioning and unsupported instant-download claims. Connected API cannot write MAIN theme files. Exact corrected `templates/index.json` + safe implementation sequence are in `foremanly/shopify/theme/`. Requires authenticated Shopify theme editor/browser or another tool that can safely edit the live theme. Re-check current live file before replacing because automations may change state concurrently.
2. **Shopify digital fulfillment setup — HIGH impact.** Attach/configure the $9/$12 downloadable packages and test delivery. Current connector does not expose digital-download attachment/configuration. Do not activate these products until delivery is verified.
3. **Shopify service fulfillment / secure intake — HIGH impact.** Implement the prepared `foremanly/intake/` schema in Shopify or a suitable form/upload app, configure non-shipping behavior, and test order-to-project intake. Current email intake can serve as a temporary fallback but secure handling suitability must be confirmed for sensitive data.
4. **Fiverr publication — HIGH impact after storefront credibility fix.** Use `foremanly/marketplaces/FIVERR_CSV_CLEANUP_GIG.md`; owner/browser needed for seller profile/category, any identity/tax/phone verification, gallery upload, live category fields, and final publish.
5. **Upwork Project Catalog publication — HIGH impact after storefront credibility fix.** Use `foremanly/marketplaces/UPWORK_PROJECT_CATALOG_CSV_CLEANUP.md`; owner/browser needed for profile/category/gallery, account verification, live tier fields, and submission/review.
6. **Verify GitHub packaging workflow artifacts — MEDIUM.** Workflow is committed but current connector cannot independently enumerate ordinary push-triggered runs. Verify workflow success/artifacts through GitHub Actions UI or a compatible workflow-run tool before treating generated ZIPs as fulfillment-ready.
7. **Publication gate — HIGH impact once ready.** Activate only offers whose scope, checkout, intake, fulfillment, and post-purchase flow have been tested. Any new legal/KYC/payout/tax/app-charge/paid-plan step requires owner action/approval.

Do not interrupt the owner for these during routine work; advance other legitimate work and surface them when the owner says `Report`.

## Automation
`Foremanly Growth Engine` is enabled **hourly**, the maximum supported frequency.

Every run should:
- read `FACTORY_MASTER_STATE.md` and this file when available
- verify Shopify identity before mutations
- ALWAYS PROGRESS with concrete revenue/durable operations work when available
- run the quality loop after implementation
- update canonical state after material verified changes
- add genuine owner/browser/tool blockers to `Pending Human / External Actions`
- use fresh primary platform research when rules may have changed
- stop rather than fabricate progress when nothing useful can be done

Hard approval gates: purchases, ads, subscriptions, inventory, listing/setup fees, binding legal terms, KYC/tax/bank/payout attestations, impersonation/unverifiable claims, and irreversible/high-risk actions.

## Current implementation state — 2026-08-18
- Correct Foremanly Shopify store verified live.
- Eight intentional Foremanly draft products exist; overlapping experiments and contractor products are archived.
- Canonical service/resource collections exist.
- Main menu corrected; legacy contractor page unpublished; current Contact/How It Works pages verified.
- Live homepage contractor-era theme defect verified; corrected replacement prepared in GitHub but live write is externally blocked.
- $9 checklist and $12 toolkit have distinct customer-facing source assets.
- Automated ZIP packaging workflow committed; execution/artifact verification pending.
- Service intake/form specification completed.
- Two cross-checked synthetic portfolio packages completed.
- Fiverr and Upwork core-cleanup listing frameworks completed.
- Hourly Growth Engine active with no-busywork and Report protocol.
- No verified external Foremanly revenue recorded.

## Immediate priorities
1. **Do not scale traffic until the live Shopify homepage is corrected.**
2. Verify/package the $9/$12 digital downloads and configure/test fulfillment.
3. Implement/test service intake and non-shipping behavior using the prepared schema.
4. Add synthetic/authorized product/gallery visuals that reuse existing portfolio evidence rather than generic stock art.
5. Test checkout, intake, fulfillment, and post-purchase instructions while products remain unpublished.
6. Publish one focused Fiverr core-cleanup Gig and one focused Upwork Project Catalog offer when authenticated gates are available.
7. Once the Shopify home/fulfillment path is credible, activate the smallest set of strongest offers first rather than all eight automatically.
8. Begin organic distribution/content using existing synthetic portfolio proof; do not create unrelated content inventory.
9. Track qualified leads, cash, fees, delivery time, revisions, source channel, and storefront funnel metrics.
10. Add new products/services only when evidence reveals a real demand or operational gap.

## Cross-chat rule
Normal ChatGPT: research, decide, refine, update state, and make safe connected-app changes.

Work / desktop: read `FACTORY_MASTER_STATE.md`, then this file, then `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`; handle browser-only authenticated actions, uploads, live theme editing, publication, KYC, and supervised platform steps; write verified results back to canonical state.
