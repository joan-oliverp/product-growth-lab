-- Cohorts
CREATE OR REPLACE TABLE cohorts AS
SELECT
  account_id,
  date_trunc('week', MIN(event_ts)) AS signup_week
FROM events
WHERE event_name = 'signup_completed'
GROUP BY 1;

-- Team size at week 4
WITH week_activity AS (
  SELECT
    q.account_id,
    q.week_start_at,
    COUNT(DISTINCT q.user_id) AS users_active
  FROM qualifying_events q
  JOIN cohorts c USING (account_id)
  GROUP BY q.account_id, q.week_start_at
),

/*
WITH week_activity AS (
  SELECT
    o.account_id,
    o.week_start_at,
    o.active_user_count AS users_active
    --COUNT(DISTINCT user_id) OVER (PARTITION BY o.account_id, o.week_start_at) AS users_active
  FROM org_weekly_active o
  JOIN cohorts c USING (account_id)
),*/
team_segment AS (
  SELECT
    account_id,
    CASE WHEN SUM(users_active > 0) FILTER (WHERE date_diff('week', c.signup_week, week_start_at) <= 4) >= 2
         THEN 'multi_user' ELSE 'single_user' END AS team_seg
  FROM week_activity w
  JOIN cohorts c USING (account_id)
  GROUP BY 1
),
retention_long AS (
  SELECT
    o.account_id,
    c.signup_week,
    date_diff('week', c.signup_week, o.week_start_at) AS week_n,
    o.is_active
  FROM org_weekly_active o
  JOIN cohorts c USING (account_id)
  WHERE week_n BETWEEN 0 AND 12
),
retention_matrix AS (
  SELECT
    c.signup_week,
    t.team_seg,
    week_n,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN is_active THEN o.account_id END)
           / COUNT(DISTINCT o.account_id), 1) AS retention_pct
  FROM retention_long o
  JOIN team_segment t USING (account_id)
  JOIN cohorts c USING (account_id)
  GROUP BY 1,2,3
)
SELECT * FROM retention_matrix
ORDER BY signup_week, team_seg, week_n;
