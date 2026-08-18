# Foremanly Systems — Product & Channel Strategy

**Last updated:** 2026-08-18

This file is a durable implementation companion to `FOREMANLY_MASTER_STATE.md`. It records current productized offers, connected-store implementation, channel-policy findings, and recommended distribution roles.

## Core commercial principle
Foremanly Systems should sell the same underlying capability in several productized forms rather than drift into unrelated physical products:

- diagnose CSV/spreadsheet quality problems
- clean and normalize bounded datasets
- prepare import-ready files for specific destination systems
- normalize multiple related files
- sell reusable QA/checklist/reporting templates
- offer recurring maintenance only after repeat need is demonstrated

Every service preserves the original source file and documents material changes, exceptions, and validation results.

## Shopify implementation — 2026-08-18
Connected store: `foremanlysystems.myshopify.com`

Six products were created as **DRAFT** so they can be refined and have fulfillment/assets configured before publication:

1. **CSV Data Quality Audit — $19**
   - Product GID: `gid://shopify/Product/8053958508587`
   - SKU: `FS-DQA-019`
   - Role: low-friction diagnostic acquisition offer

2. **CSV & Spreadsheet Cleanup — $49**
   - Product GID: `gid://shopify/Product/8053958705195`
   - SKU: `FS-CLN-049`
   - Role: core single-file cleanup service

3. **Shopify Product CSV Preflight & Cleanup — $59**
   - Product GID: `gid://shopify/Product/8053958770731`
   - SKU: `FS-SHP-059`
   - Role: verticalized import-ready offer for Shopify merchants

4. **CRM Contact CSV Cleanup — $59**
   - Product GID: `gid://shopify/Product/8053958901803`
   - SKU: `FS-CRM-059`
   - Role: verticalized contact/import cleanup offer; do not enrich/scrape personal data without authorization

5. **Multi-File Cleanup & Normalization — $99**
   - Product GID: `gid://shopify/Product/8053959032875`
   - SKU: `FS-MULTI-099`
   - Role: higher-value multi-file normalization / merge-readiness service

6. **CSV Quality Control Template Pack — $12**
   - Product GID: `gid://shopify/Product/8053959229483`
   - SKU: `FS-QA-PACK-012`
   - Role: low-ticket digital toolkit / self-serve entry point
   - BLOCKER: downloadable assets must be created and attached before publication

### Shopify publication requirements
Shopify officially supports selling both services and digital products. For digital items, use a digital-download app or supported link fulfillment; Shopify's own Digital Downloads app supports files and links. Services/digital products should be configured so shipping does not apply.

Current official references:
- https://help.shopify.com/en/manual/products/digital-service-product/selling-services-or-digital-products
- https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads

Before any draft becomes Active:
- verify service/digital fulfillment configuration
- remove physical shipping where appropriate
- attach finished digital assets to the template pack
- add intake requirements / file-upload path for service products
- add product images / portfolio visuals using synthetic or authorized data only
- test checkout and post-purchase instructions

## Market evidence — Shopify CSV pain
A Shopify App Store listing launched in June 2026, `MerchantCSV: CSV Import Fixer`, explicitly markets fixes for strict product-CSV import problems including boolean formatting, currency symbols, handles, duplicates, variants, failed-row reporting, and downloadable corrected CSVs. This validates Shopify product-CSV cleanup as a concrete merchant pain point and supports a human-reviewed Foremanly preflight/cleanup service rather than a generic spreadsheet-only pitch.

Reference:
- https://apps.shopify.com/csv-import-fixer-1

Commercial implication:
- keep **Shopify Product CSV Preflight & Cleanup** as a priority vertical offer
- differentiate on preserved originals, transparent change logs, human-reviewed exceptions, and one-off service pricing rather than competing only as recurring software

## TikTok / TikTok Shop strategy
### TikTok Shop
Do **not** list Foremanly's normal services or standalone digital template products on TikTok Shop under ordinary seller access.

Current U.S. policy states services are prohibited, and virtual/digital products are prohibited unless approved for sale under the applicable Virtual Goods category. Current Virtual Goods eligibility is invite-only.

References:
- https://seller-us.tiktok.com/university/essay?knowledge_id=1399532709988097
- https://seller-us.tiktok.com/university/essay?knowledge_id=7563407075510030

### TikTok organic content
Use TikTok primarily as an **attention and education channel** that drives qualified prospects toward Foremanly's permitted storefront/service rails.

Content themes:
- 15–30 second before/after synthetic CSV examples
- “3 reasons your CSV import fails”
- duplicate-record demos
- inconsistent date/phone/currency formatting demos
- malformed row / shifted-column examples
- Shopify product-CSV preflight tips
- “what a quality report should contain”
- preserve-the-original / audit-trail differentiation

Never expose real client data in content.

## Recommended channel roles
### Shopify — primary owned storefront
Best for:
- productized services
- digital template/toolkit products
- bundles and upsells
- organic traffic destination

### Fiverr — service marketplace
Best for:
- CSV/Excel cleanup
- data-quality audits
- deduplication / formatting
- import-ready file preparation

Current Fiverr policy allows responsible AI use across service categories when the freelancer remains accountable and the delivery is high-quality, customized, and meaningfully refined. Respect any client request for non-AI work and do not misuse personal data.

Reference:
- https://help.fiverr.com/hc/en-us/articles/37554976380177-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients

