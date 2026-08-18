# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating file for Foremanly Systems. Normal ChatGPT and Work/desktop sessions should read this file first, then update it whenever pricing, offers, research, blockers, priorities, compliance rules, implementation status, customer learnings, or delivery standards materially change.

**Parent Factory state:** `FACTORY_MASTER_STATE.md`
**Product/channel implementation detail:** `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`

## Company definition
Foremanly Systems is a CSV and spreadsheet data-quality company.

Core work:
- identify duplicate records
- identify missing values
- identify formatting inconsistencies
- identify structural problems
- clean and normalize CSV / spreadsheet data
- preserve the original source file unchanged
- document every material change, exception, and unresolved ambiguity

Standard deliverables:
1. cleaned CSV or spreadsheet
2. concise quality report
3. change / exception documentation

Operating principles:
- clearly defined project scope
- careful validation
- dependable communication
- reversible, auditable changes
- no silent deletion or mutation of source data
- no unsupported claims about accuracy, compliance, security, or business outcomes

## Canonical delivery workflow
1. Preserve the original source file exactly as received.
2. Create a working copy for analysis and cleanup.
3. Inspect schema, headers, row counts, encodings, delimiters, and data types.
4. Detect duplicates using explicit rules appropriate to the dataset.
5. Identify missing / null / blank values and distinguish intentional blanks from likely defects where possible.
6. Detect formatting inconsistencies such as dates, casing, whitespace, phone numbers, currency, numeric formats, booleans, and identifiers.
7. Detect structural issues such as shifted columns, malformed rows, mixed delimiters, inconsistent headers, unexpected extra fields, or broken records.
8. Apply only bounded, explainable corrections.
9. Validate post-cleaning row counts, column counts, key uniqueness, null counts, and any client-defined constraints.
10. Produce the cleaned file plus a concise quality report and a change / exception log.

## Validation standard
Every completed project should record, when applicable:
- input filename
- original row and column counts
- output row and column counts
- duplicate rule used
- duplicate count found / removed / retained
- missing-value counts by relevant column
- formatting corrections performed
- structural defects repaired
- exceptions intentionally left unchanged
- unresolved ambiguities requiring client guidance
- validation checks run after cleanup

Do not claim a dataset is "error-free" unless the scope and validation actually support that statement. Prefer precise wording such as "validated against the agreed checks."

## Productized offer architecture — implemented 2026-08-18
The connected Shopify store is `foremanlysystems.myshopify.com`.

The following products now exist as **DRAFT** products in Shopify. Draft status is intentional until fulfillment, intake, assets, images, and checkout behavior are verified.

1. **CSV Data Quality Audit — $19**
   - Shopify Product GID: `gid://shopify/Product/8053958508587`
   - SKU: `FS-DQA-019`
   - Purpose: low-friction diagnostic entry offer

2. **CSV & Spreadsheet Cleanup — $49**
   - Shopify Product GID: `gid://shopify/Product/8053958705195`
   - SKU: `FS-CLN-049`
   - Purpose: core single-file cleanup service

3. **Shopify Product CSV Preflight & Cleanup — $59**
   - Shopify Product GID: `gid://shopify/Product/8053958770731`
   - SKU: `FS-SHP-059`
   - Purpose: verticalized import-ready offer for Shopify merchants

4. **CRM Contact CSV Cleanup — $59**
   - Shopify Product GID: `gid://shopify/Product/8053958901803`
   - SKU: `FS-CRM-059`
   - Purpose: verticalized CRM/contact import cleanup with explicit privacy/authorization constraints

5. **Multi-File Cleanup & Normalization — $99**
   - Shopify Product GID: `gid://shopify/Product/8053959032875`
   - SKU: `FS-MULTI-099`
   - Purpose: higher-value multi-file normalization and merge-readiness work

6. **CSV Quality Control Template Pack — $12**
   - Shopify Product GID: `gid://shopify/Product/8053959229483`
   - SKU: `FS-QA-PACK-012`
   - Purpose: low-ticket digital toolkit / self-serve entry point
   - BLOCKER: downloadable assets must be completed and attached before publication

### Current pricing ladder
Use this as the default until conversion data supports a change:
- $12: digital toolkit entry
- $19: diagnostic audit
- $49: core single-file cleanup
- $59: vertical import-ready cleanup
- $99: multi-file cleanup / normalization
- $95+: reusable cleanup workflow or script
- $150–$300+ and higher: scoped business-data automation when complexity warrants it
- recurring maintenance: only after repeat need is demonstrated

