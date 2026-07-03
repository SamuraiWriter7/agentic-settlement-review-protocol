# Changelog

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
