# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating state for Foremanly Systems. Read this file before advancing Foremanly. Update it whenever pricing, offers, research, blockers, priorities, compliance rules, implementation status, customer learnings, or delivery standards materially change.

**Parent Factory state:** `FACTORY_MASTER_STATE.md`
**Detailed product/channel research:** `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`

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

Core positioning:
**Foremanly Systems cleans and validates CSV and spreadsheet data while preserving the original source file and documenting exactly what changed.**

Differentiators:
- transparent cleanup rather than black-box transformation
- original source preservation
- documented changes and exceptions
- bounded project scope
- careful validation
- dependable communication

Avoid unsupported claims such as “100% accurate,” “perfect data,” guaranteed destination imports, unsupported security/compliance guarantees, or business-outcome guarantees.

## Canonical delivery workflow
1. Preserve the original source file exactly as received.
2. Create a working copy.
3. Inspect schema, headers, row/column counts, encodings, delimiters, and data types.
4. Define duplicate logic before removing records.
5. Identify missing/null/blank values and distinguish intentional blanks where possible.
6. Detect formatting inconsistencies including dates, casing, whitespace, phone, currency, numeric, boolean, and identifier formats.
7. Detect structural issues including shifted columns, malformed rows, mixed delimiters, inconsistent headers, unexpected extra fields, and broken records.
8. Apply only bounded, explainable corrections.
9. Flag ambiguous cases instead of silently inventing rules.
10. Revalidate row/column counts, key uniqueness, null counts, formatting, and client-defined constraints.
11. Deliver the cleaned file, concise quality report, and change/exception log.

## Validation standard
Record when applicable:
- input filename
- original and output row/column counts
- duplicate rule used
- duplicates found / removed / retained / flagged
- missing-value counts by relevant column
- formatting corrections
- structural repairs
- exceptions intentionally left unchanged
- unresolved ambiguities
- post-cleaning validation checks

Prefer “validated against the agreed checks” over claiming a dataset is universally error-free.

## Data-handling constraints
- Preserve originals.
- Do not expose or reuse client data for unrelated purposes.
- Do not fabricate values to fill missing data unless the client authorizes a deterministic rule.
- Do not infer sensitive personal facts.
- Do not remove duplicates under ambiguous rules; flag suspected duplicates.
- Do not scrape/enrich personal data without clear authorization and a legitimate source/license.
- Do not bypass access controls, CAPTCHAs, platform restrictions, or authentication barriers.
- Marketing examples must use synthetic or explicitly authorized data.

## Customer qualification
Before accepting work, determine:
- number and type of files
- approximate rows / columns
- required output format
- cleanup goal
- duplicate definition and removal/flagging rules
- required fields / acceptable missing values
- formatting standard or destination-system specification
- whether rows may be removed or only flagged
- confidentiality/sensitivity requirements
- deadline
- acceptance checks

If a rule cannot be inferred safely, flag it instead of inventing it.

## Shopify implementation — 2026-08-18
Connected store: `foremanlysystems.myshopify.com`

Six products exist as **DRAFT** products. Draft status is intentional until fulfillment, intake, images, and checkout behavior are verified.

1. **CSV Data Quality Audit — $19**
   - GID: `gid://shopify/Product/8053958508587`
   - SKU: `FS-DQA-019`
   - diagnostic acquisition offer

2. **CSV & Spreadsheet Cleanup — $49**
   - GID: `gid://shopify/Product/8053958705195`
   - SKU: `FS-CLN-049`
   - core single-file cleanup

3. **Shopify Product CSV Preflight & Cleanup — $59**
   - GID: `gid://shopify/Product/8053958770731`
   - SKU: `FS-SHP-059`
   - Shopify merchant import-preflight vertical

4. **CRM Contact CSV Cleanup — $59**
   - GID: `gid://shopify/Product/8053958901803`
   - SKU: `FS-CRM-059`
   - authorized CRM/contact import cleanup vertical

5. **Multi-File Cleanup & Normalization — $99**
   - GID: `gid://shopify/Product/8053959032875`
   - SKU: `FS-MULTI-099`
   - multi-file normalization / merge-readiness

