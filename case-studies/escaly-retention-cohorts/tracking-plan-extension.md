# Tracking Plan Extension — Retention Cohorts (Team Adoption)

> **Purpose.** Extend Escaly’s canonical tracking plan (`events.json` v1.0.0) to measure **team-based retention** without redefining activation. Activation remains **`generate_report`** (from the [Activation Funnel](../escaly-activation-funnel/README.md) case study). This file documents additive events, derived signals, and governance compliance.

---

## 1) Scope & Principles
- **Keep activation canonical**: activation = `generate_report` (first value moment).
- **Measure retention at the organization level** using weekly activity.
- **Favor server-authoritative signals** and avoid UI noise (no `login`).
- **No PII in properties**; use stable identifiers for joins (`user_id`, `account_id`).

**References**
- Tracking plan: `../../tracking-plan-escaly/events.v1.0.0.json`
- Governance: `../../tracking-plan-escaly/governance.md`
- Activation definition: *Case Study — Escaly Activation Funnel*

---

## 2) Additive Events (v1.1.0 candidate)

These additions are **minor version** changes (additive, non-breaking) that enable analysis of collaboration and org-level retention.

### 2.1 `user_invited`
- **Authority:** client
- **Status:** *planned (not yet active in Phase 1 analyses)*
- **Description:** A professional invites a colleague to join their organization.
- **Required identifiers:** `user_id`, `account_id`
- **Properties:**
  - `invite_method` *(enum: `email`, `link`)*
  - `is_resend` *(boolean)*
  - `source_surface` *(enum: `in_app`, `admin_dashboard`)*
- **Governance notes:** No emails or names in properties. The invite payload that contains PII is handled outside analytics.

### 2.2 `org_weekly_active` (derived)
- **Authority:** warehouse-derived (not emitted by client/server)
- **Description:** Weekly aggregate that marks an organization as active if it had ≥1 **qualifying event** in that ISO week.
- **Required identifiers:** `account_id`
- **Properties:**
  - `week_start_at` *(timestamp, ISO week Monday 00:00:00)*
  - `active_user_count` *(integer, distinct active users that week)*
  - `has_generated_report` *(boolean, whether any `generate_report` occurred)*
- **Qualifying events (value/usage):** `submit_assessment`, `generate_report`

> **Why derived?** It provides a clean retention metric in analysis without introducing noisy primitives like `login`.

---

## 3) Existing Canonical Events Used
| Event               | Purpose |
|---------------------|---------|
| `signup_completed`  | Defines cohort start (`signup_week`). |
| `submit_assessment` | Signals ongoing product use (assessment lifecycle). |
| `generate_report`   | Canonical activation & continued value moment. |

> **Note:** We intentionally **do not** add `user_activated`. The activation moment is already represented by `generate_report`.

---

## 4) Retention Metric (Org-Level)
> **Definition used across the case study:**
- **Weekly org retention** = % of organizations with `org_weekly_active = true` in week *n* after `signup_completed` (cohort by `signup_week`).
- `org_weekly_active = true` when an account has ≥1 qualifying event (`submit_assessment` or `generate_report`) during that ISO week.