Never silently expand file count, row volume, manual ambiguity resolution, sensitive-data requirements, or destination-specific mapping into a starter package.

## Market / product evidence — 2026-08-18
A current Shopify App Store product launched in June 2026, `MerchantCSV: CSV Import Fixer`, markets fixes for strict product-CSV import issues including boolean formatting, currency symbols, handles, duplicate rows, variant problems, row-level error reporting, and corrected CSV downloads.

Implication:
- Shopify Product CSV cleanup is a concrete merchant pain point, not a speculative niche.
- Keep `Shopify Product CSV Preflight & Cleanup` high in the commercial priority list.
- Differentiate Foremanly through preserved originals, transparent change logs, human-reviewed exceptions, and bounded one-off service scope rather than trying to compete only as recurring software.

Reference and additional channel detail are stored in `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`.

## Service architecture
### Entry service — Data Quality Audit
Best for buyers who want diagnosis before cleanup.
Potential deliverables:
- issue summary
- duplicate / missing-value findings
- formatting / structural findings
- recommended cleanup scope

### Core service — CSV / Spreadsheet Cleanup
Best for one clearly defined file or workbook.
Potential deliverables:
- cleaned file
- quality report
- change / exception log

### Vertical service — Shopify Product CSV Preflight & Cleanup
Best for merchants preparing a product CSV for Shopify import.
Potential checks:
- duplicate/inconsistent rows
- handle consistency
- variant structure
- prices/booleans/header formatting
- missing/expected values against the agreed import scope
- fields requiring merchant review

Do not guarantee Shopify import acceptance; store configuration and changing platform rules can affect results.

### Vertical service — CRM Contact CSV Cleanup
Best for legitimate buyer-supplied contact/customer/lead CSV files before an authorized CRM/contact-system import.
Potential checks:
- duplicate rules
- blank/malformed required fields
- name/email/phone/date/identifier formatting
- header and column mapping consistency

Do not scrape, enrich, infer, sell, or repurpose personal data without clear authorization and a legitimate source/license.

### Larger service — Multi-file Cleanup / Normalization
Best for multiple related files requiring consistent structure, naming, formats, or merging readiness.

### Recurring service — Data Maintenance
Offer only when a repeatable recurring need is demonstrated. Do not force recurring plans onto one-off buyers.

### Adjacent higher-value services
Pursue when scope justifies it:
- analysis-ready dataset preparation
- import-ready CSV preparation against a supplied destination specification
- workbook consolidation + validation
- recurring CSV / Excel reporting workflows
- reusable cleanup / normalization scripts
- stable-layout PDF table extraction into structured spreadsheet data
- structured-data-to-report/dashboard preparation

## Digital-product backlog
Stay tightly adjacent to Foremanly's core capability; do not create unrelated products merely to increase SKU count.

Priority backlog:
1. CSV Health Check Mini Kit — free or $0–$5 lead magnet
2. Shopify Product CSV Preflight Template Pack — $12–$19
3. CRM Import Preflight Template Pack — $12–$19
4. Inventory CSV Cleanup Pack — $12–$19
5. Multi-File Merge Readiness Kit — $19–$29
6. Reusable cleanup workflow/script — $95+ when based on a buyer's explicit rules

The existing `CSV Quality Control Template Pack` should be finished before adding several more low-ticket SKUs.

## Channel strategy — verified 2026-08-18
### Shopify — primary owned storefront
Current official Shopify guidance supports selling services and digital products. Digital downloads require appropriate fulfillment; Shopify's own Digital Downloads app can attach files or supported links. Shipping should not apply to digital/service products.

Before activating any Foremanly Shopify draft:
- configure service/digital fulfillment
- remove physical shipping where appropriate
- attach finished digital assets
- implement an intake / buyer file-upload path
- add synthetic/authorized product visuals
- test checkout and post-purchase instructions

### TikTok / TikTok Shop
Treat TikTok primarily as a **marketing and education channel**, not a default checkout rail for Foremanly.

Current U.S. TikTok Shop policy says ordinary services are prohibited and virtual/digital products require approval under the applicable Virtual Goods category; current Virtual Goods eligibility is invite-only.

Therefore:
- do not list Foremanly services in TikTok Shop under ordinary access
- do not list standalone digital template products there unless the account/product is explicitly eligible under current rules
- use organic TikTok content to drive qualified attention toward permitted storefront/service rails

