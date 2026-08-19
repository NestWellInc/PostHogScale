# Foremanly Systems — Shopify Prepublication QA Runbook

**Purpose:** turn the remaining browser/authenticated launch gates into one deterministic verification pass. This runbook does not authorize publication. Every intentional Foremanly SKU remains DRAFT until the applicable gates are actually tested and recorded in `foremanly/operations/PUBLICATION_READINESS.md` and `FOREMANLY_MASTER_STATE.md`.

## Preconditions
- Connected store identity must be **Foremanly Systems** and known Foremanly product IDs must resolve in that store.
- Read `FOREMANLY_MASTER_STATE.md`, `foremanly/operations/PUBLICATION_READINESS.md`, `foremanly/shopify/theme/UNPUBLISHED_PREVIEW_STATUS.md`, and `foremanly/intake/POST_PURCHASE_INTAKE_RUNBOOK.md` immediately before testing.
- Use the existing unpublished theme **Foremanly Systems — Data Quality Preview** (`gid://shopify/OnlineStoreTheme/189403922475`). Do not create another preview merely for QA.
- Do not make products ACTIVE merely to test them. Use Shopify preview/test mechanisms where available. Any real charge, paid app, subscription, upgrade, legal acceptance, KYC/tax/bank step, or irreversible publication requires owner approval.

## A. Storefront preview QA
Test desktop and mobile widths.

1. Homepage clearly positions Foremanly as CSV/spreadsheet data-quality work.
2. No contractor-era copy, contractor catalog, instant-download promise, invented review, unsupported accuracy/security/compliance claim, or guaranteed-import language appears.
3. Primary and secondary homepage CTAs resolve to intended Foremanly destinations.
4. Main navigation renders: Home; Data Services; How Data Services Work; Contact.
5. No customer-facing navigation exposes archived contractor products or duplicate experiment collections.
6. Contact and How Data Services Work pages render without stale contractor language.
7. Footer/privacy links work and do not create a dead end.
8. No empty review/testimonial section is presented as social proof.

Record: viewport tested, URL/path, PASS/FAIL, defect, correction, retest result.

## B. Service product-page QA
Apply to FS-DQA-019, FS-CLN-049, FS-SHP-059, FS-CRM-059, FS-MULTI-099, and FS-IMPORT-001.

For each SKU verify:
1. Correct title, price, SKU, file/row limit, and service scope render.
2. Product is non-shipping and does not ask the buyer for a shipping method/address solely because of product configuration.
3. Source-preservation rule is visible or clearly incorporated into the service description/process.
4. Duplicate/removal behavior is not implied to be automatic without an agreed rule.
5. Missing values are not promised to be invented or enriched by default.
6. Ambiguous cases are described as flagged/clarified rather than silently guessed.
7. Destination-specific offers avoid guaranteed-import claims.
8. Existing synthetic/process visual renders legibly and is not framed as a client result/testimonial.
9. Purchase/intake instructions point to the intended post-purchase path.
10. No physical-delivery, instant-download, subscription, or incompatible legacy language appears.

Special scope checks:
- FS-DQA-019 remains diagnostic-only; it must not imply that $19 includes cleanup.
- FS-SHP-059 does not guarantee Shopify import acceptance.
- FS-CRM-059 does not promise external enrichment unless separately authorized/scoped.
- FS-MULTI-099 does not silently merge/delete cross-file duplicate candidates without an agreed rule.
- FS-IMPORT-001 requires buyer-supplied destination rules/specification and does not guarantee destination acceptance.

## C. Service checkout and post-purchase QA
Test the flow without incurring an unauthorized real charge.

1. Cart/checkout preserves correct SKU, price, and quantity.
2. No shipping charge or irrelevant shipping step is introduced by product configuration.
3. Order/customer confirmation language does not promise unsupported turnaround, instant files, or automatic cleanup.
4. Buyer is directed to the intended secure intake route after purchase.
5. Intake can capture order matching, file(s), requested output, duplicate rule/action, required/acceptable blanks, destination specification when relevant, deletion authorization, merge key when relevant, sensitive-data/data-authorization gate, deadline, acceptance checks, and ambiguity contact.
6. File upload/storage path is suitable for the intended data sensitivity; if suitability is uncertain, sensitive-data projects remain blocked for handling review.
7. Submitted intake can be tied back to the paid order without relying on guesswork.
8. Internal routing follows `POST_PURCHASE_INTAKE_RUNBOOK.md`: Awaiting Intake → Intake Received → Needs Clarification / Needs Rescope / Handling Review / Ready for Work.
9. A $19 audit order cannot accidentally route into cleanup work without a separate authorized scope/payment.
10. Completion path can deliver the agreed output plus quality report and change/exception documentation.

## D. Digital product-page QA
Apply to FS-DIGITAL-CHECK-001 and FS-QA-PACK-012.

1. Correct title/price/SKU render.
2. Product is non-shipping.
3. Copy accurately distinguishes the $9 checklist from the fuller $12 template pack.
4. Customer-facing visual renders and does not imply a done-for-you service.
5. No claim promises error-free data, compliance, security, or guaranteed import acceptance.
6. Digital-delivery mechanism is attached to the correct SKU and correct verified package.
7. Delivery instructions are clear and do not expose internal repository paths.

Verified package identities:
- FS-DIGITAL-CHECK-001 → `Foremanly-Spreadsheet-Data-Quality-Checklist.zip` → SHA-256 `253b422fe733cf43d7fed9a6ea88a9adf8257826bc7cc4435ed586087ab590d2`
- FS-QA-PACK-012 → `Foremanly-CSV-Quality-Control-Template-Pack.zip` → SHA-256 `ddeb0732dd15ff204c7b39d0fe31268a7529abef68d3febdf4e7ddeda5d2495e`

## E. Digital delivery test
Do not clear either digital SKU until a test verifies the customer experience.

For each digital SKU:
1. Confirm the delivery mechanism is configured for the correct product/variant.
2. Use an authorized Shopify test-order/test-payment path if available; do not create a real charge without approval.
3. Verify the buyer-facing order confirmation does not require physical shipping.
4. Verify the customer receives or can access exactly one intended package.
5. Download the delivered file and confirm it opens as a ZIP.
6. Confirm package identity against the verified package name/hash when the testing environment permits hashing the delivered file.
7. Confirm no internal-only files, client data, credentials, repository metadata, or unrelated assets are present.
8. Verify retry/re-access behavior is understandable to a normal buyer.
9. Record PASS/FAIL and any defect; retest after corrections.

## F. Evidence record
For every test, record:
- date/time and tester/session
- SKU/theme/path
- device/viewport where relevant
- exact test performed
- PASS/FAIL
- observed result
- defect and correction, if any
- retest result
- screenshot/reference location if available

Do not mark a gate complete based on configuration alone. Require observed behavior.

## G. Publication clearance rule
A SKU can be marked publication-ready only when every applicable unchecked gate in `PUBLICATION_READINESS.md` has observed PASS evidence. Storefront coherence must also pass. Publication itself remains a deliberate separate action; passing QA does not automatically publish a product or theme.

If a failure is found, keep the SKU DRAFT, record the blocker in the canonical Report Queue when owner/browser action is required, fix safely reversible defects where possible, and retest. Do not loosen the gate to create artificial progress.
