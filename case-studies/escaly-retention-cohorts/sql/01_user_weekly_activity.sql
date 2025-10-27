-- Distinct user-week activity from qualifying events
CREATE OR REPLACE TABLE user_weekly AS
SELECT DISTINCT account_id, user_id, week_start_at
FROM qualifying_events;
