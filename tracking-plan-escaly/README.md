# Tracking Plan — Escaly

## 🎯 Purpose
This folder defines the **event instrumentation schema** for Escaly.  
It ensures product interactions are tracked consistently to support **acquisition, activation, retention, and monetization analysis**.

The plan is implemented in code (JSON + schema) to provide version control, validation, and transparency — mirroring how modern SaaS teams manage analytics contracts.

---

## 📂 Contents
- **events.json** → Canonical event definitions (signup, assessment, report generation).  
- **governance.md** → Rules for naming, ownership, data quality, and PII handling.  
- **about-tracking-plan.md** → Rationale and overview of why this plan was designed this way.  
- **diagrams/** → Visual flow diagrams of onboarding and reporting funnels.  

---

👉 See [about-tracking-plan.md](about-tracking-plan.md) for the rationale behind this plan and how it was designed.

---

## Repo Flow
![Escaly Repo Flow](diagrams/repo_flow.png)

This diagram shows how the tracking plan sits between  
**business logic** (conceptual definitions) and **case studies** (insights).
