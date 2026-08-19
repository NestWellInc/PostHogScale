# Foremanly Systems — Service Intake & Triage Specification

This document converts the Foremanly intake questionnaire into an implementation-ready workflow for Shopify, a form app, or another secure intake tool.

## Intake objective
Collect enough information before fulfillment to define the project boundary, prevent unauthorized data changes, identify sensitive-data or authorization issues, and route the order to the correct Foremanly offer or a separate quote.

The field-level implementation schema is in `service_intake_fields.csv`.

## Minimum information before work begins
Do not begin cleanup until Foremanly has:
- order or project identifier
- customer contact
- source file(s)
- file count and approximate dimensions
- desired output format
- cleanup goal / requested checks
- permission on row deletion versus flag-only handling
- duplicate rule when duplicate action is requested
- destination specification when destination-specific preparation is requested
- confirmation that the customer is authorized to provide the data
- sensitive-data answer
- deadline
- ambiguity decision rule

## Default operating rule
Unless explicitly agreed otherwise:
- preserve the original source unchanged
- work from a copy
- flag ambiguous duplicates rather than remove them
- do not invent missing values
- do not perform external enrichment
- do not delete suspect rows without an agreed rule and permission
- preserve identifiers where formatting could change their meaning
- deliver a cleaned working file, concise quality report, and change/exception documentation for service products

## Offer routing
### $19 CSV Data Quality Audit
Use when the buyer needs diagnosis only and the project is one clearly defined file. Output is findings/recommended cleanup scope; do not silently perform the $49 cleanup.

### $49 CSV & Spreadsheet Cleanup
Use for one bounded file where duplicate, missing-value, formatting, and structural rules can be agreed without destination-specific mapping complexity.

### $59 Shopify Product CSV Preflight & Cleanup
Use when the buyer is preparing a Shopify product CSV and can provide the actual source/export plus the intended import goal. Recheck current Shopify guidance before technical changes if field behavior could have changed.

### $59 CRM Contact CSV Cleanup
Use for one customer/lead/contact CSV when the customer supplies the destination field requirements or accepts a general clean/normalize scope. Do not enrich or infer personal data.

### $79 Import-Ready CSV Preparation
Use when a buyer supplies a destination-system field/import specification and wants one CSV prepared against it. Complex migrations/API work are separate scope.

### $99 Multi-File Cleanup & Normalization
Use for multiple related files where cross-file headers, formats, keys, and merge-readiness rules can be explicitly defined. File count, volume, merge keys, and destination requirements must be confirmed before fulfillment.

## Quote / rescope triggers
Do not silently absorb the following into a starter product:
- file count or row volume materially beyond the product's stated/expected starter scope
- multiple unrelated datasets
- unclear or conflicting duplicate rules
- complex record merging requiring judgment
- destination mapping without a supplied specification
- app/API integration
- recurring scheduled processing
- reusable scripts/workflows
- unusually complex malformed files
- substantial manual research or enrichment
- sensitive/regulated data requiring handling commitments Foremanly has not explicitly established
- deadline that cannot be supported without an unverified promise

When triggered, pause fulfillment and provide a bounded rescope or separate quote rather than degrading quality.

## Hard-stop / owner-review triggers
Do not process when:
- customer says they do not have the right to provide the data
- authorization is unclear and cannot be resolved
- requested work requires bypassing access controls, CAPTCHA, authentication, platform restrictions, or anti-bot controls
- requested enrichment requires unauthorized scraping, purchased/stolen data, or inference of sensitive personal facts
- the customer requests fabricated records or unsupported compliance/security guarantees
- a platform/project explicitly prohibits the proposed AI/automation method

## Sensitive-data handling gate
If `sensitive_data=Yes` or `Unsure`, do not tell the buyer to upload/send the file until Foremanly has confirmed that the project is suitable for the available handling method. Record the blocker rather than improvising a security claim.

## Intake validation logic
- `file_count >= 1`
- source file upload required
- destination specification required when destination-specific mapping is requested
- duplicate definition required when duplicate review/removal is requested
- duplicate winner/merge rule required when conflicting duplicate records may be merged or removed by preference
- merge keys required when multiple files will be merged
- enrichment source/use required when enrichment is requested
- `data_authorization` must be `Yes` before work starts
- row deletion requires explicit `Yes under agreed rules`

## Project record created after intake
Create/record:
- project/order ID
- received filenames
- preserved-original identifiers
- working-copy filenames
- agreed checks
- duplicate rule
- missing-value rule
- formatting/destination rules
- deletion permission
- acceptance checks
- deadline
- unresolved pre-work questions

## Completion gate
Before delivery verify:
- source original remains unchanged
- input/output dimensions reconciled
- every intentional row removal is supported by the agreed rule
- missing values were not invented outside an explicit rule
- requested formatting/destination checks were rerun
- exceptions/ambiguity are documented
- standard deliverables match the purchased scope

## Implementation note
A future Shopify/form implementation should reproduce these fields and conditional rules, not merely provide a generic file-upload box. The goal is to reduce back-and-forth while preventing silent assumptions and uncontrolled scope expansion.
