# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating state for Foremanly Systems. Read this file before advancing Foremanly and update it after material changes.

**Parent Factory:** `FACTORY_MASTER_STATE.md`  
**Detailed channel research:** `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`

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
Verified live through the Shopify connector on 2026-08-18:
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

### Archived duplicate experiments
- `gid://shopify/Product/8053966536747` — duplicate audit
- `gid://shopify/Product/8053966635051` — overlapping cleanup
- `gid://shopify/Product/8053966798891` — duplicate multi-file offer
- `gid://shopify/Product/8053967290411` — overlapping QA toolkit

Do not reactivate without evidence.

### Collections
- **Foremanly Data Quality Services** — `gid://shopify/Collection/690943492139` — contains the six service drafts: $19 audit, $49 cleanup, $59 Shopify CSV, $59 CRM CSV, $99 multi-file, and $79 import-ready preparation.
- **Foremanly Data Quality Resources** — `gid://shopify/Collection/690943524907` — contains the $12 template pack and $9 checklist.

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
A 2026-08-18 live audit found 96 online-store sessions in the prior 30 days with zero cart additions, zero checkout starts, and zero completed checkouts. Treat catalog coherence, trust, intake/fulfillment readiness, visuals, and path-to-purchase as the immediate bottleneck before scaling traffic.

Prior paid/fulfilled Shopify orders associated with the owner must not be counted as external Foremanly revenue unless separately verified.

## Digital asset status
Core template source assets exist under `foremanly/template-pack/`:
- `README.md`
- `data_quality_audit_checklist.csv`
- `quality_report_template.md`
- `change_exception_log.csv`
- `duplicate_rule_worksheet.csv`
- `validation_checklist.csv`
- `intake_scope_questionnaire.md`

Before selling digital products:
- package customer-facing downloads
- configure digital fulfillment
- remove physical shipping where appropriate
- finalize buyer instructions/licensing copy
- test purchase/download flow
- add synthetic/authorized visuals

Do not add more overlapping low-ticket SKUs until these are sellable.

## Channel strategy — verified 2026-08-18
### Shopify
Primary owned storefront for services and digital products.

### TikTok / TikTok Shop
Use TikTok primarily for organic education/attention. Current U.S. TikTok Shop rules do not permit ordinary service listings. Virtual/digital goods require applicable Virtual Goods approval and current eligibility is invite-only. Do not list Foremanly services in TikTok Shop or assume ordinary seller access can sell Foremanly downloads. Reconsider only if the account receives applicable approval and the exact product meets current rules.

Organic themes: synthetic before/after CSV examples, duplicates, missing values, formatting, malformed rows, Shopify CSV preflight, quality-report education, and preserve-the-original/audit-trail positioning. Never expose client data.

### Etsy
Use only for Foremanly-designed digital downloads/templates where current rules fit. General Foremanly cleanup services are not the Etsy lane. Spend approval is required before fee-incurring setup/listings.

### Gumroad / Payhip / Ko-fi
Use as secondary digital/service rails when current terms and account eligibility fit. Payhip is especially suitable for digital products and related product types; Gumroad supports digital and service-type products subject to current restrictions; Ko-fi is a candidate for digital products and bounded service requests. Do not incur new paid plans or fees without approval.

### Fiverr / Upwork Project Catalog
Prepare predefined service versions of the $19 / $49 / $59 / $79 / $99 ladder when owner-authenticated publication is available. Respect current AI, privacy, profile, communication, and payment rules.

## Product backlog
Stay adjacent to real data-quality jobs:
1. CSV Health Check Mini Kit — free/$0–$5 lead magnet
2. Shopify Product CSV Preflight Template Pack — $12–$19
3. CRM Import Preflight Template Pack — $12–$19
4. Inventory CSV Cleanup Pack — $12–$19
5. Multi-File Merge Readiness Kit — $19–$29
6. buyer-specific reusable cleanup workflow/script — $95+

Do not expand the catalog until current drafts have clear fulfillment and positioning.

## Metrics
Track qualified leads, quotes, jobs won, gross cash, fees, verified net cash, average order value, delivery time, revisions, repeat customers, source channel, Shopify funnel metrics, rows processed, duplicates found, missing-value issues, formatting defects, structural repairs, exceptions, and validation failures.

## Automation
`Foremanly Growth Engine` is enabled **hourly**, the maximum supported frequency.

Every run should:
- read `FACTORY_MASTER_STATE.md` and this file when GitHub is available
- verify the Shopify connection is Foremanly Systems before mutations
- prioritize revenue, catalog quality, checkout/intake/fulfillment readiness, durable assets, pricing, portfolio examples, legitimate distribution, and safe reversible connected-app work
- update canonical state after material verified changes
- use fresh platform research when rules may have changed

`Foremanly Research — Retired` remains disabled because it targeted the obsolete contractor-tools model.

Hard approval gates: purchases, ads, subscriptions, inventory, listing/setup fees, binding legal terms, KYC/tax/bank/payout attestations, impersonation/unverifiable profile claims, and irreversible/high-risk actions.

## Current implementation state — 2026-08-18
- Correct Foremanly Shopify store verified live.
- Eight intentional Foremanly draft products exist.
- Four overlapping experiments are archived.
- All eight drafts are organized into the two Foremanly collections.
- Core digital template source assets exist in GitHub.
- TikTok is separated into organic acquisition vs. Shop eligibility.
- Etsy is a digital-download lane only and remains spend-gated.
- Gumroad, Payhip, Ko-fi, Fiverr, and Upwork remain secondary candidates subject to current rules/account checks.
- Hourly Growth Engine is active at the maximum supported frequency.
- No verified external Foremanly revenue or conversion has been recorded.

## Immediate priorities
1. Package template/checklist assets into customer-facing downloads.
2. Configure digital/service fulfillment and non-shipping behavior in Shopify.
3. Build standardized service intake/file-upload flow.
4. Create synthetic before/after portfolio examples for each service lane.
5. Add synthetic/authorized visuals to the eight drafts.
6. QA every product page for scope clarity, trust, buyer instructions, and unsupported claims.
7. Test Shopify checkout, intake, fulfillment, and post-purchase instructions while drafts remain unpublished.
8. Prepare mirrored Fiverr/Upwork services and Payhip/Ko-fi/Gumroad digital listings where no paid gate is triggered.
9. Build a TikTok organic content queue; do not depend on TikTok Shop.
10. Track leads, cash, fees, delivery time, revisions, source channel, and storefront funnel metrics.
11. Do not create more overlapping Shopify SKUs until these eight have clear fulfillment and positioning.

## Cross-chat rule
Normal ChatGPT: research, decide, refine, update state, and make safe connected-app changes.

Work / desktop: read `FACTORY_MASTER_STATE.md`, then this file, then `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`; handle browser-only authenticated actions, uploads, publication, KYC, and supervised platform steps; then write verified results back to canonical state.
