-- time_to_activation_by_segment.sql
-- Median time-to-activation segmented by channel and plan tier (DuckDB)

WITH signup AS (
  SELECT
    user_id,
    session_id AS signup_session_id,
    CAST(occurred_at AS TIMESTAMP) AS signup_at,
    channel,
    plan_tier
  FROM mock_events
  WHERE event = 'signup_completed'
),
first_report_same_session AS (
  SELECT
    s.user_id,
    MIN(CAST(e.occurred_at AS TIMESTAMP)) AS report_at
  FROM signup s
  JOIN mock_events e
    ON e.user_id = s.user_id
   AND e.event = 'generate_report'
   AND e.session_id = s.signup_session_id
  GROUP BY s.user_id
),
durations AS (
  SELECT
    s.user_id,
    s.channel,
    s.plan_tier,
    (EXTRACT(EPOCH FROM (fr.report_at - s.signup_at)) / 60.0) AS tta_minutes
  FROM signup s
  JOIN first_report_same_session fr
    ON fr.user_id = s.user_id
)
SELECT
  channel,
  plan_tier,
  COUNT(*) AS activated_users,
  ROUND(median(tta_minutes), 2) AS median_tta_minutes,
  ROUND(avg(tta_minutes), 2) AS mean_tta_minutes
FROM durations
GROUP BY channel, plan_tier
ORDER BY channel, plan_tier;
