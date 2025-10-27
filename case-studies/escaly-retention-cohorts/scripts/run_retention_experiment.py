import duckdb, pathlib
import os
import pandas as pd

# Create a single connection
con = duckdb.connect()

# Print a specific table
def print_table(connection, table_name, sort_by=None, ascending=True):
    try:
        df = connection.execute(f"SELECT * FROM {table_name}").fetchdf()
        if sort_by:
            df = df.sort_values(by=sort_by, ascending=ascending)
        print(f"=== {table_name} ===")
        print(df.to_markdown(index=False))
        print("\n")
    except Exception as e:
        print(f"Error retrieving table {table_name}: {e}")

# Run setup script
setup_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/00_setup.sql').read_text()
con.execute(setup_sql)

# Run weekly activity aggregation script
weekly_activity_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/01_user_weekly_activity.sql').read_text()
con.execute(weekly_activity_sql)

# Run organization-level weekly activity script
org_weekly_active_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/02_org_weekly_active.sql').read_text()
con.execute(org_weekly_active_sql)

# Run segmentation script
segmentation_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/03_team_segment_w4.sql').read_text()
con.execute(segmentation_sql)

# Run longitudinal retention script
longitudinal_retention_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/04_retention_long.sql').read_text()
con.execute(longitudinal_retention_sql)

# Run retention matrix script
retention_matrix_sql = pathlib.Path('case-studies/escaly-retention-cohorts/sql/05_retention_matrix.sql').read_text()
con.execute(retention_matrix_sql)
print_table(con, "retention_matrix")  # Retention matrix table

# 1) Create figs dir and export the raw retention matrix as CSV
figs_dir = pathlib.Path("case-studies/escaly-retention-cohorts/figs")
figs_dir.mkdir(parents=True, exist_ok=True)

retention_matrix_df = con.execute("SELECT * FROM retention_matrix").fetchdf()
retention_matrix_csv = figs_dir / "retention_matrix.csv"
retention_matrix_df.to_csv(retention_matrix_csv, index=False)
print(f"💾 Wrote CSV: {retention_matrix_csv}")

# 2) Build a README-friendly summary table (weighted by cohort_size)
# Expected columns in retention_matrix: signup_week, team_seg, cohort_size, w0, w1, w2, w3, w4, w6, w8, w12
week_cols = [c for c in ["w1", "w4", "w8", "w12"] if c in retention_matrix_df.columns]
if not week_cols:
    print("⚠️ No week columns (w1/w4/w8/w12) found in retention_matrix; skipping README table/plot.")
else:
    def weighted_avg(group, col):
        return (group[col] * group["cohort_size"]).sum() / group["cohort_size"].sum()

    summary_rows = []
    for seg, g in retention_matrix_df.groupby("team_seg"):
        row = {"team_seg": seg}
        for col in week_cols:
            row[col] = round(weighted_avg(g, col), 1)
        summary_rows.append(row)

    summary_df = pd.DataFrame(summary_rows)
    # Print as Markdown for easy copy-paste into README
    print("=== README Table — Weighted Retention by Team Segment (paste into README) ===")
    print(summary_df.rename(columns={
        "team_seg": "Cohort Type",
        "w1": "Week 1",
        "w4": "Week 4",
        "w8": "Week 8",
        "w12": "Week 12"
    }).to_markdown(index=False))
    print("\n")

    # 3) Plot retention curve (by team segment, using weighted points)
    # Map available week columns to numeric x-axis
    col_to_week = {"w0":0, "w1":1, "w2":2, "w3":3, "w4":4, "w6":6, "w8":8, "w12":12}
    avail_weeks = sorted([col_to_week[c] for c in retention_matrix_df.columns if c in col_to_week])

    # Compute weighted averages per week for each team segment
    plot_rows = []
    for seg, g in retention_matrix_df.groupby("team_seg"):
        for col, wk in col_to_week.items():
            if col in retention_matrix_df.columns:
                val = weighted_avg(g, col)
                plot_rows.append({"team_seg": seg, "week_n": wk, "retention_pct": val})
    plot_df = pd.DataFrame(plot_rows)
    plot_df = plot_df[plot_df["week_n"].isin(avail_weeks)].sort_values(["team_seg","week_n"])

    # Plot with matplotlib (no custom colors/styles)
    try:
        import matplotlib.pyplot as plt
        plt.figure()
        for seg, seg_df in plot_df.groupby("team_seg"):
            plt.plot(seg_df["week_n"], seg_df["retention_pct"], marker="o", label=seg)
        plt.title("Escaly — 12-Week Retention by Team Segment")
        plt.xlabel("Weeks Since Signup")
        plt.ylabel("% of Active Organizations")
        plt.grid(alpha=0.3)
        plt.legend(title="Team Segment")
        out_png = figs_dir / "retention_curve.png"
        plt.savefig(out_png, bbox_inches="tight")
        print(f"📈 Saved figure: {out_png}")
    except Exception as e:
        print(f"⚠️ Could not generate plot (matplotlib missing?): {e}")
