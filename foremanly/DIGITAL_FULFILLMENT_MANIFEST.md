# Foremanly Systems — Digital Fulfillment Manifest

**Purpose:** Canonical packaging map for Foremanly's current digital Shopify products. Use this file when creating download bundles or configuring a digital-delivery app. Do not add customer files to a product unless this manifest is intentionally updated.

## Product 1 — Spreadsheet Data Quality Checklist
- Shopify product: `Spreadsheet Data Quality Checklist`
- Product GID: `gid://shopify/Product/8053967093803`
- SKU: `FS-DIGITAL-CHECK-001`
- Current price: `$9`
- Intended format: digital download; no physical shipment

### Customer files
1. `foremanly/template-pack/CHECKLIST_README.md`
2. `foremanly/template-pack/data_quality_audit_checklist.csv`

### Excluded from this product
Do not include the quality-report template, change/exception log, duplicate-rule worksheet, validation worksheet, or intake/scope questionnaire. Those are reserved for the full template pack and create the upgrade distinction.

### Suggested packaged filename
`foremanly-spreadsheet-data-quality-checklist-v1.zip`

## Product 2 — CSV Quality Control Template Pack
- Shopify product: `CSV Quality Control Template Pack`
- Product GID: `gid://shopify/Product/8053959229483`
- SKU: `FS-QA-PACK-012`
- Current price: `$12`
- Intended format: digital download; no physical shipment

### Customer files
1. `foremanly/template-pack/START_HERE.md`
2. `foremanly/template-pack/data_quality_audit_checklist.csv`
3. `foremanly/template-pack/duplicate_rule_worksheet.csv`
4. `foremanly/template-pack/change_exception_log.csv`
5. `foremanly/template-pack/validation_checklist.csv`
6. `foremanly/template-pack/quality_report_template.md`
7. `foremanly/template-pack/intake_scope_questionnaire.md`

### Suggested packaged filename
`foremanly-csv-quality-control-template-pack-v1.zip`

## Pre-upload QA gate
Before attaching either product to a live digital-delivery flow:
- verify each listed file opens correctly
- verify there is no real client data, credential, internal secret, or unrelated Factory material in the customer package
- confirm filenames match this manifest
- verify the lightweight checklist package does not accidentally include full-pack files
- verify the full pack contains all seven listed customer files
- confirm both Shopify products remain non-shipping and inventory-untracked
- replace draft-only product copy that says delivery is not yet configured before publication
- test the download flow from checkout through customer access
- record the delivery app/method and successful test result in `FOREMANLY_MASTER_STATE.md`

## Publication rule
Neither digital product should be activated merely because the files exist. Publication readiness requires the package, delivery method, checkout/download flow, and customer-facing copy to be verified together.
