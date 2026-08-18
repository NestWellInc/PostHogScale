# Foremanly Systems — Canonical Master State

**Purpose:** Authoritative cross-chat operating state for Foremanly Systems. Read this file before advancing Foremanly. Update it whenever pricing, offers, research, blockers, priorities, compliance rules, implementation status, customer learnings, delivery standards, or verified commercial results materially change.

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

## Shopify — canonical connected store
Verified 2026-08-18 through the connected Shopify app.

- Store name: **Foremanly Systems**
- Storefront identity: `foremanlysystems.myshopify.com`
- Plan: Basic
- Currency: USD
- Time zone: CDT
- Country: United States

**Safety rule:** before any Shopify mutation, verify the connected shop is Foremanly Systems. If a different shop is connected, do not modify it; switch/reauthorize first.

### Foremanly draft offer ladder
Six Foremanly products are intentionally **DRAFT** until fulfillment, intake, visuals, and checkout behavior are verified.

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
   - authorized CRM/contact import-cleanup vertical

5. **Multi-File Cleanup & Normalization — $99**
   - GID: `gid://shopify/Product/8053959032875`
   - SKU: `FS-MULTI-099`
   - multi-file normalization / merge-readiness

6. **CSV Quality Control Template Pack — $12**
   - GID: `gid://shopify/Product/8053959229483`
   - SKU: `FS-QA-PACK-012`
   - digital toolkit / self-serve entry

### Shopify collections created 2026-08-18
- **Foremanly Data Quality Services** — `gid://shopify/Collection/690943492139`
  - contains the five service drafts
- **Foremanly Data Quality Resources** — `gid://shopify/Collection/690943524907`
  - contains the $12 template-pack draft

These collections organize the Foremanly catalog without activating the draft offers.

### Live Shopify audit — 2026-08-18
Current catalog total observed: 13 products.

- 6 Foremanly draft products listed above
- 6 older contractor-spreadsheet products are still ACTIVE
- 1 older travel-compression product remains DRAFT

The active contractor products predate the current Foremanly data-quality positioning. Do **not** delete or archive them automatically because they may still belong to the broader Factory inventory. Keep Foremanly offers isolated in dedicated collections while the Factory decides whether legacy products should be retained, migrated, hidden, or separated.

Traffic / conversion audit for the prior 30 days through 2026-08-18:
- 96 online-store sessions / visitors reported
- 0 sessions with cart additions
- 0 sessions reaching checkout
- 0 sessions completing checkout
- reported storefront conversion rate: 0%

Interpretation: the immediate Shopify bottleneck is not scaling traffic. Priority should be offer presentation, catalog coherence, fulfillment/intake readiness, trust/visual assets, and a clear path to purchase before increasing acquisition effort.

