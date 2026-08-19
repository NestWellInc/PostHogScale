# Foremanly Systems — Marketplace Unit Economics

**Purpose:** prevent channel fees from silently destroying Foremanly's pricing ladder. This is a decision aid, not a promise that a marketplace will apply a particular fee to a future order. Re-check the live platform fee shown before publishing/accepting work.

**Checked:** 2026-08-19 against current official Upwork and Fiverr help guidance.

## Current platform facts

### Upwork
Upwork's current official guidance says the freelancer service fee can range from **0% to 15% per contract** and the exact percentage is shown before proposal/offer/contract commitment. Once a contract begins, that fee is fixed for that contract. Therefore Foremanly must not model Upwork as a guaranteed 10% channel.

Source: Upwork Help, `Learn about the Freelancer Service Fee`.

### Fiverr
Current Fiverr help material instructs sellers to factor a **20% Fiverr commission** into pricing. Because future account/order treatment must still be checked in the authenticated UI, use 20% as the conservative planning assumption for ordinary Fiverr service orders and verify before publication.

Source: Fiverr Help, current freelancer pricing guidance.

## Gross-to-net sensitivity
Excludes taxes, currency conversion, withdrawal costs, refunds, paid promotion, and any other account-specific charges.

| Buyer price | Direct / 0% fee | Upwork @ 5% | Upwork @ 10% | Upwork @ 15% | Fiverr planning @ 20% |
|---:|---:|---:|---:|---:|---:|
| $19 | $19.00 | $18.05 | $17.10 | $16.15 | $15.20 |
| $49 | $49.00 | $46.55 | $44.10 | $41.65 | $39.20 |
| $59 | $59.00 | $56.05 | $53.10 | $50.15 | $47.20 |
| $79 | $79.00 | $75.05 | $71.10 | $67.15 | $63.20 |
| $99 | $99.00 | $94.05 | $89.10 | $84.15 | $79.20 |

## Equivalent buyer price to preserve direct-store gross
If Foremanly eventually decides that a marketplace package should net approximately the same amount as its direct-store list price, the buyer-facing price would need to be approximately:

| Direct target | 5% fee | 10% fee | 15% fee | 20% fee |
|---:|---:|---:|---:|---:|
| $19 | $20.00 | $21.12 | $22.36 | $23.75 |
| $49 | $51.58 | $54.45 | $57.65 | $61.25 |
| $59 | $62.11 | $65.56 | $69.42 | $73.75 |
| $79 | $83.16 | $87.78 | $92.95 | $98.75 |
| $99 | $104.21 | $110.00 | $116.48 | $123.75 |

These are arithmetic reference points, **not automatic pricing instructions**. Marketplace search position, buyer expectations, package minimums, competition, conversion, and first-review strategy can justify different prices.

## Launch implications

1. **Do not blindly mirror Shopify pricing onto Fiverr.** At the current $19 / $49 / $99 Fiverr framework, a 20% planning commission implies only $15.20 / $39.20 / $79.20 before other costs. That may still be acceptable for initial customer acquisition, but it must be intentional rather than invisible.
2. **Do not hard-code a 10% Upwork fee.** Read the exact fee presented for the contract/project and use the 0–15% range for planning.
3. **Protect scope before raising prices.** The fastest margin leak is uncontrolled ambiguity/revisions, not merely platform fees. Preserve the existing bounded packages, buyer requirements, rescope rules, and explicit duplicate/removal logic.
4. **Measure contribution, not just gross sales.** For every external order record buyer price, marketplace fee, other direct transaction costs, delivery labor/time, revision time, refund/credit if any, and net cash.
5. **Use first orders as evidence.** Do not proliferate marketplace SKUs or pay for promotion before the first focused offer generates evidence about qualified inquiries, conversion, actual delivery time, revision load, and net cash.

## Minimum order record for channel learning
Record for each completed marketplace job:
- channel + listing/package
- buyer price
- platform fee percentage and dollar amount actually charged
- other direct transaction/withdrawal costs if applicable
- verified net cash
- delivery minutes/hours
- revision minutes/hours
- scope/rescope events
- acquisition source if known
- repeat/referral status

After at least 3 genuine external jobs on a channel, calculate realized net dollars per delivery hour and compare with direct-store work before changing the pricing ladder.

## Guardrail
Never claim these modeled nets as actual earnings. Actual fees must come from the platform's authenticated offer/contract/order details and transaction records.