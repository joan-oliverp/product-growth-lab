# Case Study — Escaly Retention Cohorts

## 🎯 Context
This case study is part of the *Product Manager Technical Skills & PLG Portfolio*.  

The goal is to analyze **retention behavior in Escaly**, a B2B SaaS platform that digitalizes psychosocial assessments for social organizations.  

The study explores how *team adoption*—the number of professionals actively using Escaly within the same organization—affects 12-week retention.

---

## 🛠 Problem
- Early Escaly usage often remains limited to one enthusiastic professional within an organization.
- Without collaborative use, the platform’s full value—shared data, standardized reporting, and collective decision-making—never materializes.  
- Churn analysis showed that most inactive accounts had only one active user.  
- Escaly’s mission is inherently collaborative: assessments are interpreted, discussed, and followed up by multidisciplinary teams.  
- Understanding how early multi-user adoption influences long-term retention is essential to improve onboarding and expansion strategy.

---

## 📐 Hypothesis
> Organizations where **two or more professionals become active during the first 4 weeks after signup** will show **significantly higher 12-week retention** than organizations with only one active user.

Rationale:
- Collaboration transforms Escaly from an individual tool into a shared workflow.  
- Peers reduce friction by modeling correct use and reinforcing digital habits.  
- Once multiple users depend on shared data, the perceived switching cost increases.

In PLG terms, *team activation* is Escaly’s equivalent of a **collaboration loop**—similar to inviting teammates in Notion or Miro—and should correlate with sustained engagement.

---

## 📊 Measurement
**Cohort definition**  
- Cohorts grouped by `signup_week` (organization-level).  
- Observation window: 12 weeks post-signup.  

**Retention metric**
- % of organizations with ≥ 1 active user in week _n_.  

**Segmentation**
- **Single-user orgs:** 1 active user by week 4  
- **Multi-user orgs:** ≥ 2 active user by week 4  

---

## **Technical Specification**

The detailed tracking plan for this analysis is documented separately in:  
[`tracking-plan-extension.md`](./tracking-plan-extension.md)

This supporting file outlines the event schema, governance alignment, and measurement logic for the extended tracking plan that enables team-based retention analysis.

---

## 📈 Results (Mock or Real Data)

A 12-week retention analysis was run on 86 organizations that signed up between May and July 2025.

| Cohort Type | Week 1 | Week 4 | Week 8 | Week 12 |
|--------------|--------|--------|--------|---------|
| Single-user orgs (n = 49) | 68 % | 34 % | 19 % | 10 % |
| Multi-user orgs (n = 37) | 92 % | 73 % | 52 % | 31 % |

- Multi-user organizations retained activity **3.1× longer on average**.  
- The retention curve for team-adopted accounts flattened after week 6, while single-user accounts decayed steadily.  
- Entities using **multiple scales** (e.g., GENCAT + Barthel) added +6 pp to week 12 retention.  
- 81 % of churned accounts never had a second active user.

---

## 💡 Insights
1. **Team adoption drives retention.**  
   Escaly’s stickiness emerges once it becomes a shared workflow, not an individual tool.  

2. **Peer influence accelerates digital adoption.**  
   Internal champions succeed when they onboard at least one colleague early—social proof lowers resistance to change.  

3. **Depth and breadth reinforce each other.**  
   Collaborative teams using multiple scales retain longest, showing the compound effect of social and functional engagement.  

4. **Product implication.**  
   Onboarding should explicitly nudge first users to *invite a teammate* and *complete an assessment together*.  
   Collaboration is not a side feature; it’s the retention engine.

---

## 🚀 Next Steps
  Future PLG experiments should test:  
  - Auto-prompting invites during first assessment  
  - Shared dashboards and activity notifications  
  - Usage badges (“2 of your colleagues are active this week”)  

---

## 🔑 Why It Matters for PLG
- **Collaboration = Growth loop.**  
  “Invite → Collaborate → Retain” defines Escaly’s compounding engine. Each invitation extends the product’s reach inside an organization.  

- **Monetization readiness.**  
  Team retention validates a shift from single-seat trials to tiered, organization-based subscriptions—the foundation for scalable ARR.  

- **Efficient growth.**  
  A +10 pp increase in team activation can translate into +6–8 pp improvement in week-12 retention, boosting LTV without new acquisition spend.  

---

## 📂 Supporting Artifacts
- **Tracking Plan:** [Link to events.json or schema]  
- **SQL Notebook:** [Link to notebook or queries]  
- **Mock Data:** [Link to CSV/DB if available]  
- **Figures:** ![Example Chart](../../figures/example.png)  

---
