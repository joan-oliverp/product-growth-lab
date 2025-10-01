#!/usr/bin/env python3
"""
run_duckdb.py — lightweight SQL runner for mock_data.csv

Usage:
  python run_duckdb.py ../sql/funnel.sql
"""

import sys
import duckdb
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_duckdb.py <query.sql>")
        sys.exit(1)

    sql_file = sys.argv[1]
    if not os.path.exists(sql_file):
        print(f"❌ SQL file not found: {sql_file}")
        sys.exit(1)

    # Connect to in-memory DuckDB
    con = duckdb.connect()

    # Load CSV into a table
    con.execute("""
    CREATE OR REPLACE TABLE mock_events AS
    SELECT * FROM read_csv_auto('../mock-data/mock_data.csv', HEADER=TRUE);
    """)

    # Read SQL query from file
    with open(sql_file, "r") as f:
        query = f.read()

    print(f"▶ Running {sql_file}...\n")
    try:
        res = con.execute(query).fetchdf()
        print(res.to_markdown(index=False))   # pretty print
    except Exception as e:
        print(f"❌ Error running query: {e}")

if __name__ == "__main__":
    main()