### Upwork Project Catalog — service marketplace
Best for:
- fixed-scope audit
- one-file cleanup
- Shopify CSV cleanup
- multi-file normalization

Upwork Project Catalog supports ready-to-launch predefined projects with scope, pricing tiers, add-ons, images/video, and PDF work samples. Listings are reviewed before publication.

References:
- https://support.upwork.com/hc/en-us/articles/360058234233-How-to-get-started-with-Project-Catalog-as-a-freelancer
- https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog

### Gumroad — secondary digital/service rail
Current Gumroad product types include digital products and service-type products. Current standard direct-sale fee is 10% + $0.50 plus card processing; Discover marketplace sales carry a higher fee. Service products have restrictions and should be used only where the exact Foremanly service fits current rules.

References:
- https://gumroad.com/help/article/149-adding-a-product
- https://gumroad.com/help/article/70-can-i-sell-services.html
- https://gumroad.com/help/article/66-gumroads-fees.html

Recommended Gumroad use:
- CSV Quality Control Template Pack
- future import-preflight checklists/templates
- bounded commission-style cleanup only after confirming account/service eligibility

### Payhip — preferred zero-monthly digital rail
Current Free Forever plan: $0/month + 5% Payhip transaction fee, with payment-processor fees additional. Supports digital products and commission-style offerings.

References:
- https://payhip.com/pricing
- https://payhip.com/sell-commissions

Recommended Payhip use:
- template pack
- checklists / QA worksheets
- digital bundles
- possibly clearly bounded commissions after testing the workflow

### Ko-fi — preferred zero-monthly shop/commission rail
Current Ko-fi Free: no monthly cost; 5% service fee on Shop/Commissions and processor fees additional. Commission terminology can be changed to Services/Bookings/Requests.

References:
- https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee
- https://help.ko-fi.com/hc/en-us/articles/360016170433-What-are-Ko-fi-Commissions

Recommended Ko-fi use:
- service requests
- small digital products
- low-friction direct-sale alternative

### Etsy — later digital-product discovery channel, spend-gated
Etsy permits seller-designed digital downloads and made-to-order digital files. Current listing fee is $0.20 per listing, and the transaction fee is 6.5% plus payment processing; an initial shop setup fee may also apply depending on location.

References:
- https://help.etsy.com/hc/en-us/articles/360024112614-What-Can-I-Sell-on-Etsy
- https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings
- https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy

Because the Factory has a no-new-spend rule without owner approval, do not open/publish paid Etsy listings automatically. Prepare listing assets first; request approval only when publication is otherwise ready.

## Priority product backlog
Do not create unrelated products. Highest-value next SKUs should stay tightly adjacent to real data-quality jobs:

1. **CSV Health Check Mini Kit** — free or $0–$5 lead magnet
   - checklist + issue-count worksheet
   - purpose: email/lead acquisition and service upsell

2. **Shopify Product CSV Preflight Template Pack** — $12–$19
   - checklist, field-review worksheet, error log, validation sheet
   - avoid promising platform acceptance

3. **CRM Import Preflight Template Pack** — $12–$19
   - duplicate-rule worksheet, required-field checklist, mapping sheet, exception log

4. **Inventory CSV Cleanup Pack** — $12–$19
   - SKU uniqueness, missing values, numeric/date formatting, location/quantity validation worksheets

5. **Multi-File Merge Readiness Kit** — $19–$29
   - schema comparison, header map, type map, duplicate rule, merge acceptance checklist

6. **Reusable Cleanup Workflow / Script** — $95+
   - only for a buyer's agreed rules and data structure; document assumptions and exceptions

## Pricing architecture after current research
Maintain:
- $12 digital toolkit entry
- $19 diagnostic audit
- $49 core single-file cleanup
- $59 vertical import-ready cleanup
- $99 multi-file normalization
- $95+ reusable workflow/script
- $150–$300+ scoped business-data automation when complexity warrants it
- recurring maintenance only after repeat need is demonstrated

Do not underprice by silently expanding row counts, file counts, manual ambiguity resolution, sensitive-data requirements, or destination-specific mapping into the starter price.

## Immediate next actions
1. Finish the six digital assets for `CSV Quality Control Template Pack`.
2. Build synthetic before/after portfolio samples for audit, cleanup, Shopify CSV, and multi-file use cases.
3. Add a standardized intake/file-upload workflow to Shopify service products.
4. Add clean branded product images based only on synthetic data.
5. Test Shopify checkout/fulfillment with products still in Draft.
6. Prepare mirrored Fiverr and Upwork Project Catalog listing copy using the same service ladder.
7. Prepare Payhip and Ko-fi versions of the digital toolkit and bounded service requests.
8. Use TikTok content to explain data-quality problems and drive attention to the owned storefront rather than relying on TikTok Shop eligibility.
9. Track channel source, leads, quotes, wins, gross cash, fees, verified net cash, delivery time, and revisions in the Factory ledger.

## Compliance / risk rules
- preserve source files unchanged
- never expose real client data in marketing examples
- use synthetic or explicitly authorized examples
- do not promise error-free data or guaranteed imports
- do not infer sensitive personal facts to fill missing values
- do not remove duplicates under ambiguous rules; flag them
- do not scrape/enrich personal data without clear authorization and legitimate source/licensing
- do not buy ads, subscriptions, inventory, listing fees, or upgrades without explicit owner approval
- verify current platform policy before publication because rules can change