6. **CSV Quality Control Template Pack — $12**
   - GID: `gid://shopify/Product/8053959229483`
   - SKU: `FS-QA-PACK-012`
   - digital toolkit / self-serve entry

### Current pricing ladder
- $12: digital toolkit
- $19: diagnostic audit
- $49: core one-file cleanup
- $59: destination/vertical import-ready cleanup
- $99: multi-file cleanup / normalization
- $95+: reusable cleanup workflow/script
- $150–$300+ and higher: scoped business-data automation
- recurring maintenance only after repeat need is demonstrated

Do not silently absorb larger file counts, row volume, ambiguity resolution, destination mapping, or sensitive-data requirements into starter pricing.

## CSV Quality Control Template Pack — asset status
The first sellable asset set has now been created in GitHub under:
`foremanly/template-pack/`

Files:
- `README.md`
- `data_quality_audit_checklist.csv`
- `quality_report_template.md`
- `change_exception_log.csv`
- `duplicate_rule_worksheet.csv`
- `validation_checklist.csv`
- `intake_scope_questionnaire.md`

These assets encode Foremanly's preserve-original, explicit-rules, documented-changes, ambiguity-flagging, and validation workflow.

**Remaining blockers before Shopify publication:**
- package the customer-facing files into a clean downloadable bundle, ideally ZIP plus any convenient spreadsheet/PDF representations
- attach the bundle through Shopify digital fulfillment
- remove physical shipping for the digital product
- confirm customer-facing instructions and licensing/usage copy
- test purchase/download flow
- add synthetic/authorized product visuals

Do not recreate the core templates unless a QA pass identifies a real deficiency.

## Market evidence
A Shopify App Store product launched in June 2026, `MerchantCSV: CSV Import Fixer`, markets fixes for import-breaking product CSV problems including booleans, currency symbols, handles, duplicates, variants, failed-row reporting, and corrected CSV downloads.

Implication:
- Shopify product-CSV cleanup is a concrete merchant pain point.
- Keep `Shopify Product CSV Preflight & Cleanup` high priority.
- Differentiate with preserved originals, transparent change logs, human-reviewed exceptions, and bounded one-off service work rather than competing only as recurring software.

Detailed sources are recorded in `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`.

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

### TikTok / TikTok Shop
Use TikTok primarily as an organic education/attention channel.

Current U.S. TikTok Shop rules prohibit ordinary services and require applicable approval for virtual/digital products; current Virtual Goods eligibility is invite-only. Therefore do not assume Foremanly services or templates can be sold through TikTok Shop.

Organic content themes:
- synthetic before/after CSV examples
- duplicate demos
- missing-value and formatting examples
- malformed row / shifted-column examples
- Shopify product CSV preflight tips
- what a quality report contains
- preserve-the-original / audit-trail differentiation

Never expose real client data.

### Fiverr
Priority service marketplace when owner-authenticated publication is available.
Current policy allows responsible AI-assisted work when customized, high-quality, meaningfully refined, and freelancer-accountable. Respect explicit non-AI requests and privacy rules.

### Upwork Project Catalog
Suitable for predefined service versions of the $19 / $49 / $59 / $99 ladder. Listings are reviewed before publication.

### Payhip
Current Free Forever: $0/month + 5% Payhip transaction fee, processor fees additional. Preferred zero-monthly digital-product rail.

### Ko-fi
Current Free: no monthly cost; 5% on Shop/Commissions plus processor fees. Suitable for small digital products and service requests.

### Gumroad
Supports digital and service-type products. Current direct-sale fees are materially higher than Payhip/Ko-fi and service restrictions apply. Secondary rail.

### Etsy
Supports seller-designed digital downloads and made-to-order digital files but has listing/transaction fees and may have a setup fee. Because Factory spending requires approval, prepare assets only; do not incur Etsy charges automatically.

