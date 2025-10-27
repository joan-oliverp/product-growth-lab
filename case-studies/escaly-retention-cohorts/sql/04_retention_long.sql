-- Create retention_long covering up to 12 weeks after the latest signup_week in cohorts
CREATE OR REPLACE TABLE retention_long AS
WITH params AS (
  -- global end = latest signup week + 12 weeks
  SELECT MAX(signup_week) + INTERVAL '12 week' AS global_end
  FROM cohorts
),
cohort_weeks AS (
  -- for each cohort, generate one row per week from signup_week up to global_end
  SELECT
    c.account_id,
    c.signup_week,
    date_diff('week', c.signup_week, gs.week_start_at) AS week_n,
    date_trunc('week', gs.week_start_at) AS week_start_at
  FROM cohorts c
  CROSS JOIN params p
  CROSS JOIN generate_series(c.signup_week, p.global_end, INTERVAL '1 week') AS gs(week_start_at)
)
SELECT
  cw.account_id,
  cw.signup_week,
  cw.week_n,
  COALESCE(o.is_active, FALSE) AS is_active
FROM cohort_weeks cw
LEFT JOIN org_weekly_active o
  ON o.account_id = cw.account_id
  AND o.week_start_at = cw.week_start_at
ORDER BY cw.account_id, cw.week_n;
