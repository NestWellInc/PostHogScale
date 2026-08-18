# Foremanly Systems — Canonical Master State

**Purpose:** This is the authoritative cross-chat operating file for Foremanly Systems. Normal ChatGPT and Work/desktop sessions should read this file first before advancing Foremanly, then update it whenever pricing, offers, research, blockers, priorities, compliance rules, implementation status, customer learnings, or delivery standards materially change.

**Parent Factory state:** `FACTORY_MASTER_STATE.md`

## Company definition
Foremanly Systems is a data-quality services company focused on CSV and spreadsheet projects.

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

## Service architecture
Keep scope bounded and easy to understand.

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

## Pricing logic
Use the parent Factory's economic ladder as a reference until Foremanly-specific conversion data supports changes:
- low-cost audit / bounded starter: approximately $15–$25
- structured cleanup / normalization: approximately $35–$60+
- multi-file or more complex data processing: approximately $80–$125+
- reusable scripts / cleanup workflows: approximately $95+
- scoped business-data automation: approximately $150–$300+ and higher where complexity warrants it
- recurring maintenance: only when repeat need is proven

Never silently expand a starter package to absorb a much larger project.

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
Keep reports concise and useful. Default sections:
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

Differentiators to reinforce:
- transparent cleanup rather than black-box transformation
- original source preservation
- documented changes and exceptions
- bounded project scope
- careful validation
- dependable communication

Avoid generic claims such as "100% accurate," "perfect data," or unsupported compliance guarantees.

## Current acquisition priorities
1. Make the offer easy to buy with a bounded starter service.
2. Build proof through transparent before/after examples using synthetic or authorized sample data.
3. Maintain reusable delivery templates for quality reports and change logs.
4. Publish to legitimate low-fixed-cost channels where terms permit data-cleanup services.
5. Use current-platform rules before posting or automating outreach.
6. Qualify inquiries into audit, single-file cleanup, multi-file normalization, reusable workflow, or recurring maintenance.
7. Track leads, quotes, wins, delivery time, revision rate, and repeat buyers so pricing can be evidence-driven.

## Business metrics to track
Minimum commercial metrics:
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

Minimum operations metrics:
- rows processed
- duplicate records detected
- missing-value issues detected
- formatting defects corrected
- structural defects corrected
- exceptions flagged
- post-cleaning validation failures

## Automation operating rule
The scheduled Foremanly Growth Engine may advance research, positioning, offer design, templates, SOPs, prospect research, channel research, pricing analysis, and other reversible business-development work.

It may update this file or related GitHub records when connected tools safely permit it.

It must stop for explicit owner approval before:
- purchases or paid subscriptions
- accepting binding legal terms
- KYC / tax / bank / payout attestations
- impersonating the owner
- publishing personal-profile facts that cannot be verified
- irreversible or high-risk external actions

When one channel is blocked, record the blocker and advance another legitimate revenue or operations path instead of generating busywork.

## Cross-chat operating rule
This file is Foremanly's living source of truth.

Normal ChatGPT:
- research
- decide / refine
- improve pricing / offers / SOPs
- update this file when material
- make direct GitHub or connected-app changes when allowed

Work / desktop:
- read this file first
- perform browser-only authenticated actions, uploads, publication, KYC, or supervised platform steps
- update this file with verified implementation status, URLs, blockers, and results

Both environments should avoid relying on scattered chat history when this file contains a newer verified state.

## Current implementation state — 2026-08-18
- Company definition established.
- Core CSV / spreadsheet data-quality scope established.
- Standard deliverables established: cleaned file + concise quality report + change / exception documentation.
- Original-source preservation is a hard delivery rule.
- Hourly Foremanly Growth Engine automation is active at the maximum supported automation frequency.
- Canonical GitHub state file created in `NestWellInc/PostHogScale` to prevent fragmented handoffs.
- No Foremanly-specific verified revenue, conversion rate, customer count, or platform traction has yet been recorded in this file.

## Immediate next priorities
1. Create reusable quality-report and change-log templates.
2. Create a standardized intake / scope questionnaire.
3. Build a deterministic CSV cleanup QA checklist and acceptance criteria.
4. Produce synthetic sample datasets and before/after portfolio examples that do not expose client data.
5. Establish a lead / quote / revenue tracker dedicated to Foremanly.
6. Validate current acquisition channels and package pricing against live market/platform conditions before publication.
7. Record every material research finding and implementation result here so the next session starts from verified state.

## Update protocol
When materially changing this file:
- prefer verified facts over assumptions
- label estimates and hypotheses
- include live URLs / identifiers when useful
- preserve historical constraints unless intentionally superseded
- record blockers precisely
- update current priorities to reflect the newest evidence
- avoid duplicating transient chat commentary that does not affect operations
