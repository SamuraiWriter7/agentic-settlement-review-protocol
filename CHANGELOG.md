# Changelog

## v0.3.0-candidate — Marketplace Rule Review

Third candidate release.

### Added

- `marketplace-rule-review.schema.json`
- `marketplace-rule-review.example.yaml`
- Validation support for marketplace rule review examples
- Marketplace rule compatibility records for settlement candidates
- Rule check records for beneficiary eligibility, evidence policy, payment signals, attribution, payout thresholds, dispute windows, and risk policy
- Conditional approval and escalation records for marketplace-governed settlement flows

### New concepts

- `marketplace_rule_review`
- `marketplace_context`
- `rule_scope`
- `rule_checks`
- `rule_decision`
- `conditions`
- `escalation`
- `rule_review_status`

### Purpose

v0.3 introduces marketplace rule review between human settlement review and settlement readiness.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.  
v0.2 added the Human Settlement Gate for human approval, hold, rejection, or escalation.  
v0.3 adds marketplace and platform rule compatibility checks before any settlement candidate moves toward payout or settlement engine routing.

### Important note

Marketplace Rule Review records are policy compatibility records.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any settlement candidate should remain provisional until accepted by a valid settlement engine, marketplace governance system, legal framework, or authorized payout process.

## v0.2.0-candidate — Human Settlement Gate

Second candidate release.

### Added

- `human-settlement-gate.schema.json`
- `human-settlement-gate.example.yaml`
- Validation support for human settlement gate examples
- Human review gate structure for settlement candidates
- Gate decision records for approval, hold, rejection, escalation, and evidence requests
- Decision basis records for evidence completeness, attribution, payment signals, provider signals, and risk acceptability

### New concepts

- `human_settlement_gate`
- `gate_scope`
- `human_reviewers`
- `gate_decision`
- `decision_basis`
- `conditions`
- `escalation`
- `gate_status`

### Purpose

v0.2 introduces a human gate between settlement review and settlement readiness.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.  
v0.2 adds a structured human approval layer that can hold, reject, escalate, or conditionally advance settlement candidates.

### Important note

Human Settlement Gate records are review records.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any settlement candidate should remain provisional until accepted by a valid settlement engine, marketplace rule framework, legal process, or authorized payout system.

## v0.1.0-candidate — Settlement Review Record

Initial candidate release.

### Added

- `settlement-review-record.schema.json`
- `settlement-review-record.example.yaml`
- Validation script for schema/example consistency
- GitHub Actions validation workflow
- Core settlement review fields:
  - `review_scope`
  - `source_records`
  - `evidence_status`
  - `review_findings`
  - `settlement_recommendation`
  - `audit`

### Purpose

v0.1 defines the first review layer between AI agent value-path evidence and settlement consideration.

It allows records from Agentic Royalty Path Standard and related audit layers to be reviewed for evidence completeness, attribution plausibility, human review requirements, legal review requirements, and settlement readiness.

### Important note

Settlement Review Record does not execute payments.

It does not create legal royalty claims.

It does not approve final payouts.

It only records whether a value-path evidence bundle appears ready for further review, human gate evaluation, legal review, or settlement engine consideration.


