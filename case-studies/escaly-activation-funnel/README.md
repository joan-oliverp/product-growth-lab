# Case Study: Escaly Activation Funnel

## 🎯 Context
Escaly is a SaaS platform that digitalizes standardized social assessment scales (e.g., GENCAT, Barthel Index) for NGOs and foundations.  
Pre-launch testing revealed that users often stalled after signup, without completing their first assessment.

---

## 🛠 Problem
Without completing an assessment and generating a report, users never reached the *value moment*.  
This led to low early activation and unclear trial-to-paid signals.

---

## 📐 Hypothesis
If onboarding is streamlined and supported by an AI assistant, **more users will complete their first assessment and generate a report within 7 days of signup**.

**Activation Metric (v1):**  
A user is considered *activated* when they generate their first report within 7 days of signup.

---

## 📊 Experiment Design
- **Cohort A (Baseline):** Manual onboarding with PDF instructions.  
- **Cohort B (Experiment):** Interactive onboarding + AI assistant.  

Tracked funnel steps:
1. Signup  
2. CreateUser  
3. SelectScale  
4. SubmitAssessment  
5. GenerateReport  

---

## 📈 Results (Mock Data)
- Cohort A: 35% activated  
- Cohort B: 55% activated  
- **Uplift: +20 percentage points** (directional, p < 0.1)

---

## 💡 Insights
- Reducing onboarding friction had more impact than adding new features.  
- The *“share report”* step emerged as the key **value moment** for buy-in.  
- AI assistant cut setup-related support tickets by ~30%.  

---

## 🚀 Next Steps
1. Roll out interactive onboarding for all users.  
2. Instrument `SharedReport` as an advanced activation milestone.  
3. Trigger trial-to-paid nudges post-report generation.  

---

## 📂 Artifacts
- **Tracking Plan:** [`tracking-plan-escaly/events.json`](../../tracking-plan-escaly/events.json)  
- **SQL Notebook:** [`dashboards/sql/activation-funnel.sql`](../../dashboards/sql/activation-funnel.sql)  
- **Mock Data:** [`data/mock/events.csv`](../../data/mock/events.csv)  
- **Figures:** ![Activation Funnel](../../figures/activation-funnel.png)

---