Content themes:
- synthetic before/after CSV examples
- duplicate detection demos
- missing-value and formatting issue examples
- malformed row / shifted-column examples
- Shopify product-CSV preflight tips
- what a quality report contains
- preserve-the-original / audit-trail differentiation

Never expose real client data in social content.

### Fiverr — service marketplace
Priority service-marketplace channel when owner-authenticated publication is available.

Current Fiverr guidance permits responsible AI use across service categories when work is high-quality, customized, meaningfully refined, and the freelancer remains accountable. Respect explicit non-AI client requests and privacy rules.

Good Foremanly Gig directions:
- CSV / Excel cleanup and formatting
- data-quality audit
- deduplication and validation
- Shopify/import-ready CSV preparation

### Upwork Project Catalog — service marketplace
Project Catalog supports predefined, ready-to-buy service projects with scope, pricing tiers, add-ons, media, and PDF work samples; listings are reviewed before publication.

Good Foremanly Project Catalog directions:
- $19 audit
- $49 one-file cleanup
- $59 Shopify CSV cleanup
- $99 multi-file normalization

### Gumroad — secondary rail
Current Gumroad supports digital products and service-type products. Standard direct-sale fees are materially higher than Payhip/Ko-fi, and service products have restrictions.

Use mainly for:
- digital toolkit products
- bounded commission-style work only if the exact service and account remain eligible

### Payhip — preferred zero-monthly digital rail
Current Free Forever pricing is $0/month + 5% Payhip transaction fee, with processor fees additional.

Use for:
- template packs
- checklist bundles
- digital toolkits
- potentially bounded commissions after workflow validation

### Ko-fi — preferred zero-monthly shop/commission rail
Current Ko-fi Free has no monthly cost and charges 5% on Shop/Commissions, with processor fees additional. Commission terminology can be changed to Services/Bookings/Requests.

Use for:
- small digital products
- service requests
- low-friction direct-sale alternative

### Etsy — later, spend-gated
Etsy permits seller-designed digital downloads and made-to-order digital files, but currently charges listing and transaction fees and may charge a shop setup fee depending on location.

Because the Factory has a no-new-spend rule without explicit owner approval:
- prepare Etsy listing assets if useful
- do not incur listing/setup charges or publish paid listings automatically

## Customer qualification
Before accepting work, determine:
- number and type of files
- approximate rows / columns
- required output format
- exact cleanup goals
- what counts as a duplicate
- required fields / acceptable missing values
- formatting standard or destination-system specification
- whether rows may be removed or only flagged
- whether data contains regulated, confidential, or sensitive information that changes handling requirements
- deadline / turnaround requirement

If a rule cannot be inferred safely, flag it rather than inventing it.

## Quality report structure
Default sections:
- project summary
- files processed
- checks performed
- issues found
- changes made
- exceptions / unresolved items
- validation results

Prefer counts and concrete facts over vague language.

## Change / exception log structure
For each material cleanup category, record:
- issue type
- rule applied
- number of affected records / cells where feasible
- whether corrected, retained, removed, or flagged
- notes / exceptions

## Data-handling constraints
- Preserve originals.
- Do not expose or reuse client data for unrelated purposes.
- Do not fabricate records to fill missing values unless the client explicitly authorizes a deterministic fill rule.
- Do not infer sensitive personal facts to complete a dataset.
- Do not remove duplicates unless the duplicate rule is defined and defensible; when uncertain, flag suspected duplicates.
- Do not scrape or enrich personal data without clear authorization and a legitimate source / license.
- Do not bypass access controls, CAPTCHAs, platform restrictions, or authentication barriers.

## Sales positioning
Primary message:
Foremanly Systems cleans and validates CSV and spreadsheet data while preserving the original source file and documenting exactly what changed.

Differentiators:
- transparent cleanup rather than black-box transformation
- original source preservation
- documented changes and exceptions
- bounded project scope
- careful validation
- dependable communication

Avoid generic claims such as "100% accurate," "perfect data," or unsupported compliance guarantees.

## Acquisition priorities
1. Finish the current Shopify draft catalog rather than creating unrelated products.
2. Complete the downloadable assets for `CSV Quality Control Template Pack`.
3. Build synthetic before/after portfolio samples for audit, core cleanup, Shopify CSV, CRM CSV, and multi-file use cases.
4. Add a standardized intake/file-upload workflow to Shopify service products.
5. Add branded product images using synthetic or explicitly authorized data only.
6. Test Shopify checkout and post-purchase instructions while products remain Draft.
7. Prepare mirrored Fiverr and Upwork Project Catalog service listings.
8. Prepare Payhip and Ko-fi versions of the digital toolkit and bounded service requests.
9. Use TikTok organic content as a problem/solution funnel rather than assuming TikTok Shop eligibility.
10. Track channel source, leads, quotes, wins, gross cash, fees, verified net cash, delivery time, revisions, and repeat buyers.

