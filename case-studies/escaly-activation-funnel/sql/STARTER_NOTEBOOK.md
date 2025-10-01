# STARTER_NOTEBOOK — Escaly Activation Funnel (SQL)

This notebook demonstrates how to analyze the **activation funnel** for Escaly using the synthetic dataset in  
[`../mock-data/mock_data.csv`](../mock-data/mock_data.csv).

---

## 🎯 Goals
- Define the activation funnel (Signup → Report).  
- Calculate **activation rate (Session 1)**.  
- Compute **median time-to-activation**.  
- Build a simple **funnel table**.  
- Segment activation by **channel** and **plan tier**.

---

## ⚙️ Setup (DuckDB in Codespaces)

Install DuckDB if needed:
```bash
pip install duckdb --quiet
```

Load CSV into DuckDB:
```sql
CREATE OR REPLACE TABLE mock_events AS
SELECT * FROM read_csv_auto('../mock-data/mock_data.csv', HEADER=TRUE);
```

---

## 📊 1) Quick Sanity Check
```sql
SELECT event, COUNT(*) AS n_events
FROM mock_events
GROUP BY 1
ORDER BY n_events DESC;
```
👉 Confirms expected counts of `signup_completed`, `select_scale`, `submit_assessment`, `generate_report`.

---

## 📈 2) Activation Rate (Session 1)

```sql
WITH signup AS (
  SELECT user_id, session_id AS signup_session_id, occurred_at, channel, plan_tier
  FROM mock_events
  WHERE event = 'signup_completed'
),
activated AS (
  SELECT DISTINCT s.user_id
  FROM signup s
  JOIN mock_events e
    ON e.user_id = s.user_id
   AND e.event = 'generate_report'
   AND e.session_id = s.signup_session_id
)
SELECT
  COUNT(*) AS signups,
  COUNT(a.user_id) AS activated_users,
  ROUND(100.0 * COUNT(a.user_id) / COUNT(*), 2) AS activation_rate_pct
FROM signup s
LEFT JOIN activated a USING (user_id);
```

---

## ⏱ 3) Median Time-to-Activation
```sql
WITH signup AS (
  SELECT user_id, session_id, occurred_at AS signup_at
  FROM mock_events
  WHERE event = 'signup_completed'
),
first_report AS (
  SELECT user_id, MIN(occurred_at) AS report_at
  FROM mock_events
  WHERE event = 'generate_report'
  GROUP BY user_id
),
durations AS (
  SELECT s.user_id,
         TIMESTAMPDIFF('minute', s.signup_at, f.report_at) AS tta_minutes
  FROM signup s
  JOIN first_report f USING (user_id)
)
SELECT
  APPROX_MEDIAN(tta_minutes) AS median_tta_minutes
FROM durations;
```

---

## 🔄 4) Funnel Table (Drop-offs)
```sql
WITH signup AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'signup_completed'
),
scale_selected AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'select_scale'
),
assessment_complete AS (
  SELECT DISTINCT user_id
  FROM mock_events
  WHERE event = 'submit_assessment' AND status = 'complete'
),
activated AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'generate_report'
),
counts AS (
  SELECT 'Signup Completed' AS step, COUNT(*) AS users_remaining FROM signup
  UNION ALL
  SELECT 'Scale Selected', COUNT(*) FROM scale_selected
  UNION ALL
  SELECT 'Assessment Completed', COUNT(*) FROM assessment_complete
  UNION ALL
  SELECT 'Report Generated (Activated)', COUNT(*) FROM activated
)
SELECT
  step,
  users_remaining,
  ROUND(100.0 * users_remaining / FIRST_VALUE(users_remaining) OVER (), 2) AS conversion_pct_from_start
FROM counts;
```

---

## 📊 5) Segmentation Examples
**By acquisition channel:**
```sql
WITH signup AS (
  SELECT user_id, session_id, channel
  FROM mock_events
  WHERE event = 'signup_completed'
),
activated AS (
  SELECT DISTINCT s.user_id
  FROM signup s
  JOIN mock_events e
    ON e.user_id = s.user_id
   AND e.event = 'generate_report'
   AND e.session_id = s.session_id
)
SELECT
  s.channel,
  COUNT(*) AS signups,
  COUNT(a.user_id) AS activated_users,
  ROUND(100.0 * COUNT(a.user_id) / COUNT(*), 2) AS activation_rate_pct
FROM signup s
LEFT JOIN activated a USING (user_id)
GROUP BY s.channel
ORDER BY activation_rate_pct DESC;
```
**By plan tier:**
```sql
WITH signup AS (
  SELECT user_id, session_id, plan_tier
  FROM mock_events
  WHERE event = 'signup_completed'
),
activated AS (
  SELECT DISTINCT s.user_id
  FROM signup s
  JOIN mock_events e
    ON e.user_id = s.user_id
   AND e.event = 'generate_report'
   AND e.session_id = s.session_id
)
SELECT
  s.plan_tier,
  COUNT(*) AS signups,
  COUNT(a.user_id) AS activated_users,
  ROUND(100.0 * COUNT(a.user_id) / COUNT(*), 2) AS activation_rate_pct
FROM signup s
LEFT JOIN activated a USING (user_id)
GROUP BY s.plan_tier
ORDER BY activation_rate_pct DESC;
```

---

## ✅ Next Steps
Export funnel table to CSV:
```sql
COPY (
  WITH counts AS (
    SELECT 'Signup Completed' AS step, COUNT(*) AS users_remaining FROM mock_events WHERE event='signup_completed'
    UNION ALL
    SELECT 'Report Generated (Activated)', COUNT(DISTINCT user_id) FROM mock_events WHERE event='generate_report'
  )
  SELECT * FROM counts
) TO '../outputs/funnel_table.csv' WITH (HEADER, DELIMITER ',');
```
