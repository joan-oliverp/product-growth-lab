#!/usr/bin/env python3
"""
generate_mock_data.py

Escaly — Activity 1.2: Retention Cohorts (Team Adoption)
Final mock data generator aligned with the tracking plan.

Events produced (canonical only):
  - signup_completed
  - submit_assessment
  - generate_report

CSV schema (headers):
  account_id,user_id,event_name,event_ts,report_id,assessment_id,scale_id

Key behavior modeling:
  - Organizations are split into single-user vs multi-user cohorts.
  - Multi-user orgs have higher weekly activity and slower decay.
  - A second (and third) user is likely to become active in weeks 0–4 for multi-user orgs.
  - Each active user-week may produce one submit_assessment and sometimes a generate_report.

Usage:
  python generate_mock_data.py \
      --accounts 120 \
      --weeks 12 \
      --start-date 2025-05-05 \
      --multi-share 0.45 \
      --seed 7 \
      --out case-studies/escaly-retention-cohorts/data/events.csv

"""

from __future__ import annotations

import argparse
import csv
import math
import random
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import List


# ----------------------------
# Config & small utilities
# ----------------------------

SCALES = ["sc_barthel", "sc_gencat", "sc_cope", "sc_quality_of_life"]

@dataclass
class OrgConfig:
    account_id: str
    signup: date
    users: List[str]
    is_multi: bool


def iso_dt(d: date, hour: int = 9, minute: int = 0) -> str:
    """Return ISO8601 UTC-like timestamp with trailing Z (no tz calc needed for mock)."""
    return datetime.combine(d, time(hour, minute)).isoformat() + "Z"


def week_start(d: date, weeks: int) -> datetime:
    """Week start (same weekday/time as signup reference) + n weeks."""
    return datetime.combine(d + timedelta(weeks=weeks), time(9, 0))


def choice(seq):
    return seq[random.randrange(len(seq))]


# ----------------------------
# Core generator
# ----------------------------

def build_orgs(
    n_accounts: int,
    start_date: date,
    signup_span_days: int,
    multi_share: float,
) -> List[OrgConfig]:
    """
    Create base orgs:
      - Distribute signups uniformly across signup_span_days.
      - Decide if org is multi-user (prob = multi_share).
      - Assign 1..5 users (single-user = 1; multi-user = 2..5 with skew to 2–3).
    """
    orgs = []
    for i in range(1, n_accounts + 1):
        acc = f"a{i}"
        signup = start_date + timedelta(days=random.randint(0, max(0, signup_span_days)))
        is_multi = random.random() < multi_share

        if is_multi:
            # Skew towards 2–3 users; occasionally 4–5
            size = random.choices([2, 3, 4, 5], weights=[0.55, 0.30, 0.10, 0.05], k=1)[0]
        else:
            size = 1

        users = [f"u{acc}_{j}" for j in range(1, size + 1)]
        orgs.append(OrgConfig(account_id=acc, signup=signup, users=users, is_multi=is_multi))
    return orgs


