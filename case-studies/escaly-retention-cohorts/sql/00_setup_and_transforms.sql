CREATE OR REPLACE TABLE events AS
SELECT * FROM read_csv_auto('case-studies/escaly-retention-cohorts/data/events.csv', header=True);


-- Base normalizations
UPDATE events SET event_ts = CAST(event_ts AS TIMESTAMP);

-- Qualifying usage events
CREATE OR REPLACE VIEW qualifying_events AS
SELECT account_id, user_id, event_name, date_trunc('week', event_ts) AS week_start_at
FROM events
WHERE event_name IN ('submit_assessment','generate_report');

-- Derived signal: org_weekly_active
CREATE OR REPLACE TABLE org_weekly_active AS
SELECT
  account_id,
  week_start_at,
  COUNT(DISTINCT user_id) AS active_user_count,
  active_user_count > 0 AS is_active
FROM qualifying_events
GROUP BY 1,2;
