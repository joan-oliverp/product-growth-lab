-- Cohort sizes = number of accounts per team segment
CREATE OR REPLACE TABLE cohort_sizes AS
SELECT team_seg, COUNT(DISTINCT account_id) AS cohort_size
FROM team_segment
GROUP BY 1;

-- Aggregate by segment only (combining signup weeks)
CREATE OR REPLACE TABLE retention_matrix AS
WITH base AS (
  SELECT
    ts.team_seg,
    r.week_n,
    COUNT(DISTINCT CASE WHEN r.is_active THEN r.account_id END) AS orgs_active
  FROM retention_long r
  JOIN team_segment ts USING (account_id)
  GROUP BY 1,2
)
SELECT
  b.team_seg,
  cs.cohort_size,
  MAX(CASE WHEN week_n = 0  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w0,
  MAX(CASE WHEN week_n = 1  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w1,
  MAX(CASE WHEN week_n = 2  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w2,
  MAX(CASE WHEN week_n = 3  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w3,
  MAX(CASE WHEN week_n = 4  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w4,
  MAX(CASE WHEN week_n = 6  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w6,
  MAX(CASE WHEN week_n = 8  THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w8,
  MAX(CASE WHEN week_n = 12 THEN ROUND(100.0 * orgs_active / cs.cohort_size, 1) END) AS w12
FROM base b
JOIN cohort_sizes cs USING (team_seg)
GROUP BY 1,2
ORDER BY 1;
