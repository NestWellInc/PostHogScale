# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating state for Foremanly Systems. Read this file before advancing Foremanly and update it after material changes.

**Parent Factory:** `FACTORY_MASTER_STATE.md`  
**Detailed channel research:** `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`

## Company definition
Foremanly Systems is a CSV and spreadsheet data-quality company.

Core work:
- identify duplicate records
- identify missing values
- identify formatting inconsistencies
- identify structural problems
- clean and normalize CSV / spreadsheet data
- preserve the original source file unchanged
- document material changes, exceptions, and unresolved ambiguity

Standard deliverables:
1. cleaned CSV or spreadsheet
2. concise quality report
3. change / exception documentation

Core positioning:
**Foremanly Systems cleans and validates CSV and spreadsheet data while preserving the original source file and documenting exactly what changed.**

Operating principles:
- clearly defined scope
- careful validation
- dependable communication
- reversible, auditable cleanup
- no silent source-file mutation
- no fabricated values unless the client explicitly authorizes a deterministic rule
- ambiguous duplicate/removal rules are flagged, not guessed
- marketing examples use synthetic or explicitly authorized data only
- avoid unsupported claims such as “100% accurate,” “perfect data,” guaranteed imports, or unsupported compliance/security guarantees

## Canonical delivery workflow
1. Preserve the original source exactly as received.
2. Work from a copy.
3. Inspect schema, headers, row/column counts, encodings, delimiters, and data types.
4. Define duplicate logic before removing records.
5. Identify missing/null/blank values.
6. Detect formatting inconsistencies.
7. Detect structural problems such as malformed rows, shifted columns, mixed delimiters, inconsistent headers, unexpected fields, and broken records.
8. Apply only bounded, explainable corrections.
9. Flag ambiguous cases rather than inventing rules.
10. Revalidate counts, uniqueness, missing values, formats, and client-defined constraints.
11. Deliver cleaned output + quality report + change/exception log.

## Shopify — verified connected store
Verified through the live Shopify connector on 2026-08-18.

- Store: **Foremanly Systems**
- Domain: `foremanlysystems.myshopify.com`
- Plan: Basic
- Currency: USD
- Time zone: CDT
- Country: United States

**Guardrail:** verify the connected Shopify shop is Foremanly Systems before every Shopify mutation. If another shop is connected, do not modify it.

### Current intentional DRAFT catalog
Draft status is intentional until fulfillment, intake, visuals, shipping/digital configuration, and checkout behavior are verified.

1. **CSV Data Quality Audit — $19**
   - `gid://shopify/Product/8053958508587`
   - SKU `FS-DQA-019`
   - diagnostic acquisition offer

2. **CSV & Spreadsheet Cleanup — $49**
   - `gid://shopify/Product/8053958705195`
   - SKU `FS-CLN-049`
   - core one-file cleanup

3. **Shopify Product CSV Preflight & Cleanup — $59**
   - `gid://shopify/Product/8053958770731`
   - SKU `FS-SHP-059`
   - Shopify merchant import-preflight vertical

4. **CRM Contact CSV Cleanup — $59**
   - `gid://shopify/Product/8053958901803`
   - SKU `FS-CRM-059`
   - authorized CRM/contact import-cleanup vertical

5. **Multi-File Cleanup & Normalization — $99**
   - `gid://shopify/Product/8053959032875`
   - SKU `FS-MULTI-099`
   - multi-file normalization / merge-readiness

6. **CSV Quality Control Template Pack — $12**
   - `gid://shopify/Product/8053959229483`
   - SKU `FS-QA-PACK-012`
   - digital toolkit / self-serve entry

7. **Import-Ready CSV Preparation — $79**
   - `gid://shopify/Product/8053966995499`
   - SKU `FS-IMPORT-001`
   - destination-spec import preparation using buyer-supplied requirements

8. **Spreadsheet Data Quality Checklist — $9**
   - `gid://shopify/Product/8053967093803`
   - SKU `FS-DIGITAL-CHECK-001`
   - low-friction self-service checklist / possible lead-in product

### Archived duplicate experiments
Do not reactivate unless later evidence justifies them.
- `gid://shopify/Product/8053966536747` — duplicate $19 audit experiment
- `gid://shopify/Product/8053966635051` — duplicate/overlapping $49 cleanup experiment
- `gid://shopify/Product/8053966798891` — duplicate $99 multi-file experiment
- `gid://shopify/Product/8053967290411` — overlapping QA toolkit experiment

