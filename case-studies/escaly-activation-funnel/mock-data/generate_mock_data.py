#!/usr/bin/env python3
import argparse, csv, random, uuid
from datetime import datetime, timedelta, timezone

# -------------------------
# Config (distributions)
# -------------------------

CHANNEL_DIST = {
    "organic": 0.4, "paid_search": 0.25, "referral": 0.1, "email": 0.15, "direct": 0.1
}
PLA_DIST = {"free": 0.65, "pro":0.25, "business": 0.05}
DEVICE_DIST = {"desktop": 0.7, "mobile": 0.25, "tablet": 0.05}
LOCALES = ["en-US", "es-ES", "ca-ES", "fr-FR"]
SCALES = [("sc_101", "GENCAT"), ("sc_102", "Barthel"), ("sc_103", "GHQ-12"), ("sc_104", "Geriatric Depression Scale (GDS)"), ("sc_105", "Mini-Mental State Examination (MMSE)")]

# Signup auth mix
SIGNUP_AUTH_DIST = {"email_password": 0.6, "sso_google": 0.3, "sso_azure": 0.1}

# Target step-through probabilities (overall)
P_SELECT = 0.83     # reach select_scale
P_ASSESS_COMPLETE = 0.60  # reach submit_assessment complete
P_ACTIVATE = 0.27   # reach generate_report

# Channel multipliers for activation odds (directional)
CHANNEL_ACTIVATION_MULT = {
    "organic": 1.2, "paid_search": 0.7, "referral": 1.1, "email": 1.0, "direct": 0.9
}

# Plan multipliers
PLAN_ACTIVATION_MULT = {"free": 0.85, "pro": 1.1, "business": 1.25}

# Time deltas (minutes) — bounds used for uniform sampling
DELTA_SELECT = (1, 5)
DELTA_ASSESS_STARTED = (3, 10)
DELTA_ASSESS_INPROG = (5, 20)
DELTA_ASSESS_COMPLETE = (8, 25)
DELTA_REPORT = (9, 30)  # from signup

SESSION_TIMEOUT_MIN = 30

def choice_from_dist(d):
    r = random.random()
    cum = 0
    for k, p in d.items():
        cum += p
        if r <= cum:
            return k
    return list(d.keys())[-1]

def iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def generate_users(n_users, start_date, end_date):
    """Yield user dicts with signup timestamp and attributes."""
    span = (end_date - start_date).days
    for i in range(n_users):
        signup_day = start_date + timedelta(days=random.randint(0, max(0, span)))
        signup_time = signup_day + timedelta(
            hours=random.randint(8, 20), minutes=random.randint(0, 59), seconds=random.randint(0, 59)
        )
        channel = choice_from_dist(CHANNEL_DIST)
        plan = choice_from_dist(PLAN_DIST)
        device = choice_from_dist(DEVICE_DIST)
        locale = random.choice(LOCALES)
        method = choice_from_dist(METHOD_DIST)
        email_verified = True if method != "email_password" else (random.random() < 0.95)

        yield {
            "user_id": f"u_{i:05d}",
            "account_id": f"a_{i:05d}",
            "signup_at": signup_time.replace(tzinfo=timezone.utc),
            "channel": channel,
            "plan_tier": plan,
            "device_type": device,
            "locale": locale,
            "method": method,
            "is_email_verified": email_verified,
        }

def activation_probability(base=P_ACTIVATE, channel=None, plan=None):
    m = 1.0
    if channel in CHANNEL_ACTIVATION_MULT: m *= CHANNEL_ACTIVATION_MULT[channel]
    if plan in PLAN_ACTIVATION_MULT: m *= PLAN_ACTIVATION_MULT[plan]
    # Convert multiplicative factor to bounded probability around base
    p = max(0.01, min(0.95, base * m))
    return p

def within_session(t0, t_next):
    return (t_next - t0).total_seconds() <= SESSION_TIMEOUT_MIN * 60

