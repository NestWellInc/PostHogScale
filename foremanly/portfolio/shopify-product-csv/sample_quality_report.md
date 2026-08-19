# Foremanly Systems — Synthetic Shopify Product CSV Preflight Report

**Project type:** Shopify product CSV preflight and cleanup demo  
**Source:** `sample_dirty_shopify_products.csv`  
**Output:** `sample_clean_shopify_products.csv`  
**Data:** Fully synthetic demonstration data; no real merchant or client information.

## Validation basis
This demo was checked against Shopify's current product CSV guidance on 2026-08-18. The example intentionally uses a small subset of current product CSV fields so the before/after differences remain easy to audit.

Relevant current rules used for this demo:
- current product CSV headers should match Shopify's documented field names
- URL handles use letters, dashes, and numbers and cannot contain spaces
- when variant-related fields such as SKU are included, related option fields must also be supplied as required by the data dependency
- price values should be monetary numbers without currency symbols
- publication, status, tax, and shipping fields should use Shopify's documented values

## Counts
- Input data rows: **4**
- Output data rows: **4**
- Columns: **14** before and after
- Rows removed: **0**
- Columns added or removed: **0**

## Agreed demo rules
1. Preserve product titles, descriptions, vendors, types, tags, and SKUs unless a specific import-format issue requires a change.
2. Normalize URL handles to lowercase hyphenated handles.
3. Because each demo row contains a SKU and represents a single default variant, fill missing `Option1 name` and `Option1 value` with `Default Title`.
4. Normalize prices to plain numeric values with two decimals.
5. Normalize documented boolean/status fields to their target values.
6. For this synthetic merchant scenario, products with `Status=draft` must not be published on the online store.
7. For this synthetic merchant scenario, the row explicitly described and typed as a digital download does not require shipping.

Rules 6 and 7 are merchant-scenario rules for this demo, not assumptions Foremanly should silently make for a real client.

## Changes made
- URL handle corrections: **3 rows**
- Published-on-online-store corrections/normalization: **2 rows**
- Status normalization: **2 rows**
- Missing Option1 dependency filled: **1 row / 2 cells**
- Price formatting corrections: **4 rows**
- Charge-tax normalization: **1 row**
- Requires-shipping corrections/normalization: **3 rows**

## Exceptions / ambiguity handling
No source row was deleted. No title, SKU, description, vendor, type, or tag was invented or replaced.

The draft-publication and digital-shipping changes were made only because the synthetic project explicitly defines those business rules. In a real project, Foremanly would obtain or confirm those rules before changing ambiguous values.

## Post-cleaning checks
- All four rows remain present.
- All 14 source columns remain present.
- All cleaned URL handles are lowercase and hyphenated with no spaces.
- Every row with an SKU includes `Option1 name=Default Title` and `Option1 value=Default Title` for this single-variant demo.
- All prices contain plain numeric values with two decimal places.
- Status values are normalized to documented values used by the scenario.
- The synthetic digital guide is draft, unpublished, and marked as not requiring shipping under the agreed rule.

## Scope note
This is a preflight example, not a guarantee that a destination store will accept every import. Real Shopify imports can depend on the complete file, related fields, store configuration, existing products/variants, Markets, inventory locations, apps, and current platform behavior. Foremanly should validate against the buyer's actual export/template and agreed import goal before making changes.
