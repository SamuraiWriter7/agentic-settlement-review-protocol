# Changelog

## v0.5.0-candidate — Settlement Readiness Report

Fifth candidate release.

### Added

* `settlement-readiness-report.schema.json`
* `settlement-readiness-report.example.yaml`
* Validation support for settlement readiness report examples
* Settlement readiness summary records for AI agent settlement candidates
* Blocking status records for unresolved review, rule, dispute, legal, or evidence issues
* Settlement route recommendations for next-step review or settlement engine routing
* Risk summary records for settlement readiness evaluation

### New concepts

* `settlement_readiness_report`
* `report_scope`
* `source_reviews`
* `readiness_summary`
* `blocking_status`
* `settlement_route`
* `risk_summary`
* `readiness_decision`
* `report_status`

### Purpose

v0.5 introduces a final readiness report for the first candidate arc of the Agentic Settlement Review Protocol.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.
v0.2 added the Human Settlement Gate for human approval, hold, rejection, or escalation.
v0.3 added Marketplace Rule Review for marketplace and platform policy compatibility.
v0.4 added Dispute / Appeal Record for contested settlement candidates.
v0.5 summarizes the readiness state and recommends whether the candidate is ready, conditionally ready, blocked, rejected, escalated, or not ready.

### Important note

Settlement Readiness Reports are readiness summaries.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any final settlement action should remain subject to a valid settlement engine, marketplace governance process, legal framework, or authorized payout system.

---

## v0.4.0-candidate — Dispute / Appeal Record

Fourth candidate release.

### Added

* `dispute-appeal-record.schema.json`
* `dispute-appeal-record.example.yaml`
* Validation support for dispute and appeal examples
* Dispute records for contested settlement candidates
* Appeal records for marketplace rule decisions and human gate outcomes
* Evidence submission records for new or contested evidence
* Resolution records for blocked, reopened, escalated, or resolved settlement candidates

### New concepts

* `dispute_appeal_record`
* `dispute_scope`
* `related_records`
* `claimant`
* `dispute_basis`
* `evidence_submission`
* `review_process`
* `resolution`
* `dispute_status`

### Purpose

v0.4 introduces dispute and appeal handling before settlement readiness.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.
v0.2 added the Human Settlement Gate for human approval, hold, rejection, or escalation.
v0.3 added Marketplace Rule Review for marketplace and platform policy compatibility.
v0.4 records disputes, appeals, objections, and review requests related to attribution, weighting, payment evidence, provider signals, marketplace rules, or human gate outcomes.

### Important note

Dispute / Appeal Records are audit records.

They do not resolve disputes, execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any disputed settlement candidate should remain provisional until resolved by a valid human review process, marketplace governance system, legal framework, or authorized settlement process.

---

## v0.3.0-candidate — Marketplace Rule Review

Third candidate release.

### Added

* `marketplace-rule-review.schema.json`
* `marketplace-rule-review.example.yaml`
* Validation support for marketplace rule review examples
* Marketplace rule compatibility records for settlement candidates
* Rule check records for beneficiary eligibility, evidence policy, payment signals, attribution, payout thresholds, dispute windows, and risk policy
* Conditional approval and escalation records for marketplace-governed settlement flows

### New concepts

* `marketplace_rule_review`
* `marketplace_context`
* `rule_scope`
* `rule_checks`
* `rule_decision`
* `conditions`
* `escalation`
* `rule_review_status`

### Purpose

v0.3 introduces marketplace rule review between human settlement review and settlement readiness.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.
v0.2 added the Human Settlement Gate for human approval, hold, rejection, or escalation.
v0.3 adds marketplace and platform rule compatibility checks before any settlement candidate moves toward payout or settlement engine routing.

### Important note

Marketplace Rule Review records are policy compatibility records.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any settlement candidate should remain provisional until accepted by a valid settlement engine, marketplace governance system, legal framework, or authorized payout process.

---

## v0.2.0-candidate — Human Settlement Gate

Second candidate release.

### Added

* `human-settlement-gate.schema.json`
* `human-settlement-gate.example.yaml`
* Validation support for human settlement gate examples
* Human review gate structure for settlement candidates
* Gate decision records for approval, hold, rejection, escalation, and evidence requests
* Decision basis records for evidence completeness, attribution, payment signals, provider signals, and risk acceptability

### New concepts

* `human_settlement_gate`
* `gate_scope`
* `human_reviewers`
* `gate_decision`
* `decision_basis`
* `conditions`
* `escalation`
* `gate_status`

### Purpose

v0.2 introduces a human gate between settlement review and settlement readiness.

v0.1 created the Settlement Review Record for reviewing AI agent value-path evidence.
v0.2 adds a structured human approval layer that can hold, reject, escalate, or conditionally advance settlement candidates.

### Important note

Human Settlement Gate records are review records.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any settlement candidate should remain provisional until accepted by a valid settlement engine, marketplace rule framework, legal process, or authorized payout system.

---

## v0.1.0-candidate — Settlement Review Record

Initial candidate release.

### Added

* `settlement-review-record.schema.json`
* `settlement-review-record.example.yaml`
* Validation script for schema/example consistency
* GitHub Actions validation workflow
* Core settlement review fields:

  * `review_scope`
  * `source_records`
  * `evidence_status`
  * `review_findings`
  * `settlement_recommendation`
  * `audit`

### Purpose

v0.1 defines the first review layer between AI agent value-path evidence and settlement consideration.

It allows records from Agentic Royalty Path Standard and related audit layers to be reviewed for evidence completeness, attribution plausibility, human review requirements, legal review requirements, and settlement readiness.

### Core concept

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
```

This protocol reviews whether those records are ready for settlement consideration:

```text
Value Path Evidence
  ↓
Settlement Review Record
  ↓
Human / Legal / Marketplace Review
  ↓
Settlement Readiness
```

### Important note

Settlement Review Record does not execute payments.

It does not create legal royalty claims.

It does not approve final payouts.

It only records whether a value-path evidence bundle appears ready for further review, human gate evaluation, legal review, or settlement engine consideration.

