# Factory Autonomy Policy

**Status:** ACTIVE
**Authorized by owner:** 2026-08-23
**Purpose:** Allow the Factory to accept and execute suitable paid machine work without waiting for per-job owner approval.

## Standing authorization
The owner has granted standing approval for the Factory decision-maker to accept and execute jobs that satisfy every GREEN-GATE condition below. The owner does **not** need to approve each qualifying job individually.

This standing authorization exists because requiring owner approval per job would destroy utilization and prevent the Factory from operating as an autonomous cash engine.

## GREEN-GATE — may accept and execute autonomously
A job may be accepted without further owner approval only when all are true:
1. The requested output does not inherently require the owner's personal opinion, identity, lived experience, biometric contribution, physical presence, personal survey response, or uniquely human testimony.
2. The work can be truthfully completed by software/machines with appropriate automated QA.
3. The client/platform terms do not prohibit the proposed automation/AI/software method.
4. Acceptance does not require impersonation, fake credentials, fabricated experience, fake reviews, deceptive engagement, CAPTCHA/anti-bot bypass, KYC evasion, account-limit evasion, or undisclosed human identity substitution.
5. The input/data may lawfully and contractually be processed for the requested purpose; no unauthorized access or prohibited scraping is required.
6. The work is within a bounded, testable specification and can be validated before delivery.
7. No new spend, subscription, listing fee, bid-credit purchase, paid verification, inventory purchase, ad spend, or other cash outlay is required beyond previously approved resources.
8. No real-money trading, gambling, lending, or speculative financial risk is involved.
9. The job does not require regulated professional judgment we cannot truthfully provide (legal, medical, tax, accounting attestation, licensed engineering, etc.).
10. The expected contribution is positive after known platform fees and marginal compute/tool cost.

## Machine-first job classes
Prefer and automatically route suitable work such as:
- CSV/Excel cleanup, normalization, validation, deduplication, formatting
- deterministic file/data conversion
- structured PDF/table extraction where quality can be verified
- JSON/XML/CSV transformation
- authorized/public data extraction and permitted scraping
- catalog/product-data normalization
- spreadsheet reconciliation and comparison
- batch file operations
- structured report generation
- repeatable data pipelines and reusable scripts
- objective web research where the requested deliverable is factual/structured rather than personal opinion

## Human-specific work — do not automate as a substitute
Reject or escalate work whose value specifically depends on a real human response, including personal surveys, focus groups, personal usability reactions, identity-dependent testing, genuine voice/photo collection, interviews, mystery shopping requiring physical presence, or explicit independent human judgment.

## Hard-stop / owner escalation
Owner input is required only for:
- KYC, identity, tax, banking/payout setup, CAPTCHA, or personal profile facts
- any new monetary spend or financial commitment not already approved
- platform terms that are ambiguous about automation where acceptance could risk the account
- a contract containing unusual liability, exclusivity, IP assignment, indemnity, or material legal terms outside ordinary marketplace terms
- work involving sensitive/regulated data beyond the Factory's approved handling scope
- any request for credentials/secrets the Factory should not possess
- publication/account actions explicitly reserved to the owner by platform or canonical policy

## Dispatch policy
The Factory should optimize for **net contribution per constrained execution slot**, not human hourly wage.

When capacity is idle, low-value positive-margin GREEN-GATE jobs are acceptable. Higher-value work may preempt lower-value queued work when deadlines and existing commitments permit.

Target utilization: up to **90%** of safe execution capacity, retaining approximately 10% for retries, QA, spikes, and higher-value arrivals.

Never create duplicate worker/platform accounts or evade concurrency/account limits merely to increase capacity. Parallelism must occur inside permitted infrastructure or through legitimately separate authorized work streams.

## Machine-to-decision-maker protocol
Machines should communicate through a non-Work control channel using structured job messages. Until a dedicated event-driven agent endpoint is deployed, the canonical durable message format is a queue record containing:
- job_id
- source/platform
- client/job reference
- requested deliverable
- offered/contracted revenue
- deadline
- inputs/location
- platform automation rule status
- estimated machine time/cost
- risk flags
- proposed worker
- validation plan
- state: DISCOVERED | GREEN_GATE | ACCEPTED | RUNNING | QA | DELIVERED | PAID | REVIEW | REJECTED

The decision-maker may autonomously move GREEN-GATE jobs through ACCEPTED → RUNNING → QA → DELIVERED under this standing authorization.

Failures, ambiguity, or hard-stop conditions go to REVIEW rather than being guessed through.

## Cash accounting
Only completed paid transactions count as revenue. Leads, accepted jobs, completed-but-unpaid jobs, prospective contracts, and hypothetical capacity do not count as verified cash.

## Priority
1. Keep safe idle capacity earning positive contribution.
2. Protect account/platform longevity.
3. Replace low-yield jobs with higher-yield jobs as they become available.
4. Build recurring/direct demand so the Factory depends less on marketplaces.
5. Continue searching for larger machine-native cash engines and category-defining businesses in parallel.
