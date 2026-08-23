# Factory Freelancer Dispatcher

This worker uses the official Freelancer Python SDK and the account's Personal Access Token from an environment variable. The token must **never** be committed to GitHub.

## Required secret
`FLN_OAUTH_TOKEN`

## Behavior
- searches projects through the official SDK;
- rejects clearly human-specific or prohibited work;
- scores machine-suitable work;
- generates a proposed bid;
- supports dry-run mode before live bidding;
- only GREEN_GATE decisions may reach bid submission.

## Current stage
The first deployment must run in `dry_run=True` until authentication, project search response shape, and bid creation are verified against the live account. Once verified, the Factory autonomy policy permits qualifying positive-margin jobs to be submitted without per-job owner approval.

## Secret handling
Store the Freelancer PAT only in a private deployment secret/environment variable (for example Vercel Environment Variables). Never paste it into chat, source files, issues, commits, logs, or screenshots.

## Human-only gates
KYC, banking, identity verification, CAPTCHA, new monetary spend, or ambiguous platform-rule situations remain owner/human gates.