## Digital-product backlog
Do not proliferate unrelated SKUs. Highest-fit future products:
1. CSV Health Check Mini Kit — free or $0–$5
2. Shopify Product CSV Preflight Template Pack — $12–$19
3. CRM Import Preflight Template Pack — $12–$19
4. Inventory CSV Cleanup Pack — $12–$19
5. Multi-File Merge Readiness Kit — $19–$29
6. Buyer-specific reusable cleanup workflow/script — $95+

Finish/package/publish the existing template pack before adding several more low-ticket SKUs.

## Quality report default sections
- project summary
- files processed
- checks performed
- issues found
- changes made
- exceptions / unresolved items
- validation results

Prefer concrete counts over vague language.

## Change / exception log default fields
- issue type
- rule applied
- affected record/cell count where feasible
- corrected / retained / removed / flagged
- notes / exceptions

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

Operations:
- rows processed
- duplicates detected
- missing-value issues detected
- formatting defects corrected
- structural defects corrected
- exceptions flagged
- validation failures

## Automation state
`Foremanly Growth Engine` is active **hourly**, the maximum supported automation frequency.

Its current mandate uses the CSV/spreadsheet data-quality company definition and prioritizes productized services, digital products/templates, Shopify catalog improvement, Payhip/Ko-fi/Gumroad readiness, Fiverr/Upwork offers, TikTok/social content concepts, SEO/content, lead magnets, pricing, intake/QA/report assets, synthetic portfolio examples, SOPs, and safe connected-app updates. When GitHub access is available it should read/update `FACTORY_MASTER_STATE.md` and this file after material changes.

The obsolete contractor-focused `Foremanly Research` hourly automation was disabled and renamed `Foremanly Research — Retired` on 2026-08-18.

The Growth Engine must stop for owner approval before:
- purchases, paid subscriptions, paid ads, inventory, listing/setup fees, or upgrades
- binding legal terms
- KYC / tax / bank / payout attestations
- impersonation or unverifiable personal-profile claims
- irreversible/high-risk external actions

When blocked on one channel, advance another legitimate revenue/operations path rather than generating busywork.

## Current implementation state — 2026-08-18
- Core company and delivery standards established.
- Original-source preservation is a hard rule.
- Connected Foremanly Shopify store verified.
- Six draft Shopify products created.
- Product/channel strategy file created and committed.
- Core CSV Quality Control Template Pack assets created in GitHub.
- Hourly Growth Engine corrected to the current business model.
- Obsolete contractor-focused research automation retired.
- TikTok separated into marketing vs. Shop eligibility to prevent policy mismatch.
- No Foremanly-specific verified revenue, conversion rate, customer count, or platform traction recorded yet.

## Immediate priorities
1. QA and package `foremanly/template-pack/` into the customer-facing digital bundle.
2. Attach/configure the digital bundle in Shopify and remove physical shipping.
3. Build standardized service intake/file-upload flow using the existing intake questionnaire.
4. Create synthetic before/after portfolio examples for audit, general cleanup, Shopify CSV, CRM CSV, and multi-file work.
5. Add synthetic/authorized product visuals to all six Shopify drafts.
6. Test Shopify checkout, intake, fulfillment, and post-purchase instructions while drafts remain unpublished.
7. Prepare mirrored Fiverr and Upwork Project Catalog listings.
8. Prepare Payhip and Ko-fi mirrors for the digital toolkit/service requests.
9. Build a TikTok organic content queue around real CSV/spreadsheet pain points.
10. Track leads, wins, cash, fees, delivery time, revisions, and source channel.

## Cross-chat operating rule
Normal ChatGPT:
- research, decide, refine, update state, and make safe connected-app changes

Work / desktop:
- read `FACTORY_MASTER_STATE.md`, then this file, then `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md` when relevant
- handle browser-only authenticated actions, uploads, publication, KYC, and supervised platform steps
- update these files with verified URLs, blockers, implementation status, and cash results

Use these canonical files instead of reconstructing state from scattered chats.

## Update protocol
- prefer verified facts over assumptions
- label estimates/hypotheses
- include identifiers/URLs when useful
- preserve hard constraints unless intentionally superseded
- record blockers precisely
- update priorities to reflect current evidence
- do not duplicate transient commentary that does not affect operations
