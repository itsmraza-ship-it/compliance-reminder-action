#!/usr/bin/env python3
"""Quick local check: how many days remain until a compliance deadline?

Usage:
    python3 scripts/check.py --deadline-date 2027-04-01 --warn-days 30

Exit codes: 0 = plenty of time, 1 = within warning window, 2 = overdue or invalid date.
"""

import argparse
import sys
from datetime import date


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Days remaining until a compliance deadline.")
    p.add_argument("--deadline-date", required=True, help="Deadline in YYYY-MM-DD format")
    p.add_argument("--warn-days", type=int, default=30, help="Warning window in days")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        deadline = date.fromisoformat(args.deadline_date)
    except ValueError:
        print(f"Invalid date: {args.deadline_date}. Use YYYY-MM-DD.", file=sys.stderr)
        return 2

    days = (deadline - date.today()).days

    if days < 0:
        print(f"OVERDUE by {-days} day(s). Deadline was {args.deadline_date}.")
        return 2
    if days <= args.warn_days:
        print(f"Due soon: {days} day(s) remaining (deadline {args.deadline_date}).")
        return 1
    print(f"OK: {days} day(s) remaining (deadline {args.deadline_date}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
