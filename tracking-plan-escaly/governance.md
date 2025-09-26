# Escaly — Tracking Governance

## 1. Purpose & Scope
This document defines the **governance rules** for Escaly’s product analytics.  
It ensures event instrumentation is **consistent, reliable, and maintainable** across all case studies.  
These rules apply to all current and future events, properties, and identifiers.

---

## 2. Ownership & Change Management
- **Owner:** Product Manager (Escaly)  
- **Reviewers:** Data Analyst / Engineer  
- **Change process:**  
  - Propose changes via GitHub Pull Request  
  - Review for consistency with governance  
  - Update version history below  
- **Change log:**  
  | Date       | Version | Change            | Owner |
  |------------|---------|-------------------|-------|
  | 2025-09-25 | 1.0.0   | Initial governance | PM    |

---

## 3. Naming Conventions

### Events
- **Format:** `snake_case`  
- **Style:** VerbNoun, present tense (e.g., `generate_report`, `submit_assessment`)  
- **Avoid:** spaces, punctuation, emojis, capitalization inconsistencies  
- **Optional grouping:** use prefixes for domains if helpful (e.g., `assessment_submit`, `report_generate`)  
- **Rule:** events describe *business actions*, not UI clicks (✅ `submit_assessment` | ❌ `click_next_button`)

### Properties
- **Format:** `snake_case`  
- **Style:** descriptive, generic, and reusable (✅ `plan_tier` | ❌ `signup_button_color`)  
- **Booleans:** prefix with `is_` or `has_` (e.g., `is_trial`, `has_completed`)  
- **Dates/times:** suffix `_at` or `_timestamp` (e.g., `submitted_at`)  
- **Enums:** allowed values must be documented in the tracking plan (e.g., `plan_tier` = free, pro, business)

### Identifiers
- `user_id` = stable per individual user  
- `account_id` = stable per customer account (B2B context)  
- `assessment_id` = unique per assessment  
- `anonymous_id` = pre-authentication identifier  

---

## 4. Data Quality & QA
- **Deduplication:**  
  - Use `(user_id, event_name, occurred_at)` as unique key  
  - For assessments, dedupe by `assessment_id`  
- **Test data:** exclude internal/test users and accounts from production metrics  
- **Type checks:** ensure property types match definitions (int, string, bool, enum)  
- **Null handling:** required properties must never be null  
- **Monitoring:** sample events checked in dev and production  

### Event QA Rules
To ensure data quality, each event must pass the following validation checks in the warehouse:
| Event             | Idempotency Key                  | Required Non-Null Fields                     | Notes                                   |
|-------------------|----------------------------------|----------------------------------------------|-----------------------------------------|
| signup_started    | anonymous_id, event, occurred_at | anonymous_id, signup_step, source_surface     | Client event; allow retries, dedupe in warehouse |
| signup_completed  | user_id, event                   | user_id, account_id, method, is_email_verified | Server authoritative; one per account   |
| select_scale      | user_id, scale_id, event, occurred_at | user_id, account_id, scale_id, scale_name | Client event; used for funnel analysis  |
| submit_assessment | assessment_id, status            | user_id, account_id, assessment_id, scale_id, status | Keep latest record per assessment_id; server authoritative |
| generate_report   | report_id                        | user_id, account_id, report_id, assessment_id, scale_id, format | Server authoritative; dedupe by report_id |

---

## 5. Versioning
- **Method:** Semantic Versioning (semver)  
  - Patch = small clarifications, typos  
  - Minor = additive (new properties/events)  
  - Major = breaking change (rename, redefine)  
- **Deprecation:** deprecated events must remain documented with an end date and replacement guidance  

---

## 6. Privacy & Compliance
- **PII:**  
  - No personal data (e.g., names, emails) in event properties  
  - Identity resolution only via designated identity calls  
- **Regulatory:** Follow GDPR-style principles (minimal necessary data, explicit consent where required)

---

## 7. Relation to Business Logic
This governance ensures Escaly’s tracking plan is **clean, consistent, and compliant**.  

It exists to support the **business logic** defined in  
[`business-logic-escaly/business-logic.md`](../business-logic-escaly/business-logic.md),  
which specifies the core funnels and metrics that guide product decisions.

---