def emit_events(
    orgs: List[OrgConfig],
    weeks: int,
    base_p_single: float = 0.55,
    base_p_multi: float = 0.78,
    decay_single: float = 0.78,
    decay_multi: float = 0.95,
    report_prob: float = 0.65,
) -> List[dict]:
    """
    Emit events per org across weeks:
      - Week 0..weeks-1 relative to org.signup.
      - Per week, compute activity probability with decay; multi-user has higher base and slower decay.
      - If week in 0..4 and org is multi, encourage 2nd user activity (collaboration onset).
      - When active: emit submit_assessment, maybe generate_report.
    """
    rows: List[dict] = []

    for org in orgs:
        # 1) signup_completed by first user
        first_user = org.users[0]
        rows.append(dict(
            account_id=org.account_id,
            user_id=first_user,
            event_name="signup_completed",
            event_ts=iso_dt(org.signup, 9, 0),
            report_id="",
            assessment_id="",
            scale_id=""
        ))

        # Changed range to include the final week
        for w in range(weeks + 1):
            # Compute per-week activity probability by org type with exponential decay
            if org.is_multi:
                p = base_p_multi * (decay_multi ** w)
            else:
                p = base_p_single * (decay_single ** w)

            # Decide which users might be active
            wk_start = week_start(org.signup, w)

            candidate_users = [first_user]
            if org.is_multi and w <= 4:
                # Early collaboration: 50% chance to bring at least one more user
                if random.random() < 0.50 and len(org.users) > 1:
                    candidate_users.append(choice(org.users[1:]))

            # Occasionally involve a third user after week 2 (for larger teams)
            if org.is_multi and len(org.users) >= 3 and w >= 2 and random.random() < 0.25:
                candidate_users.append(choice(org.users[1:]))

            # De-duplicate user list
            candidate_users = list(dict.fromkeys(candidate_users))

            # Emit qualifying events for active users this week
            for u in candidate_users:
                if random.random() < p:
                    # submit_assessment
                    as_id = f"as_{org.account_id}_{w}_{u}"
                    scale_id = choice(SCALES)
                    rows.append(dict(
                        account_id=org.account_id,
                        user_id=u,
                        event_name="submit_assessment",
                        event_ts=(wk_start + timedelta(minutes=random.randint(5, 120))).isoformat() + "Z",
                        report_id="",
                        assessment_id=as_id,
                        scale_id=scale_id
                    ))
                    # Maybe generate_report (value moment)
                    if random.random() < report_prob:
                        rows.append(dict(
                            account_id=org.account_id,
                            user_id=u,
                            event_name="generate_report",
                            event_ts=(wk_start + timedelta(minutes=random.randint(121, 220))).isoformat() + "Z",
                            report_id=f"r_{org.account_id}_{w}_{u}",
                            assessment_id=as_id,
                            scale_id=scale_id
                        ))

    return rows


# ----------------------------
# CLI
# ----------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate mock events for Escaly Activity 1.2 (Retention Cohorts: Team Adoption)."
    )
    p.add_argument("--accounts", type=int, default=80, help="Number of organizations to simulate.")
    p.add_argument("--weeks", type=int, default=12, help="Number of weeks to simulate per organization.")
    p.add_argument("--start-date", type=str, default="2025-05-05", help="Signup start date (YYYY-MM-DD).")
    p.add_argument("--signup-span-days", type=int, default=21, help="Uniform spread (days) for signup window.")
    p.add_argument("--multi-share", type=float, default=0.45, help="Share of organizations that are multi-user.")
    p.add_argument("--seed", type=int, default=7, help="Random seed for reproducibility.")
    p.add_argument("--out", type=str, default="case-studies/escaly-retention-cohorts/data/events.csv", help="Output CSV path.")
    return p.parse_args()


def main():
    args = parse_args()
    random.seed(args.seed)

    start_date = date.fromisoformat(args.start_date)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    orgs = build_orgs(
        n_accounts=args.accounts,
        start_date=start_date,
        signup_span_days=args.signup_span_days,
        multi_share=args.multi_share,
    )

    rows = emit_events(orgs, weeks=args.weeks)

    # Write CSV
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["account_id", "user_id", "event_name", "event_ts", "report_id", "assessment_id", "scale_id"]
        )
        w.writeheader()
        w.writerows(rows)

    # Small console summary
    n_signup = sum(1 for r in rows if r["event_name"] == "signup_completed")
    n_submit = sum(1 for r in rows if r["event_name"] == "submit_assessment")
    n_report = sum(1 for r in rows if r["event_name"] == "generate_report")
    multi = sum(1 for o in orgs if o.is_multi)
    single = len(orgs) - multi

    print(f"✅ Wrote {len(rows):,} events to {out}")
    print(f"   Orgs: {len(orgs)}  (multi: {multi}, single: {single})")
    print(f"   signup_completed: {n_signup:,} | submit_assessment: {n_submit:,} | generate_report: {n_report:,}")


if __name__ == "__main__":
    main()
