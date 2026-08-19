# Foremanly Shopify Unpublished Preview Status

**Last verified:** 2026-08-18 (CDT) / 2026-08-19 UTC

## Preview theme
- Name: `Foremanly Systems — Data Quality Preview`
- Theme GID: `gid://shopify/OnlineStoreTheme/189403922475`
- Shopify role: `UNPUBLISHED`
- Processing: complete
- Processing failed: false

## Homepage patch
The corrected Foremanly homepage from:

`foremanly/shopify/theme/templates/index.json`

was written to the preview theme at:

`templates/index.json`

Shopify verification after the write:
- filename: `templates/index.json`
- content type: `application/json`
- size: 5,183 bytes
- Shopify MD5: `5c4c4bb249fe3f3d50530fda10c471c7`
- updated at: `2026-08-19T00:26:46Z`
- write user errors: none

## Safety state
The live `MAIN` theme was **not** modified or published by this operation. The preview remains unpublished intentionally.

Do not create another Foremanly preview theme unless this one is missing, corrupted, or superseded for a documented reason. Concurrent agents should reuse and QA this theme rather than duplicating it.

## Remaining gate
Before any publication:
1. visually preview the unpublished theme in an authenticated/browser-capable Shopify session;
2. confirm homepage sections render correctly and navigation/links resolve;
3. confirm no legacy contractor-era or unsupported instant-download claims remain in the rendered experience;
4. only then consider publishing the preview theme.

Publishing remains a deliberate human/publication gate and should be surfaced through the Foremanly Report Queue when the owner explicitly asks for `Report`.
