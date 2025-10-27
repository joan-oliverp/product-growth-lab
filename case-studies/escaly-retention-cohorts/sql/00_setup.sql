-- Create event table from CSV (tiny dataset first; later overwrite)
CREATE OR REPLACE TABLE events AS
SELECT * FROM read_csv_auto('case-studies/escaly-retention-cohorts/data/events.csv', header=True);

-- Normalize types
UPDATE events
SET event_ts = CAST(event_ts AS TIMESTAMP);

-- Helpful views
CREATE OR REPLACE VIEW signup_events AS
SELECT account_id, MIN(event_ts) AS signup_completed_at
FROM events
WHERE event_name = 'signup_completed'
GROUP BY account_id;

CREATE OR REPLACE VIEW qualifying_events AS
SELECT account_id, user_id, event_name, event_ts,
       date_trunc('week', event_ts) AS week_start_at
FROM events
WHERE event_name IN ('submit_assessment','generate_report');
