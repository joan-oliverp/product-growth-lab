-- funnel.sql
-- Escaly Activation Funnel
-- Outputs step-by-step user counts and conversion percentages
-- Run with: python ../scripts/run_duckdb.py funnel.sql

WITH signup AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'signup_completed'
),
scale_selected AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'select_scale'
),
assessment_complete AS (
  SELECT DISTINCT user_id FROM mock_events WHERE event = 'submit_assessment' AND status = 'complete'
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
),
base AS (
  SELECT MAX(users_remaining) AS total_signups FROM counts
)
SELECT
  c.step,
  c.users_remaining,
  ROUND(100.0 * c.users_remaining / b.total_signups, 2) AS conversion_pct_from_start
FROM counts c
CROSS JOIN base b
ORDER BY CASE c.step
           WHEN 'Signup Completed' THEN 1
           WHEN 'Scale Selected' THEN 2
           WHEN 'Assessment Completed' THEN 3
           WHEN 'Report Generated (Activated)' THEN 4
         END;
