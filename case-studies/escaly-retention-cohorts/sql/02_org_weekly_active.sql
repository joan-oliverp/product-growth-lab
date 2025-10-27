-- Warehouse-derived signal (org_weekly_active)
CREATE OR REPLACE TABLE org_weekly_active AS
SELECT
  account_id,
  week_start_at,
  COUNT(DISTINCT user_id) AS active_user_count,
  active_user_count > 0 AS is_active
FROM user_weekly
GROUP BY 1,2;
