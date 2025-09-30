# Case Study — Escaly Activation Funnel

## 🎯 Context
Escaly helps organizations measure and improve capabilities using structured frameworks (“scales”).  
The product delivers value when a user completes an assessment and generates a report.  
This case study defines how Escaly would **measure its activation funnel** prior to launch — setting a baseline for later PLG experiments.  

---

## 🛠 Problem
New users often sign up but fail to reach their **first value moment** (report generation).  
Without reliable activation, users are unlikely to return, retain, or upgrade.  
Escaly needs a clear definition and measurement of its activation funnel to identify drop-offs and cohort differences.  

---

## 📐 Hypothesis
If users can smoothly progress from signup to report generation within their **first session**, activation rates will be higher.  
By measuring this journey, Escaly can establish a baseline and understand friction points.  

- **North Star metric:** % of new signups who generate a report in their first session (`activation_rate_session1`).  
- **Activation event:** `generate_report`.  

---

## 📊 Experiment / Measurement
**Funnel Definition**
1. `signup_completed` → Account created & verified  
2. `select_scale` → User chooses framework  
3. `submit_assessment` → Assessment completed  
4. `generate_report` → First report generated (activation)  

**Metrics**
- Activation rate (Session 1)  
- Time to activation (median, in minutes)  
- Drop-off rates at each funnel step  

**Cohorts**
- Signup week/month  
- Acquisition channel (`organic`, `paid_search`, etc.)  
- Plan tier (`free`, `pro`, `business`)  

**Data**
- Synthetic dataset (`mock_data.csv`) with signup and activity events  
- SQL queries (`funnel.sql`) to compute metrics  

---

## 📈 Results (Mock Data)

**Funnel Conversion (Signup → Report)**  

| Step                | Users Remaining | Conversion % |
|---------------------|-----------------|--------------|
| Signup Completed    | 1,000           | 100%         |
| Scale Selected      | 820             | 82%          |
| Assessment Submitted| 600             | 60%          |
| Report Generated    | 270             | 27%          |

- **Activation Rate (Session 1):** 27%  
- **Median Time to Activation:** 14 minutes  
- **Cohort Example:** Organic users activated at 31%, while Paid Search users activated at 19%.  

**Figure 1:** Activation funnel visualization showing drop-offs at each stage (`funnel_chart.png`).  

---

## 💡 Insights
This diagnostic analysis shows:  
- The largest drop-off occurs at **Assessment Submission** (only 73% of users who select a scale complete the assessment).  
- **Organic users** outperform paid channels in activation, suggesting higher intent.  
- Free-tier users show slower time-to-activation than Pro-tier users, likely due to differences in onboarding guidance.  

---

## 🚀 Next Steps
- Expand mock dataset to include more acquisition channels.  
- Test SQL against different cohort definitions (plan tier, signup month).  
- Use this baseline to inform **future onboarding experiments** (streamlining assessments, better paid-user targeting).  

---

## 🔑 Why It Matters for PLG
Activation is the **gateway metric** in product-led growth:  
- Without activation, retention and monetization cannot compound.  
- Instrumenting the activation funnel now ensures future experiments are measurable.  
- Cohort-based insights provide a foundation for scalable PLG strategies.  
This approach generalizes to any B2B SaaS product where *first value delivery* determines long-term adoption.  

---

## 📂 Supporting Artifacts
- **Tracking Plan:** [../tracking-plan-escaly/events.json](../../tracking-plan-escaly/events.json)  
- **SQL Queries:** [funnel.sql](../../dashboards/sql/funnel.sql)  
- **Mock Data:** [mock_data.csv](../../mock-data/activation/mock_data.csv)  
- **Figures:** ![Activation Funnel](../../figures/activation-funnel.png)  

---
