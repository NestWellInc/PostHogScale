# Foremanly Systems — Post-Purchase Intake Runbook

Purpose: turn a paid Shopify service order into a safely scoped data-quality project without guessing, uncontrolled deletion, sensitive-data mishandling, or unnecessary customer back-and-forth.

This runbook implements the canonical rules in `SERVICE_INTAKE_SPEC.md` and `service_intake_fields.csv`. It does not replace the secure intake form; it defines the order of operations and customer/project states once that form is implemented.

## State machine

### 1. PAID — INTAKE REQUIRED
Trigger: a paid order for an intentional Foremanly service SKU is received.

Required action:
- create project record keyed to Shopify order number
- send/direct buyer to the approved secure intake path
- do not request sensitive files through an unapproved channel
- do not begin work from product-description assumptions

Customer-facing instruction should communicate only: order received; intake is required before work starts; preserve/send the source only through the approved intake path; Foremanly will confirm scope before processing.

### 2. INTAKE RECEIVED — TRIAGE
Required checks before work begins:
- order number matches a paid service order
- contact email present
- file count/type/approximate dimensions within purchased scope
- requested output format known
- cleanup goal/checks known
- data authorization = Yes
- sensitive-data answer reviewed
- source file received through approved path
- deletion permission explicit
- duplicate rule present when duplicate action is requested
- destination specification present when destination-specific preparation is requested
- merge keys present when files are to be merged
- deadline can be supported without an unverified promise

### 3A. READY FOR WORK
Use only when all required intake gates pass and the project fits the purchased SKU.

Create the working record:
- Shopify order ID/number
- SKU
- received filenames
- preserved-original identifier/location
- working-copy filename(s)
- agreed checks
- duplicate rule/action
- missing-value rule
- formatting/destination rules
- row-deletion permission
- acceptance checks
- deadline
- ambiguity rule

Then preserve the original unchanged and work only from a copy.

### 3B. NEEDS CUSTOMER CLARIFICATION
Use when the project is potentially valid but a required rule is missing or ambiguous.

Examples:
- buyer requests duplicate removal but does not define a duplicate
- buyer permits deletion but gives no deterministic winner rule where competing records differ
- required output/header/date/identifier rule is unclear
- destination-specific preparation requested without destination specification
- merge requested without supplied keys

Do not make the missing decision for the buyer. Pause work and request only the minimum clarification needed.

### 3C. RESCOPE / QUOTE REQUIRED
Use when the project materially exceeds the purchased offer.

Triggers include:
- file count or row volume above stated SKU scope
- multiple unrelated datasets
- complex record merging requiring judgment
- destination mapping without supplied specification
- API/app integration
- recurring/scheduled processing
- reusable script/workflow request
- unusually complex malformed files
- substantial manual research/enrichment

Do not silently absorb excess scope. Pause and provide a bounded rescope before processing.

### 3D. HOLD — HANDLING / AUTHORIZATION REVIEW
Use when:
- `data_authorization` is No or Unsure
- `sensitive_data` is Yes or Unsure and available handling suitability has not been confirmed
- requested enrichment/source rights are unclear
- buyer asks for access-control bypass, unauthorized scraping, fabricated records, or unsupported compliance/security guarantees

Do not ask the buyer to resend sensitive data through another improvised channel. Do not process until the handling/authorization issue is resolved.

## SKU routing
- **FS-DQA-019:** diagnosis only. Deliver findings/recommended cleanup scope; do not silently perform cleanup.
- **FS-CLN-049:** one bounded file; general duplicate/missing-value/format/structure cleanup under agreed rules.
- **FS-SHP-059:** one Shopify product CSV; recheck current Shopify requirements when field behavior matters.
- **FS-CRM-059:** one contact/customer/lead CSV; no enrichment or inference of personal data.
- **FS-IMPORT-001:** one CSV against buyer-supplied destination specification; no guaranteed import acceptance.
- **FS-MULTI-099:** up to purchased multi-file scope; cross-file normalization/merge-readiness only under explicit keys/rules.

## Work-completion gate
Before marking the project complete:
- verify source original remains unchanged
- reconcile input/output dimensions
- verify every intentional row removal against the agreed rule
- confirm no missing values were invented outside an explicitly authorized deterministic rule
- rerun requested formatting/destination checks
- document unresolved ambiguity/exceptions
- confirm purchased deliverables are present

Standard service delivery bundle:
1. cleaned CSV/spreadsheet when cleanup is in scope
2. concise quality report
3. change/exception documentation

For FS-DQA-019, substitute the diagnostic findings/report for a cleaned output unless cleanup was separately purchased.

## Order/project status vocabulary
Use these exact internal states to keep concurrent workers and future automation consistent:
- `PAID_INTAKE_REQUIRED`
- `INTAKE_TRIAGE`
- `NEEDS_CLARIFICATION`
- `RESCOPE_REQUIRED`
- `HANDLING_REVIEW`
- `READY_FOR_WORK`
- `IN_PROGRESS`
- `QA_VALIDATION`
- `READY_TO_DELIVER`
- `DELIVERED`

Do not use `READY_FOR_WORK` until authorization, handling suitability, source receipt, scope, and required decision rules are all resolved.

## Publication implication
This runbook clears the missing **post-purchase operating design** portion of service readiness. It does **not** clear publication by itself. The service SKUs remain DRAFT until the secure intake path is implemented/tested, Shopify checkout/non-shipping behavior is tested, customer-facing post-purchase routing is actually configured/tested, rendered product presentation is QA'd, and the coherent Foremanly storefront/theme gate is cleared.