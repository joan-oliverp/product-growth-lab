# Case Study: Designing Escaly’s Activation Funnel

## 🎯 Context
Escaly is a SaaS platform that digitalizes standardized social assessment scales (e.g., GENCAT, Barthel Index) for NGOs, care organizations, and foundations. Our target customers are traditionally conservative, with low digital adoption and limited budgets. At pre-launch, we needed to:

1. Demonstrate time-to-value quickly.  
2. Build confidence in replacing Excel/paper workflows.  
3. Create a repeatable funnel that could scale across federations and associations.  

## 🛠️ Problem
Our challenge: **users often signed up but stalled before completing their first assessment**. Without reaching this milestone, they couldn’t perceive Escaly’s value (automatic scoring, dashboards, reports).

## 📐 Hypothesis
If we streamline the onboarding process and guide users to complete their **first evaluation and generate one report**, activation will increase and trial-to-paid conversion will follow.

**Activation Metric (North Star for this experiment):**  
👉 *A new account is considered “activated” when it completes one assessment and generates one report within the first 7 days.*

## 📊 Funnel Design
Proposed steps for activation funnel:

1. **Signup** – NGO admin registers via web form.  
2. **Onboarding Tour** – Guided workflow shows how to create a first user & choose a scale.  
3. **First Assessment** – Technician enters responses for a sample user.  
4. **Report Generation** – Escaly outputs a PDF dashboard with automatic scoring.  
5. **Value Moment** – User shares the report with a colleague or director.  

## 🔧 Instrumentation Plan
Tracked Events (in JSON-style schema):

```json
[
  {"event": "Signup", "properties": {"role": "Admin"}},
  {"event": "CreateUser", "properties": {"count": 1}},
  {"event": "SelectScale", "properties": {"scale": "GENCAT"}},
  {"event": "SubmitAssessment", "properties": {"duration_sec": 240}},
  {"event": "GenerateReport", "properties": {"report_type": "Individual"}}
]
```

## 🧪 Experiment Setup
- **Cohort A (Baseline):** Current onboarding flow (manual PDF instructions).  
- **Cohort B (Experiment):** Interactive onboarding with inline guidance and AI-powered assistant.  

**Hypothesis:** Cohort B will show a **+20% increase** in users reaching activation (report generated in <7 days).

## 📈 Results (Mock Data)
- Cohort A (n=20): 35% reached activation  
- Cohort B (n=20): 55% reached activation  
- Uplift: +20 percentage points (p < 0.1, directional but promising)  

## 💡 Insights
- Reducing onboarding friction matters more than feature depth.  
- The *“value moment”* (sharing first report) is critical to securing organizational buy-in.  
- AI assistant answered basic setup questions, cutting support requests by 30%.  

## 🚀 Next Steps
1. Expand interactive onboarding to all new users.  
2. Automate trial-to-paid nudges triggered after report generation.  
3. Instrument **“Shared Report”** as an advanced activation event.  

✅ **Takeaway**: In early-stage SaaS, activation is the single most important funnel milestone. By focusing Escaly’s onboarding on *getting to the first report*, we improved trial engagement and set the stage for monetization.