### Collections
Existing collections created 2026-08-18:
- **Foremanly Data Quality Services** — `gid://shopify/Collection/690943492139`
- **Foremanly Data Quality Resources** — `gid://shopify/Collection/690943524907`

The original six Foremanly drafts were organized into these collections. The newer Import-Ready CSV Preparation and Spreadsheet Data Quality Checklist still need collection placement during the next catalog organization pass.

### Pricing architecture
- $9–$12 digital self-service entry
- $19 diagnostic audit
- $49 core one-file cleanup
- $59 verticalized import cleanup
- $79 general destination-spec import-ready preparation
- $99 multi-file cleanup / normalization
- $95+ reusable cleanup workflow/script
- $150–$300+ and higher for scoped business-data automation
- recurring maintenance only after repeat need is demonstrated

Do not silently absorb larger file counts, row volume, ambiguity resolution, destination mapping, or sensitive-data requirements into starter pricing.

### Storefront evidence / bottleneck
A prior live audit on 2026-08-18 found 96 online-store sessions in the preceding 30 days with zero cart additions, zero checkout starts, and zero completed checkouts. Treat this as evidence that catalog coherence, trust, fulfillment/intake readiness, visuals, and path-to-purchase should be fixed before trying to scale traffic.

Two paid/fulfilled Shopify orders in prior history were associated with the owner and must not be counted as external Foremanly revenue unless separately verified.

## Digital asset status
Core source assets exist under `foremanly/template-pack/` in GitHub:
- `README.md`
- `data_quality_audit_checklist.csv`
- `quality_report_template.md`
- `change_exception_log.csv`
- `duplicate_rule_worksheet.csv`
- `validation_checklist.csv`
- `intake_scope_questionnaire.md`

Remaining blockers before selling the digital products:
- package the customer-facing files into a clean downloadable bundle
- configure digital fulfillment
- remove physical shipping where appropriate
- finalize customer-facing instructions/licensing copy
- test purchase/download flow
- add synthetic/authorized visuals

Do not create more overlapping low-ticket template SKUs until the existing assets are packaged and sellable.

## Channel strategy — verified 2026-08-18
### Shopify
Primary owned storefront for productized services and digital products.

Before activating drafts:
- configure service/digital fulfillment
- remove shipping where appropriate
- add intake/file-upload instructions
- attach digital assets
- add synthetic/authorized visuals
- test checkout and post-purchase instructions
- ensure the eight intentional Foremanly offers are clearly separated from legacy Factory inventory

### TikTok / TikTok Shop
Use TikTok primarily as an organic education/attention channel.

Current U.S. TikTok Shop rules do not permit ordinary service listings. Virtual/digital goods require applicable Virtual Goods approval, and current eligibility is invite-only. Therefore:
- do not list Foremanly cleanup services in TikTok Shop
- do not assume ordinary seller access can sell Foremanly digital downloads in TikTok Shop
- only reconsider digital Shop listings if the Foremanly account is explicitly approved for the applicable virtual-goods category and the exact product meets current rules
- use organic TikTok content to drive qualified prospects toward permitted Foremanly sales rails

Good organic TikTok themes:
- synthetic before/after CSV examples
- duplicate demos
- missing-value and formatting examples
- malformed-row / shifted-column examples
- Shopify product CSV preflight tips
- what a useful quality report contains
- preserve-the-original / audit-trail differentiation

Never expose real client data.

### Etsy
Suitable for Foremanly-designed digital downloads/templates. General services are not ordinarily allowed. Etsy remains spend-gated because listing/setup/payment fees can apply; prepare assets first and do not incur fees without owner approval.

### Gumroad
Supports digital products and service-type/commission products under current rules, subject to account eligibility/restrictions. Secondary rail for Foremanly templates and possibly bounded commissions.

### Payhip
Supports digital products and other product types including subscriptions/coaching. Strong candidate for template/checklist mirrors and other bounded products with no need to make TikTok Shop the commerce layer.

### Ko-fi
Candidate zero-monthly shop/commission rail for small digital products and bounded service requests, subject to current terms and processor fees.

### Fiverr / Upwork Project Catalog
Prepare predefined versions of the $19 / $49 / $59 / $79 / $99 service ladder when owner-authenticated publication is available. Respect current platform rules, privacy requirements, AI-use rules, and on-platform communication/payment requirements.