Two paid/fulfilled orders exist in Shopify history (#1001 and #1002), and both list the owner as the customer. Do not count these as external Foremanly revenue unless separately verified as bona fide customer transactions.

## Current pricing architecture
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
Core asset set exists in GitHub under `foremanly/template-pack/`:
- `README.md`
- `data_quality_audit_checklist.csv`
- `quality_report_template.md`
- `change_exception_log.csv`
- `duplicate_rule_worksheet.csv`
- `validation_checklist.csv`
- `intake_scope_questionnaire.md`

These assets encode Foremanly's preserve-original, explicit-rules, documented-changes, ambiguity-flagging, and validation workflow.

Remaining blockers before Shopify publication:
- package customer-facing files into a clean downloadable bundle
- attach the bundle through appropriate digital fulfillment
- remove physical shipping where applicable
- confirm customer-facing instructions and licensing/usage copy
- test purchase/download flow
- add synthetic/authorized product visuals

Do not recreate the core templates unless QA identifies a real deficiency.

## Market evidence / positioning
Current research supports Shopify product-CSV cleanup as a concrete merchant pain point, including import-breaking booleans, currency symbols, handles, duplicates, variants, failed-row reporting, and corrected CSV downloads.

Keep `Shopify Product CSV Preflight & Cleanup` high priority and differentiate with:
- preserved originals
- transparent change logs
- human-reviewed exceptions
- bounded one-off service work
- clear preflight/validation scope

Detailed sources and channel notes remain in `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md`.

## Channel strategy
### Shopify
Primary owned storefront for productized services and digital products.

Before activating drafts:
- configure service/digital fulfillment
- remove shipping where appropriate
- add intake/file-upload instructions
- attach digital assets
- add synthetic/authorized visuals
- test checkout and post-purchase instructions
- resolve or deliberately separate legacy active catalog positioning

### TikTok / TikTok Shop
Use TikTok primarily as an organic education/attention channel unless current TikTok Shop eligibility explicitly supports the exact product.

Organic themes:
- synthetic before/after CSV examples
- duplicate demos
- missing-value and formatting examples
- malformed row / shifted-column examples
- Shopify product CSV preflight tips
- what a quality report contains
- preserve-the-original / audit-trail differentiation

Never expose real client data.

### Fiverr / Upwork
Prepare predefined versions of the $19 / $49 / $59 / $99 ladder. Respect platform rules, privacy requirements, client non-AI requests, owner-authenticated publication gates, and any current listing/category constraints.

### Payhip / Ko-fi / Gumroad
Use zero-fixed-cost or low-fixed-cost rails where current terms are compatible. Do not incur listing/setup/subscription fees without owner approval. Keep Gumroad secondary when economics or service-policy fit is worse than alternatives.

## Digital-product backlog
Do not proliferate unrelated SKUs. Highest-fit future products:
1. CSV Health Check Mini Kit — free or $0–$5
2. Shopify Product CSV Preflight Template Pack — $12–$19
3. CRM Import Preflight Template Pack — $12–$19
4. Inventory CSV Cleanup Pack — $12–$19
5. Multi-File Merge Readiness Kit — $19–$29
6. buyer-specific reusable cleanup workflow/script — $95+

Finish/package/publish the existing template pack before creating several more low-ticket SKUs.

## Quality-report default sections
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
- Shopify sessions, cart additions, checkout starts, completed checkouts

Operations:
- rows processed
- duplicates detected
- missing-value issues detected
- formatting defects corrected
- structural defects corrected
- exceptions flagged
- validation failures

## Automation state
`Foremanly Growth Engine` is active hourly, the maximum supported automation frequency.

Updated 2026-08-18 so future runs must:
- read canonical Factory/Foremanly state when GitHub is available
- verify the connected Shopify shop is Foremanly Systems before any Shopify mutation
- use safe reversible Shopify work for draft/catalog preparation
- update canonical state after material verified findings or implementation changes
- prioritize revenue, checkout/intake/fulfillment readiness, durable assets, and legitimate distribution rather than repetitive monitoring

The obsolete contractor-focused `Foremanly Research — Retired` automation remains disabled.

Hard approval gates:
- purchases, paid subscriptions, ads, inventory, listing/setup fees, or upgrades
- binding legal terms
- KYC / tax / bank / payout attestations
- impersonation or unverifiable personal-profile claims
- irreversible/high-risk external actions

When blocked on one channel, advance another legitimate revenue/operations path rather than generating busywork.

## Current implementation state — 2026-08-18
- Core company and delivery standards established.
- Original-source preservation is a hard rule.
- Correct Foremanly Shopify store verified through live connector.
- Six Foremanly draft Shopify products exist.
- Two Foremanly Shopify collections created and populated with those drafts.
- Live catalog audit identified six legacy ACTIVE contractor products and one unrelated legacy draft product.
- 30-day Shopify traffic audit found 96 sessions and zero cart/checkout activity.
- Core CSV Quality Control Template Pack assets exist in GitHub.
- Product/channel strategy file exists in GitHub.
- Hourly Growth Engine is active and now has an explicit Foremanly-Shopify connection guardrail.
- No verified external Foremanly revenue or conversion has been recorded.

## Immediate priorities
1. Package `foremanly/template-pack/` into the customer-facing digital bundle.
2. Configure digital/service fulfillment and remove physical shipping where appropriate.
3. Build standardized service intake/file-upload flow from the existing intake questionnaire.
4. Create synthetic before/after portfolio examples for audit, general cleanup, Shopify CSV, CRM CSV, and multi-file work.
5. Add synthetic/authorized product visuals to all six Foremanly drafts.
6. QA product pages for trust, scope clarity, buyer instructions, and catalog coherence.
7. Decide what to do with legacy active contractor products without deleting Factory inventory blindly.
8. Test Shopify checkout, intake, fulfillment, and post-purchase instructions while Foremanly offers remain unpublished.
9. Only after conversion path QA, activate the strongest offer(s) and begin focused distribution.
10. Prepare mirrored Fiverr / Upwork / Payhip / Ko-fi assets in parallel where no paid gate is triggered.
11. Track qualified leads, wins, cash, fees, delivery time, revisions, source channel, and storefront funnel metrics.

## Cross-chat operating rule
Normal ChatGPT:
- research, decide, refine, update state, and make safe connected-app changes

Work / desktop:
- read `FACTORY_MASTER_STATE.md`, then this file, then `FOREMANLY_PRODUCT_CHANNEL_STRATEGY.md` when relevant
- handle browser-only authenticated actions, uploads, publication, KYC, and supervised platform steps
- update canonical files with verified URLs, blockers, implementation status, and cash results

Use these canonical files instead of reconstructing state from scattered chats.

## Update protocol
- prefer verified facts over assumptions
- label estimates/hypotheses
- include identifiers/URLs when useful
- preserve hard constraints unless intentionally superseded
- record blockers precisely
- update priorities to reflect current evidence
- do not duplicate transient commentary that does not affect operations
