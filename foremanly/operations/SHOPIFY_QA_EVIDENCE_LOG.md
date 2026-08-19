# Foremanly Systems — Shopify QA Evidence Log

**Purpose:** durable observed-evidence ledger for the prepublication QA runbook. This file prevents configuration assumptions, duplicate testing, and false publication clearance.

**Authority:** `FOREMANLY_MASTER_STATE.md`, `foremanly/operations/PUBLICATION_READINESS.md`, and `foremanly/operations/SHOPIFY_PREPUBLICATION_QA_RUNBOOK.md` remain the control documents. A PASS here is evidence for a gate; it does not publish anything.

## Evidence standard
Record only tests that were actually observed. Do not mark PASS from configuration, intended behavior, prior prose, or an unverified claim from another worker.

For each test record:
- observed_at
- tester/session label
- object (theme/SKU/path)
- device/viewport when relevant
- runbook section + test number
- result: PASS / FAIL / BLOCKED / NOT_APPLICABLE
- observed behavior
- defect/correction when applicable
- retest result
- evidence reference (screenshot, Shopify object ID, GitHub path, or other durable reference)

## Current authenticated-access checkpoint — 2026-08-19
A scheduled worker attempted a fresh Shopify catalog verification before mutation. The connected Shopify tool required interactive user input/authentication in the non-interactive run, so no live Shopify status was asserted and no Shopify mutation was attempted.

Result: **BLOCKED — interactive Shopify authentication required for fresh live verification in this session.**

This does not supersede the last verified canonical state. It also does not clear or fail any product readiness gate. All intentional SKUs remain governed by the canonical DRAFT / NOT CLEARED rule until fresh authenticated evidence says otherwise.

## Storefront preview QA
| Observed at | Object | Viewport | Test | Result | Observed behavior | Defect/correction | Retest | Evidence |
|---|---|---|---|---|---|---|---|---|

## Service product-page QA
| Observed at | SKU | Viewport | Test | Result | Observed behavior | Defect/correction | Retest | Evidence |
|---|---|---|---|---|---|---|---|---|

## Service checkout / post-purchase QA
| Observed at | SKU | Test | Result | Observed behavior | Defect/correction | Retest | Evidence |
|---|---|---|---|---|---|---|---|

## Digital product-page QA
| Observed at | SKU | Viewport | Test | Result | Observed behavior | Defect/correction | Retest | Evidence |
|---|---|---|---|---|---|---|---|---|

## Digital delivery QA
| Observed at | SKU | Test | Result | Observed behavior | Defect/correction | Retest | Evidence |
|---|---|---|---|---|---|---|---|

## Clearance rule
Do not mark a SKU publication-ready until every applicable gate has observed PASS evidence and storefront coherence has passed. BLOCKED tests stay open. Publication remains a separate deliberate action after clearance.