## Product backlog
Stay tightly adjacent to real data-quality jobs:
1. CSV Health Check Mini Kit — free or $0–$5 lead magnet
2. Shopify Product CSV Preflight Template Pack — $12–$19
3. CRM Import Preflight Template Pack — $12–$19
4. Inventory CSV Cleanup Pack — $12–$19
5. Multi-File Merge Readiness Kit — $19–$29
6. buyer-specific reusable cleanup workflow/script — $95+

Do not expand the catalog until current drafts have clear fulfillment and positioning.

## Metrics
Commercial:
- qualified leads
- quotes sent
- jobs won
- gross cash
- platform/payment fees
- verified net cash
- average order value
- delivery time
- revisions/rework
- repeat customers
- source channel
- Shopify sessions/cart/checkout/completed-checkout funnel

Operations:
- rows processed
- duplicates detected
- missing-value issues detected
- formatting defects corrected
- structural defects corrected
- exceptions flagged
- validation failures

## Automation state
`Foremanly Growth Engine` is enabled **hourly**, the maximum supported automation frequency.

Its mandate is the current CSV/spreadsheet data-quality company definition. It should:
- read `FACTORY_MASTER_STATE.md` and this file before material decisions when GitHub is available
- verify the connected Shopify shop is Foremanly Systems before Shopify mutations
- prioritize revenue, checkout/intake/fulfillment readiness, durable assets, product/catalog quality, legitimate distribution, pricing, SOPs, portfolio examples, and safe reversible connected-app changes
- update canonical state after material verified changes
- use fresh platform research when policies may have changed

`Foremanly Research — Retired` is disabled because it targeted the obsolete contractor-tools model.

Hard approval gates:
- purchases, ads, subscriptions, inventory, listing/setup fees, or upgrades
- binding legal terms
- KYC / tax / bank / payout attestations
- impersonation or unverifiable personal-profile claims
- irreversible/high-risk external actions

When blocked on one channel, advance another legitimate revenue/operations path instead of producing busywork.

## Current implementation state — 2026-08-18
- Correct Foremanly Shopify connection verified live.
- Eight intentional Foremanly draft products exist after catalog consolidation.
- Four overlapping product experiments are archived.
- Two Foremanly collections exist; the newest two drafts still need collection placement.
- Core digital template source assets exist in GitHub.
- TikTok separated into organic acquisition vs. Shop eligibility to prevent policy violations.
- Etsy is digital-product-only for this strategy and remains spend-gated.
- Gumroad, Payhip, Ko-fi, Fiverr, and Upwork remain secondary channel candidates subject to current account/policy checks.
- Hourly Growth Engine is active at the maximum supported frequency.
- No verified external Foremanly revenue or conversion has been recorded.

## Immediate priorities
1. Package the existing template/checklist assets into customer-facing downloads.
2. Configure digital/service fulfillment and non-shipping behavior in Shopify.
3. Build the standardized service intake/file-upload flow from the existing questionnaire.
4. Create synthetic before/after portfolio examples for audit, general cleanup, Shopify CSV, CRM CSV, import-ready CSV, and multi-file work.
5. Add synthetic/authorized product visuals to the eight intentional drafts.
6. Add the newer $79 import-ready service and $9 checklist to the appropriate Foremanly collections.
7. QA every product page for scope clarity, trust, buyer instructions, and absence of unsupported claims.
8. Test Shopify checkout, intake, fulfillment, and post-purchase instructions while drafts remain unpublished.
9. Prepare mirrored Fiverr / Upwork service listings and Payhip / Ko-fi / Gumroad digital-product listings where no paid gate is triggered.
10. Build a TikTok organic content queue around CSV/spreadsheet pain points; do not depend on TikTok Shop.
11. Track leads, wins, cash, fees, delivery time, revisions, source channel, and storefront funnel metrics.
12. Do not create more overlapping Shopify SKUs until these eight have clear fulfillment and positioning.

## Cross-chat rule
Normal ChatGPT: research, decide, refine, update state, and make safe connected-app changes.

Work / desktop: read `FACTORY_MASTER_STATE.md`, then this file, then `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`; handle browser-only authenticated actions, uploads, publication, KYC, and supervised platform steps; then write verified status back to canonical state.

Use these files instead of reconstructing state from scattered chat history.