def emit_event(rows, occurred_at, event, base, **kwargs):
    row = {
        "occurred_at": iso(occurred_at),
        "event": event,
        "anonymous_id": "",
        "user_id": base["user_id"],
        "account_id": base["account_id"],
        "session_id": base["session_id"],
        "scale_id": kwargs.get("scale_id", ""),
        "assessment_id": kwargs.get("assessment_id", ""),
        "report_id": kwargs.get("report_id", ""),
        "channel": base["channel"],
        "plan_tier": base["plan_tier"],
        "utm_source": kwargs.get("utm_source", ""),
        "utm_medium": kwargs.get("utm_medium", ""),
        "utm_campaign": kwargs.get("utm_campaign", ""),
        "method": kwargs.get("method", ""),
        "is_email_verified": kwargs.get("is_email_verified", ""),
        "status": kwargs.get("status", ""),
        "format": kwargs.get("format", ""),
        "generation_ms": kwargs.get("generation_ms", ""),
        "device_type": base["device_type"],
        "locale": base["locale"],
        "exp_onboarding_flow": "control",
    }
    rows.append(row)

def generate(args):
    random.seed(args.seed)
    start_date = datetime.fromisoformat(args.start + "T00:00:00+00:00")
    end_date = datetime.fromisoformat(args.end + "T00:00:00+00:00")

    rows = []
    for u in generate_users(args.n_users, start_date, end_date):
        session_id = f"s_{uuid.uuid4().hex[:8]}"
        u["session_id"] = session_id

        # Signup
        emit_event(rows, u["signup_at"], "signup_completed", u,
                   method=u["method"], is_email_verified=u["is_email_verified"])

        # Step: select_scale
        if random.random() < P_SELECT:
            scale_id, _ = random.choice(SCALES)
            t_select = u["signup_at"] + timedelta(minutes=random.randint(*DELTA_SELECT))
            if not within_session(u["signup_at"], t_select):
                continue  # session ended before step
            u["scale_id"] = scale_id
            emit_event(rows, t_select, "select_scale", u, scale_id=scale_id)

            # Step: submit_assessment (complete) — optionally emit started/in_progress
            reached_complete = random.random() < P_ASSESS_COMPLETE
            if reached_complete:
                assess_id = f"as_{uuid.uuid4().hex[:10]}"
                # started
                t_started = u["signup_at"] + timedelta(minutes=random.randint(*DELTA_ASSESS_STARTED))
                if within_session(u["signup_at"], t_started):
                    emit_event(rows, t_started, "submit_assessment", u,
                               scale_id=scale_id, assessment_id=assess_id, status="started")
                # in_progress
                t_inprog = u["signup_at"] + timedelta(minutes=random.randint(*DELTA_ASSESS_INPROG))
                if within_session(u["signup_at"], t_inprog):
                    emit_event(rows, t_inprog, "submit_assessment", u,
                               scale_id=scale_id, assessment_id=assess_id, status="in_progress")
                # complete
                t_complete = u["signup_at"] + timedelta(minutes=random.randint(*DELTA_ASSESS_COMPLETE))
                if not within_session(u["signup_at"], t_complete):
                    continue
                emit_event(rows, t_complete, "submit_assessment", u,
                           scale_id=scale_id, assessment_id=assess_id, status="complete")

                # Step: generate_report (activation) — channel/plan adjusted
                p_act = activation_probability(P_ACTIVATE, u["channel"], u["plan_tier"])
                if random.random() < p_act:
                    t_report = u["signup_at"] + timedelta(minutes=random.randint(*DELTA_REPORT))
                    if within_session(u["signup_at"], t_report):
                        report_id = f"r_{uuid.uuid4().hex[:10]}"
                        generation_ms = random.randint(500, 4000)
                        fmt = "web" if random.random() < 0.8 else "pdf"
                        emit_event(rows, t_report, "generate_report", u,
                                   scale_id=scale_id, assessment_id=assess_id,
                                   report_id=report_id, format=fmt, generation_ms=generation_ms)

    # Sort and write
    rows.sort(key=lambda r: r["occurred_at"])
    fieldnames = ["occurred_at","event","anonymous_id","user_id","account_id","session_id",
                  "scale_id","assessment_id","report_id","channel","plan_tier","utm_source",
                  "utm_medium","utm_campaign","method","is_email_verified","status","format",
                  "generation_ms","device_type","locale","exp_onboarding_flow"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {args.out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Escaly activation funnel mock events.")
    parser.add_argument("--n_users", type=int, default=1500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--start", type=str, default="2025-08-01", help="YYYY-MM-DD (UTC)")
    parser.add_argument("--end", type=str, default="2025-09-15", help="YYYY-MM-DD (UTC)")
    parser.add_argument("--out", type=str, default="mock_data.csv")
    args = parser.parse_args()
    generate(args)