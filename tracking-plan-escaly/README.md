# Tracking Plan — Escaly

## 🎯 Purpose
This folder defines the **event instrumentation schema** for Escaly.  
It ensures all user interactions are tracked consistently to support **activation, retention, and monetization analysis**.

---

## 📂 Contents
- **events.json** → Canonical event schema (Signup → Report → UpgradePlan).  
- **governance.md** → Rules for naming, PII handling, and event ownership.  
- **diagrams/** → Visual sequence diagrams of onboarding and reporting flows.

---

## Relation to Business Logic
This tracking plan **implements** the metrics and funnels defined in the  
[`business-logic-escaly/business-logic.md`](../business-logic-escaly/business-logic.md).

- **Business logic = what matters** (North Star, AARRR funnel, key metrics)  
- **Tracking plan = how we capture it** (event names, properties, governance)

---

## 🔧 Core Events
- **Signup** — NGO admin registers (role property = Admin/Technician).  
- **CreateUser** — Admin adds the first internal user.  
- **SelectScale** — Technician selects an assessment scale.  
- **SubmitAssessment** — An evaluation is completed and submitted.  
- **GenerateReport** — A PDF/HTML report is created.  
- *(Advanced)* **SharedReport**, **UpgradePlan**, **InviteTeammate**.

---

## 📐 Activation Definition (v1)
A user is *activated* once they generate their first report within **7 days** of signup.

---

## 🧩 Governance Principles
- **Naming convention:** PascalCase for events, snake_case for properties.  
- **PII policy:** No personal identifiers in events; only internal UUIDs.  
- **Change management:** Updates via PR, with product + engineering review.  

---

## 📊 Example Usage
```sql
-- Count activated users (report generated within 7 days of signup)
WITH first_signup AS (
  SELECT user_id, signup_ts
  FROM users
),
first_report AS (
  SELECT user_id, MIN(ts) AS report_ts
  FROM events
  WHERE event_name = 'GenerateReport'
  GROUP BY user_id
)
SELECT COUNT(*) AS activated_users
FROM first_signup s
JOIN first_report r ON r.user_id = s.user_id
WHERE JULIANDAY(r.report_ts) - JULIANDAY(s.signup_ts) <= 7;
