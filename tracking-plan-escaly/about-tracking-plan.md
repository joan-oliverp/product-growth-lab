# About the Escaly Tracking Plan

## 🎯 Purpose
Escaly’s tracking plan defines how product interactions are captured so they can be turned into reliable business metrics.  
It connects **business goals** (activation, retention, North Star) with **clean instrumentation rules** that ensure data quality.

Unlike many teams that keep tracking plans in spreadsheets, Escaly maintains the plan in **JSON + schema**.  
This makes it version-controlled, auditable, and aligned with how modern SaaS companies work.

---

## 🧭 Design Approach
The plan was shaped by combining three elements:
- **Business logic** → AARRR funnel definitions and the North Star metric (monthly assessments).  
- **Governance** → clear rules for naming, ownership, and PII handling.  
- **Industry practice** → inspired by Segment/Amplitude-style tracking plans, but extended with validation and B2B identifiers.

---

## 📑 Current Scope
For the current phase (Activity 1.1), the plan instruments:
- **Acquisition** → signup start and completion.  
- **Activation** → scale selection, assessment submission, and report generation.  
- **North Star** → monthly completed assessments.  
- **Key metrics** → signup completion rate, acquisition-to-activation rate, activation rate, time to activation, assessment completion, and assessments per active account.

---

## 🚀 Why it Matters
By making the tracking plan explicit and code-based, Escaly shows:
- **Strategic alignment** → product metrics are defined before instrumentation.  
- **Operational discipline** → governance rules enforce consistency and compliance.  
- **Clarity** → artifacts are structured, easy to scan, and directly linked to product growth questions.

---