## Business metrics to track
Commercial:
- qualified leads
- quotes sent
- jobs won
- gross cash collected
- platform / payment fees
- verified net cash
- average order value
- delivery time
- revision / rework rate
- repeat-customer rate
- source channel

Operations:
- rows processed
- duplicate records detected
- missing-value issues detected
- formatting defects corrected
- structural defects corrected
- exceptions flagged
- post-cleaning validation failures

## Automation operating rule
`Foremanly Growth Engine` is active at the maximum supported frequency: **hourly**.

The automation has been updated to use the current CSV/spreadsheet company definition and to read/update `FACTORY_MASTER_STATE.md` and `FOREMANLY_MASTER_STATE.md` when connected GitHub access is available. It prioritizes durable revenue/operations work such as productized services, digital products/templates, Shopify catalog improvement, Gumroad/Payhip/Ko-fi readiness, Fiverr/Upwork offers, TikTok/social content concepts, SEO/content, lead magnets, pricing, intake/QA/report templates, synthetic portfolio examples, SOPs, and safe connected-app updates.

A previous hourly automation named `Foremanly Research` was still focused on an older contractor-tools business model. It was disabled and renamed `Foremanly Research — Retired` on 2026-08-18 so hourly cycles are not wasted on a superseded strategy.

The Growth Engine must stop for explicit owner approval before:
- purchases or paid subscriptions
- paid ads or inventory
- Etsy/listing/setup fees or other new spend
- accepting binding legal terms
- KYC / tax / bank / payout attestations
- impersonating the owner
- publishing personal-profile facts that cannot be verified
- irreversible or high-risk external actions

When one channel is blocked, record the blocker and advance another legitimate revenue or operations path instead of generating busywork.

## Current implementation state — 2026-08-18
- Company definition established.
- Core CSV / spreadsheet data-quality scope established.
- Standard deliverables established: cleaned file + concise quality report + change / exception documentation.
- Original-source preservation is a hard delivery rule.
- Hourly Foremanly Growth Engine is active at the maximum supported automation frequency and now reflects the correct data-quality business model.
- Obsolete contractor-focused hourly Foremanly research automation has been disabled.
- Canonical GitHub state exists in `NestWellInc/PostHogScale`.
- `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md` created with detailed platform policy evidence and channel roles.
- Six Foremanly products have been created as Drafts in the connected Shopify store.
- Current platform strategy distinguishes owned storefront/service marketplaces from TikTok marketing; TikTok Shop is not assumed eligible for ordinary Foremanly services/digital products.
- No Foremanly-specific verified revenue, conversion rate, customer count, or platform traction has yet been recorded.

## Immediate next priorities
1. Build the actual downloadable assets for `CSV Quality Control Template Pack`.
2. Create reusable quality-report, change-log, intake, duplicate-rule, and validation templates.
3. Produce synthetic sample datasets and before/after portfolio examples that do not expose client data.
4. Implement Shopify service intake and digital fulfillment requirements.
5. Add product images/visuals to the six drafts.
6. Test checkout/fulfillment without activating incomplete products.
7. Prepare Fiverr and Upwork equivalents.
8. Prepare Payhip and Ko-fi mirrors for zero-monthly distribution.
9. Build a TikTok organic content queue around real CSV/spreadsheet pain points.
10. Record every material research finding and implementation result here so the next session starts from verified state.

## Cross-chat operating rule
This file is Foremanly's living source of truth.

Normal ChatGPT:
- research
- decide / refine
- improve pricing / offers / SOPs
- update this file when material
- make safe direct GitHub or connected-app changes when allowed

Work / desktop:
- read this file first
- then read `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md` when working on product/channel execution
- perform browser-only authenticated actions, uploads, publication, KYC, or supervised platform steps
- update this file with verified implementation status, URLs, blockers, and results

Both environments should avoid relying on scattered chat history when this file contains newer verified state.

## Update protocol
When materially changing this file:
- prefer verified facts over assumptions
- label estimates and hypotheses
- include live URLs / identifiers when useful
- preserve historical constraints unless intentionally superseded
- record blockers precisely
- update current priorities to reflect the newest evidence
- avoid duplicating transient chat commentary that does not affect operations
