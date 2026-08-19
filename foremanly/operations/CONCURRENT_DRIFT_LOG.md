# Foremanly Systems — Concurrent Automation Drift Log

Purpose: record only material conflicts or mistakes caused by concurrent scheduled work so future runs can recognize and prevent recurrence. This is not a general activity log.

## 2026-08-18 — Premature Shopify activation corrected

### Detected state
A live Shopify verification found six intentional Foremanly service products had been changed to `ACTIVE` even though the canonical publication-readiness gates were not cleared. Digital products remained `DRAFT`.

Affected service SKUs:
- `FS-DQA-019`
- `FS-CLN-049`
- `FS-SHP-059`
- `FS-CRM-059`
- `FS-MULTI-099`
- `FS-IMPORT-001`

### Why this was drift
Foremanly's current guard requires service/digital fulfillment, intake, non-shipping/delivery behavior, visuals, and checkout QA to be verified before activation. Those readiness gates were not all cleared.

### Correction
All six affected service products were immediately restored to `DRAFT` through the connected Foremanly Shopify store, and a subsequent live catalog query verified the corrected state.

### Additional verification
The same audit verified all eight intentional Foremanly product variants have:
- `requiresShipping: false`
- inventory tracking disabled

So physical-shipping configuration was not the cause and did not require a correction.

### Prevention rule
Before any scheduled run performs other Shopify work:
1. verify the connected store is Foremanly Systems;
2. read `FOREMANLY_MASTER_STATE.md`;
3. compare intentional product status against canonical publication readiness;
4. if an intentional Foremanly product is `ACTIVE` without an explicit canonical readiness clearance, restore it to `DRAFT` before proceeding and record the drift;
5. never reactivate archived duplicate experiments without documented evidence.

Do not add routine successful actions to this file. Add only material cross-agent conflicts, regressions, or mistaken changes worth preventing in future runs.
