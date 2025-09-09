# Product Growth Lab

**A curated portfolio of SaaS & PLG technical case studies**

*By Joan Oliver Poyatos*

## 📌 Purpose

This repository showcases my hands-on approach to building and scaling **B2B SaaS products with subscription models and product-led growth (PLG)**.

It demonstrates not only strategic thinking as a Head of Product, but also the technical fluency needed to:
* Design event tracking and data models
* Run experiments and analyze product metrics
* Integrate SaaS billing and APIs
* Apply AI for growth, retention, and personalization

All examples are based on my current work with **Escaly** (a SaaS for social impact organizations) and other B2B SaaS learnings. Where real data is not available, I use **mock datasets** to illustrate the approach.

## 📂 Repository Structure
<span style="background-color: grey">**`/tracking-plan-escaly`**</span>
* Event schema in JSON/CSV format
* Documentation of key activation, retention, and monetization events
* Example instrumentation diagrams

👉 Shows ability to define measurable PLG funnels.

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
* Example scripts for personalized onboarding or messaging
* Documentation of real-world applicability

👉 Extends my track record of AI integration into PLG levers.

<span style="background-color: grey">**`/case-studies`**</span>

Readable write-ups that combine Escaly and SaaS learnings:
* **[Escaly Activation Funnel](./case-studies/escaly-activation-funnel/README.md)**
  * Defined activation as *first report generated within 7 days of signup*.
  * Designed onboarding experiment (baseline vs. AI-guided flow).
  * Built SQL notebook + dashboard to measure funnel conversion.
  * Outcome: +20pp increase in activation (mock data).

👉 Storytelling layer that connects technical work to product strategy.

## 🛣️ Roadmap & Status

To provide transparency on what’s already implemented and what’s planned, here’s a high‑level roadmap. Items marked ✅ are complete; items marked ⏳ are in progress or queued for future sprints.

### Case Studies
* ✅ **Escaly Activation Funnel** – defined activation metric, designed onboarding experiment, and documented the results with insights.
* ⏳ **Paywall Conversion** – upcoming study on trial-to-paid conversion; will include SQL analysis and experiment design.
* ⏳ **Retention Cohorts** – planned analysis of retention curves and cohort behaviour.

### Tracking Plan
* ⏳ **tracking-plan-escaly/events.json** – define core events and properties for Escaly, including naming conventions and governance notes.
* ⏳ **Instrumentation diagrams** – visual diagrams showing event flow across the activation funnel.

### Dashboards & SQL

* ⏳ **activation_funnel.sql** – write SQL to compute activation rate within 7 days.
* ⏳ **retention_cohorts.sql** – build cohort analysis queries and corresponding charts.
* ⏳ **paywall_conversion.sql** – explore trial-to-paid conversion metrics.

### Growth Experiments

* ⏳ **AB test templates** – create Markdown templates and notebooks for experiment design and sample size calculation.
* ⏳ **Additional experiments** – document future experiments such as pricing page tests or onboarding variants.

### Billing Sandbox

* ⏳ **Stripe usage simulation** – build a Python script to simulate usage-based billing events.
* ⏳ **Pricing scenarios** – outline alternative pricing/packaging strategies and their impact on revenue.

### AI for Growth

* ⏳ **Churn prediction prototype** – develop an initial notebook to model churn risk using mock engagement data.
* ⏳ **Personalized onboarding** – experiment with AI-driven onboarding sequences tailored to user personas.

You can follow these roadmap items through the repository’s commits and PRs. Each new artifact will update this checklist and include clear instructions so you can reproduce the results yourself.

## 🧩 Why This Portfolio Matters

Hiring for senior product roles often demands evidence of **both leadership and hands-on capability**.
This repo is my way of bridging that gap:
* **Leadership**: I’ve scaled multiple B2B SaaS products from concept to market leadership.
* **Technical**: I can directly design tracking, run SQL, set up billing, and orchestrate AI-driven growth experiments.

## 🔗 Connect with Me
* [LinkedIn](https://www.linkedin.com/in/joanoliverpoyatos/)
* [Portfolio of Products](https://qstcoop.org/)
* [Email](mailto:joan.poyatos@gmail.com)
