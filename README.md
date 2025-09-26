# Product Growth Lab

A public portfolio of **technical product management artifacts** in **B2B SaaS, subscription models, and product-led growth (PLG)**.  
This repo showcases not just strategy, but **hands-on ability** to design instrumentation, run growth experiments, and analyze SaaS economics.

---

## 📌 Purpose
This repository demonstrates my approach to building and scaling **B2B SaaS products with subscription models and PLG**.

It highlights both **strategic thinking** (as a Head of Product) and **technical fluency**, including:
* Defining **event instrumentation** and activation funnels  
* Designing and analyzing **growth experiments**  
* Building **SQL dashboards** for retention, activation, and billing  
* Prototyping **AI-driven growth levers** (churn prediction, personalization)  
* Simulating **SaaS billing and pricing models**

All examples are based on my work with **Escaly** (a SaaS for social impact organizations) and broader SaaS learnings.  
Where real data is not available, I use **mock datasets** to illustrate the approach.

---

## 📂 Repository Structure

<span style="background-color: grey">**`/business-logic-escaly`**</span>  
* Defines funnels (AARRR), North Star, and key metrics at a **conceptual level**  
* Independent from event names or schemas  

👉 Frames *what matters* for Escaly’s growth.

<span style="background-color: grey">**`/tracking-plan-escaly`**</span>  
* Event schema in JSON + validation  
* Governance rules for naming, ownership, and PII handling  
* Flow diagrams of onboarding and reporting  

👉 Shows *how business logic is implemented* in instrumentation.

<span style="background-color: grey">**`/dashboards`**</span>  
* SQL queries for activation, retention, and conversion funnels  
* Mock dashboards (Metabase / Looker Studio exports)  
* Cohort analysis examples  

👉 Demonstrates data fluency and decision-support dashboards.

<span style="background-color: grey">**`/growth-experiments`**</span>  
* Experiment design docs in Markdown (hypothesis → setup → evaluation)  
* Sample size calculations and statistical significance checks  
* Jupyter notebooks simulating A/B test results  

👉 Evidence of structured experimentation mindset.

<span style="background-color: grey">**`/billing-sandbox`**</span>  
* Test integration with Stripe API (usage-based billing simulation)  
* Example scripts and workflows  
* Documentation on pricing/packaging strategies  

👉 Shows competence in SaaS billing mechanics.

<span style="background-color: grey">**`/ai-for-growth`**</span>  
* Prototype notebooks using OpenAI APIs for churn prediction and upsell triggers  
* Scripts for personalized onboarding or messaging  
* Documentation of real-world applicability  

👉 Extends my track record of AI integration into PLG levers.

<span style="background-color: grey">**`/case-studies`**</span>  
Readable write-ups that combine Escaly and SaaS learnings:
* **[Escaly Activation Funnel](./case-studies/escaly-activation-funnel/README.md)**  
  * Defined activation as *first report generated within Session 1*.  
  * Designed onboarding experiment (baseline vs. AI-guided flow).  
  * Built SQL notebook + funnel dashboard.  
  * Outcome: +20pp activation lift (mock data).  

👉 Storytelling layer connecting technical work to product strategy.

---

🔗 See [business-logic-escaly](business-logic-escaly) for conceptual definitions (funnels, North Star, key metrics) and [tracking-plan-escaly](tracking-plan-escaly) for their instrumentation and governance.  

---

## 🛣️ Roadmap & Status
This roadmap shows what’s complete (✅) and what’s in progress (⏳).  
Each artifact is delivered through commits and PRs, with reproducible instructions.

### Business Logic
* ✅ **business-logic-escaly** – defined funnels (AARRR), North Star metric, and key metrics in `business-logic.md`.

### Governance
* ✅ **governance.md** – established naming conventions, ownership, PII rules, and QA guidelines.

### Tracking Plan
* ⏳ **events.json** – initial draft completed with identifiers, events, and properties; under review before finalization.  
* ⏳ **events.schema.json** – lightweight schema created for validation in VS Code.  
* ⏳ **Instrumentation diagrams** – flow diagrams of acquisition → activation events planned.

### Case Studies
* ⏳ **Escaly Activation Funnel** – structure defined; narrative draft in progress, awaiting SQL notebook + funnel chart.  
* ⏳ **Paywall Conversion** – upcoming study on trial-to-paid conversion.  
* ⏳ **Retention Cohorts** – planned analysis of retention curves and cohort behavior.

### Dashboards & SQL
* ⏳ **activation_funnel.sql** – blueprint defined; notebook and charts pending.  
* ⏳ **retention_cohorts.sql** – planned cohort analysis queries and charts.  
* ⏳ **paywall_conversion.sql** – planned trial-to-paid conversion analysis.

### Growth Experiments
* ⏳ **A/B test templates** – design templates planned.  
* ⏳ **Future experiments** – upcoming (pricing page tests, onboarding variants).

### Billing Sandbox
* ⏳ **Stripe usage simulation** – planned for usage-based billing events.  
* ⏳ **Pricing scenarios** – planned simulations of packaging/revenue impact.

### AI for Growth
* ⏳ **Churn prediction prototype** – planned modeling of churn risk with mock data.  
* ⏳ **Personalized onboarding** – planned AI-driven onboarding experiments.

---

## 🧩 From Strategy to Execution
This portfolio connects **strategic product thinking** with **hands-on execution**.

- **Strategy:** Business logic defined first (AARRR funnel, North Star metric) to guide measurement.  
- **Execution:** Tracking plan implemented in JSON + schema, with governance and QA rules.  
- **Insight:** SQL notebooks and case studies that turn events into activation, retention, and monetization insights.  
- **Breadth:** Artifacts cover the full PLG journey — from acquisition funnels to billing, experimentation, and AI-driven growth levers.  

Together, these artifacts show how product metrics can be defined, instrumented, and analyzed to drive SaaS growth.

---

## 🔗 Connect with Me
* [LinkedIn](https://www.linkedin.com/in/joanoliverpoyatos/)  
* [Portfolio of Products](https://qstcoop.org/)  
* [Email](mailto:joan.poyatos@gmail.com)  
