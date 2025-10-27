-- Cohort by account signup week
CREATE OR REPLACE TABLE cohorts AS
SELECT
  account_id,
  date_trunc('week', signup_completed_at) AS signup_week
FROM signup_events;

-- Team size by end of week 4 (weeks 0..4)
CREATE OR REPLACE TABLE team_size_w4 AS
WITH uw AS (
  SELECT
    uw.account_id,
    uw.user_id,
    uw.week_start_at,
    date_diff('week', c.signup_week, uw.week_start_at) AS week_n
  FROM user_weekly uw
  JOIN cohorts c USING (account_id)
)
SELECT account_id, COUNT(DISTINCT CASE WHEN week_n BETWEEN 0 AND 4 THEN user_id END) AS users_active_by_w4
FROM uw
GROUP BY 1;

-- Segment label
CREATE OR REPLACE TABLE team_segment AS
SELECT
  account_id,
  CASE WHEN users_active_by_w4 >= 2 THEN 'multi_user' ELSE 'single_user' END AS team_seg
FROM team_size_w4;
