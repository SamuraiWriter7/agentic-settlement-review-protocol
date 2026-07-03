# Agentic Settlement Review Protocol

A protocol for reviewing AI agent value-path evidence, commerce audits, royalty candidates, marketplace rule checks, disputes, and settlement readiness before payout decisions.

## Purpose

Agentic Settlement Review Protocol defines a review layer between AI agent value-path evidence and settlement decisions.

It is designed to receive records from systems such as:

* Agentic Royalty Path records
* Monetization Event records
* Path Royalty Weighting records
* Provider Bridge records
* Agent Commerce Audit Bridge records
* Human Settlement Gate records
* Marketplace Rule Review records
* Dispute / Appeal records

The protocol does not execute payments.

It does not create legal royalty claims.

It does not approve final payouts.

Instead, it reviews whether the available evidence is ready to move toward human review, marketplace rule evaluation, legal review, dispute resolution, or an external settlement engine.

## Core idea

The previous layer records how AI agent value was generated:

```text
Agentic Path
  ↓
Monetization Event
  ↓
Path Royalty Weighting
  ↓
Provider Bridge
  ↓
Commerce Audit
```

This protocol reviews whether those records are ready for settlement consideration:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human Settlement Gate
  ↓
Marketplace Rule Review
  ↓
Dispute / Appeal Record
  ↓
Settlement Readiness Report
```

The goal is to keep AI agent settlement flows auditable, reviewable, and non-final until the proper review gates have been completed.

## Design principles

### 1. Review before settlement

Evidence should be reviewed before any payout decision is made.

A value path may be plausible without being ready for settlement.

### 2. Candidate, not claim

A royalty candidate is not a legal claim.

A suggested share is not a payout decision.

A readiness report is not a final settlement.

This protocol preserves those distinctions.

### 3. Human gate by default

When attribution, payment evidence, provider evidence, dispute status, or legal meaning is uncertain, human review should remain available.

### 4. Marketplace-aware

Settlement candidates may be valid as evidence but still fail marketplace or platform rules.

This protocol separates evidence review from marketplace rule compatibility.

### 5. Dispute-safe

Settlement should remain blockable when a dispute, appeal, objection, or contested evidence exists.

### 6. Settlement readiness, not payment execution

This protocol evaluates readiness.

It does not execute payments or settlements.

## Version overview

```text
v0.1 — Settlement Review Record
v0.2 — Human Settlement Gate
v0.3 — Marketplace Rule Review
v0.4 — Dispute / Appeal Record
v0.5 — Settlement Readiness Report
```

## v0.1 — Settlement Review Record

v0.1 introduces the minimum structure for reviewing settlement readiness.

It defines:

* `review_scope`
* `source_records`
* `evidence_status`
* `review_findings`
* `settlement_recommendation`
* `audit`

Core flow:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human / Legal / Marketplace Review
  ↓
Settlement Readiness
```

The Settlement Review Record evaluates whether an evidence bundle appears ready for further review, human gate evaluation, legal review, or settlement engine consideration.

## v0.2 — Human Settlement Gate

v0.2 introduces the Human Settlement Gate.

This layer defines how human reviewers can approve, hold, reject, escalate, or request more evidence before any payout decision or settlement engine execution.

Core flow:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human Settlement Gate
  ↓
Approved / Hold / Needs More Evidence / Rejected
  ↓
Settlement Readiness
```

### Human Settlement Gate concepts

v0.2 introduces:

* `gate_scope`
* `human_reviewers`
* `gate_decision`
* `decision_basis`
* `conditions`
* `escalation`
* `audit`

The Human Settlement Gate is a review record.

It does not execute payments, create legal royalty claims, or determine final payout rights by itself.

## v0.3 — Marketplace Rule Review

v0.3 introduces the Marketplace Rule Review.

This layer evaluates settlement candidates against marketplace, platform, community, policy, eligibility, and payout rules before settlement readiness.

Core flow:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human Settlement Gate
  ↓
Marketplace Rule Review
  ↓
Allowed / Conditional / Rejected / Escalated
  ↓
Settlement Readiness
```

### Marketplace Rule Review concepts

v0.3 introduces:

* `marketplace_context`
* `rule_scope`
* `rule_checks`
* `rule_decision`
* `conditions`
* `escalation`
* `rule_review_status`

Marketplace Rule Review can check whether:

* the beneficiary is eligible
* the evidence meets marketplace policy
* the payment signal is accepted
* attribution is allowed
* payout thresholds are met
* the dispute window is clear
* risk policy requirements are satisfied

