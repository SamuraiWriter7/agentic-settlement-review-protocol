# Agentic Settlement Review Protocol

A protocol for reviewing AI agent value-path evidence, commerce audits, royalty candidates, and settlement readiness before payout decisions.

## Purpose

Agentic Settlement Review Protocol defines a review layer between agentic value-path evidence and settlement decisions.

It is designed to receive records from systems such as:

- Agentic Royalty Path records
- Monetization Event records
- Path Royalty Weighting records
- Provider Bridge records
- Agent Commerce Audit Bridge records

The protocol does not execute payments.

It does not create legal royalty claims.

It does not approve final payouts.

Instead, it reviews whether the available evidence is ready to move toward human review, legal review, marketplace rule evaluation, or an external settlement engine.

## Core idea

The previous layer records how value was generated:

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

This protocol reviews whether those records are ready for settlement consideration:

Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human / Legal / Marketplace Review
  ↓
Settlement Readiness
v0.1 — Settlement Review Record

v0.1 introduces the minimum structure for reviewing settlement readiness.

It defines:

review_scope
source_records
evidence_status
review_findings
settlement_recommendation
audit
Design principles
1. Review before settlement

Evidence should be reviewed before any payout decision is made.

A value path may be plausible without being ready for settlement.

2. Candidate, not claim

A royalty candidate is not a legal claim.

A suggested share is not a payout decision.

This protocol preserves that distinction.

3. Human gate by default

When attribution, payment evidence, provider evidence, or legal meaning is uncertain, human review should remain available.

4. Settlement readiness, not payment execution

This protocol evaluates readiness.

It does not execute payments or settlements.

Repository structure
schemas/
  settlement-review-record.schema.json

examples/
  settlement-review-record.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate.yml
Validation
python scripts/validate_examples.py

Expected output:

[validate] Settlement Review Record
  schema : schemas/settlement-review-record.schema.json
  example: examples/settlement-review-record.example.yaml
[ok] Settlement Review Record example is valid
Current candidate
v0.1.0-candidate — Settlement Review Record
Roadmap
v0.1 — Settlement Review Record
v0.2 — Human Settlement Gate
v0.3 — Marketplace Rule Review
v0.4 — Dispute / Appeal Record
v0.5 — Settlement Readiness Report
Important note

This protocol does not create legal royalty claims, approve payouts, or execute settlement.

It provides audit-ready review records for determining whether AI agent value-path evidence is ready for further review or settlement consideration.
