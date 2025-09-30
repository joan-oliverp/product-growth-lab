# Mock Dataset — Escaly Activation Funnel

This folder contains the **synthetic dataset** and generator used to reproduce the Escaly activation funnel analysis.

---

## 🎯 Purpose
The dataset simulates Escaly’s **activation funnel** so we can measure:
- Activation rate (Session 1).
- Time-to-activation (median minutes).
- Drop-off rates between funnel steps.

It is aligned with the **tracking plan** (`events.json`) defined in `tracking-plan-escaly/`.

---

## 🗂 Files
- **mock_data.csv** → Generated events table (one row per event).  
- **generate_mock_data.py** → Script to create the dataset.  
- **README.md** → Documentation (this file).  

---

## 📐 Schema (mock_data.csv)

| Column              | Type      | Notes |
|---------------------|-----------|-------|
| occurred_at         | timestamp | Event timestamp (UTC ISO 8601). |
| event               | string    | `signup_completed`, `select_scale`, `submit_assessment`, `generate_report`. |
| user_id             | string    | e.g. `u_00001`. |
| account_id          | string    | e.g. `a_00001`. |
| session_id          | string    | Groups events within a 30-min session window. |
| scale_id            | string    | Present from `select_scale` onwards. |
| assessment_id       | string    | For `submit_assessment` and `generate_report`. |
| report_id           | string    | For `generate_report` only. |
| channel             | enum      | `organic`, `paid_search`, `referral`, `email`, `direct`. |
| plan_tier           | enum      | `free`, `pro`, `business`. |
| method              | enum      | Signup method (`email_password`, `sso_google`, `sso_azure`). |
| is_email_verified   | boolean   | True/False (signup only). |
| status              | enum      | Assessment status (`started`, `in_progress`, `complete`). |
| format              | enum      | Report format (`web`, `pdf`). |
| generation_ms       | integer   | Report render time in ms. |
| device_type         | enum      | `desktop`, `mobile`, `tablet`. |
| locale              | string    | e.g. `en-US`, `es-ES`. |
| exp_onboarding_flow | string    | Experimental bucket (`control` for baseline). |

---

## 📊 Funnel Targets
The generator aims for realistic early-SaaS baselines:
- **Overall activation (Session 1):** 25–30%.  
- **Step-through rates:**  
  - Signup → Scale selected: ~80–85%.  
  - Scale → Assessment complete: ~55–65%.  
  - Assessment complete → Report generated: ~25–30%.  

**By channel (activation, Session 1):**
- Organic: 30–35%  
- Referral: 28–32%  
- Email: 24–28%  
- Direct: 22–26%  
- Paid search: 16–22%  

**By plan tier:**
- Business: 32–38%  
- Pro: 28–32%  
- Free: 20–26%  

---

## ⚙️ Usage

Generate a dataset:

```bash
cd case-studies/escaly-activation-funnel/mock-data/
python generate_mock_data.py --n_users 1500 --seed 42 --out mock_data.csv
