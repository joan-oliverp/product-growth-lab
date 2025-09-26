# Escaly — Business Logic

## 1. Purpose & Scope
This document defines **Escaly’s business logic**: the core funnels, the North Star, and key product metrics.  
It is **independent of instrumentation** — no event names, property keys, or schemas are included here.  
The goal is to describe *what matters* for Escaly’s growth, before deciding *how to capture it*.

---

## 2. Conventions & IDs
- **Metric identifiers:** use `snake_case` for stable IDs.  
- **Display names:** written in Title Case.  
- **Window conventions:** append `_d30`, `_w1`, `_m1` when relevant (e.g., 30 days, 1 week, 1 month).  
- **Scope clarity:** specify whether a metric is at the **user**, **account**, or **org-wide** level.

---

## 3. AARRR Funnel Definitions
Escaly follows the AARRR model. Each stage is defined conceptually:

### Acquisition
- **Goal:** Convert visitors into registered users.  
- **Definition:** A user is acquired when they complete the signup process.  
- **Attribution:** Acquisition source is assigned using last non-direct marketing touch.  

### Activation
- **Goal:** Ensure new users realize value quickly.  
- **Definition:** A user is activated when they experience Escaly’s first value moment (generating a usable report) during their first session.  
- **Window:** Session 1 is defined as continuous usage until 30 minutes of inactivity.  

### Retention
- **Goal:** Keep users coming back to repeat the value moment.  
- **Definition:** A user is retained if they return to perform a core action (such as completing a new assessment or viewing a new report) after at least 30 days.  

### Referral
- **Goal:** Users invite or recommend Escaly to others.  
- **Definition:** A referral occurs when a user brings a new teammate or account into Escaly. *(to be detailed in later phases)*  

### Revenue
- **Goal:** Users or accounts generate monetary value.  
- **Definition:** Revenue is recognized when an account transitions to a paid plan or renews subscription. *(to be detailed in later phases)*  

---

## 4. North Star Metric

### Monthly Assessments (`nsm_monthly_assessments`)
- **Definition:** The total number of assessments completed across all users and all scales in a given calendar month.  
- **Scope:** All users and accounts, aggregated monthly.  
- **Deduplication:** Each assessment counts once, regardless of retries.  
- **Segments:** Always analyzed by plan type, acquisition channel, and industry.  
- **Why it matters:** This represents recurring value creation — every assessment signals that Escaly is helping users measure, learn, and improve.

---

## 5. Key Metrics

### Metric Glossary

| Metric ID                          | Display Name                        | Purpose                                               |
|-----------------------------------|-------------------------------------|-------------------------------------------------------|
| `signup_completion_rate`          | Signup Completion Rate              | Efficiency of Escaly’s signup flow                    |
| `acq_to_activation_rate`          | Acquisition to Activation Rate      | Quality of new users (conversion into value)          |
| `signup_channel_share`            | Channel Mix of New Accounts         | Distribution of signups by acquisition source         |
| `activation_rate_session1`        | Activation Rate (First Session)     | Effectiveness of onboarding                          |
| `tta_median_minutes`              | Time to Activation (Median)         | Speed of delivering first value                      |
| `completion_rate_assessment`      | Assessment Completion Rate          | Usability of assessments (drop-off inside flow)       |
| `assessments_per_active_account_m1` | Assessments per Active Account/Month | Depth of usage and account-level engagement          |

---

### Acquisition Metrics
- **Signup Completion Rate (`signup_completion_rate`)**  
  Percentage of users who start the signup process and successfully create an account.  
  *Purpose:* Measures the efficiency of Escaly’s onboarding funnel entry point.

- **Acquisition to Activation Rate (`acq_to_activation_rate`)**  
  Percentage of newly acquired users who reach their first value moment within Session 1.  
  *Purpose:* Connects acquisition quality to early product value.

- **Channel Mix of New Accounts (`signup_channel_share`)**  
  Distribution of new accounts by acquisition source (e.g., organic, paid, referral).  
  *Purpose:* Highlights which channels drive new users into Escaly.

---

### Activation Metrics
- **Activation Rate (First Session) (`activation_rate_session1`)**  
  Percentage of new users who reach their first value moment during their first session.  
  *Purpose:* Evaluates onboarding effectiveness.

- **Time to Activation (Median) (`tta_median_minutes`)**  
  Median elapsed time between signup and reaching the first value moment.  
  *Purpose:* Shows how quickly new users realize value.

---

### Product Usage Metrics
- **Assessment Completion Rate (`completion_rate_assessment`)**  
  Ratio of assessments successfully completed to assessments started within a given month.  
  *Purpose:* Indicates product usability and where users drop off.

- **Assessments per Active Account per Month (`assessments_per_active_account_m1`)**  
  Average number of completed assessments per active account in a month.  
  *Purpose:* Normalizes usage by account size and highlights depth of adoption.

---

## 6. Segmentation, Cohorts & Sessionization
- **Segments:** Metrics are sliced by acquisition channel, plan type, industry, and region.  
- **Cohorts:** Users/accounts are grouped by signup week or month.  
- **Session definition:** A session ends after 30 minutes of inactivity. The first session begins at signup.  

---

## 7. Attribution Rules
- **Model:** Last non-direct attribution.  
- **Hierarchy:** Ad click > Campaign tag > Referral > Direct.  
- **Purpose:** Ensures acquisition sources are assigned consistently.  

---

## 8. Data Quality & Edge Cases
- **Test users:** Internal/test accounts excluded from all metrics.  
- **Timezone:** All metrics calculated in UTC; visualizations may adapt to viewer timezone.  
- **Late data:** Metrics finalized after a 5-day window to allow for delayed processing.  
- **Granularity:** Metrics reported monthly unless otherwise specified.  

---

## 9. Relation to Governance
This document defines *what matters* for Escaly’s growth (funnels, North Star, key metrics) at the **conceptual level**.  

The corresponding **governance rules** (naming conventions, QA, privacy, versioning) are defined in  
[`tracking-plan-escaly/governance.md`](../tracking-plan-escaly/governance.md) and ensure that any tracking plan implementing these metrics remains consistent and trustworthy.

---

## 10. Versioning & Change Log
- **Versioning:** Semantic Versioning (semver) applies to business logic.  
  - Patch = clarity/typo updates.  
  - Minor = additive definitions.  
  - Major = changes to metric definitions.  

| Date       | Version | Change                  | Owner |
|------------|---------|-------------------------|-------|
| 2025-09-25 | 1.0.0   | Initial business logic  | PM    |

---