The Marketplace Rule Review is a policy compatibility record.

It does not execute payouts or create legal royalty claims.

## v0.4 — Dispute / Appeal Record

v0.4 introduces the Dispute / Appeal Record.

This layer records disputes, appeals, objections, and review requests related to settlement candidates before settlement readiness.

Core flow:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human Settlement Gate
  ↓
Marketplace Rule Review
  ↓
Dispute / Appeal Record
  ↓
Resolved / Rejected / Escalated / Reopened
  ↓
Settlement Readiness
```

### Dispute / Appeal concepts

v0.4 introduces:

* `dispute_scope`
* `related_records`
* `claimant`
* `dispute_basis`
* `evidence_submission`
* `review_process`
* `resolution`
* `audit`

The Dispute / Appeal Record captures contested settlement candidates, attribution disagreements, payment evidence objections, marketplace rule appeals, human gate appeals, royalty weighting disputes, commerce audit disputes, and settlement readiness objections.

It does not resolve disputes by itself.

It records the dispute so that settlement can remain blocked, reopened, escalated, or reviewed.

## v0.5 — Settlement Readiness Report

v0.5 introduces the Settlement Readiness Report.

This layer summarizes whether an AI agent settlement candidate is ready, conditionally ready, blocked, rejected, escalated, or not ready before any payout decision or settlement engine execution.

Core flow:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human Settlement Gate
  ↓
Marketplace Rule Review
  ↓
Dispute / Appeal Record
  ↓
Settlement Readiness Report
  ↓
Ready / Conditional / Blocked / Rejected / Escalated
```

### Settlement Readiness Report concepts

v0.5 introduces:

* `report_scope`
* `source_reviews`
* `readiness_summary`
* `blocking_status`
* `settlement_route`
* `risk_summary`
* `recommendation`
* `audit`

The Settlement Readiness Report summarizes:

* whether evidence is complete
* whether the human gate is complete
* whether marketplace rules are satisfied
* whether disputes are clear
* whether settlement remains blocked
* what next route is recommended
* what risk level remains
* whether settlement readiness can be granted

The report does not execute payouts, create legal royalty claims, or determine final settlement rights.

It only summarizes readiness and recommends the next route.

## Repository structure

```text
schemas/
  settlement-review-record.schema.json
  human-settlement-gate.schema.json
  marketplace-rule-review.schema.json
  dispute-appeal-record.schema.json
  settlement-readiness-report.schema.json

examples/
  settlement-review-record.example.yaml
  human-settlement-gate.example.yaml
  marketplace-rule-review.example.yaml
  dispute-appeal-record.example.yaml
  settlement-readiness-report.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate.yml
```

## Validation

Validate all examples against their schemas:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Settlement Review Record
[ok] Settlement Review Record example is valid

[validate] Human Settlement Gate
[ok] Human Settlement Gate example is valid

[validate] Marketplace Rule Review
[ok] Marketplace Rule Review example is valid

[validate] Dispute / Appeal Record
[ok] Dispute / Appeal Record example is valid

[validate] Settlement Readiness Report
[ok] Settlement Readiness Report example is valid
```

## Important note

This protocol does not execute payments.

It does not create legal royalty claims.

It does not approve final payouts.

It does not determine final settlement rights.

Instead, it provides audit-ready review records for evaluating whether AI agent value-path evidence is ready for further review, human gate evaluation, marketplace rule evaluation, dispute resolution, legal review, or settlement engine consideration.

Any commerce action, payment event, authorization event, royalty candidate, suggested share, dispute resolution, or readiness report should be treated as provisional until reviewed and accepted by a valid human process, marketplace governance system, legal framework, settlement engine, or authorized payout process.

## Current candidate

```text
v0.5.0-candidate — Settlement Readiness Report
```

## First arc summary

The first candidate arc establishes five review layers:

```text
Review
  ↓
Human Gate
  ↓
Marketplace Rule
  ↓
Dispute / Appeal
  ↓
Readiness Report
```

Together, these layers define a foundation for AI agent settlement review.

Agentic Settlement Review Protocol is designed as a bridge between AI agent value-path evidence, human review, marketplace governance, dispute handling, and settlement readiness.

## Roadmap

Possible future extensions:

```text
v0.6 — Legal Review Bridge
v0.7 — Settlement Engine Handoff
v0.8 — Multi-Party Settlement Graph
v0.9 — Payout Execution Receipt
v1.0 — Agentic Settlement Review Standard
```

