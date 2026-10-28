"""
Filter a day's schedule to a specific time zone — the code companion to the FAQ
"Why do schedule endpoints return matches from the previous/next day?" (../FAQ.md).

startTimestamp is Unix seconds in UTC. A viewer's local day is the half-open
window local midnight <= startTimestamp < local midnight + 86400. This example
fetches the UTC dates at offsets -1, 0 and +1, then keeps events inside that window.

Football has no sport-wide day list: GET /api/matches/{day}/{month}/{year} is
discontinued. Other sports still publish GET /api/{sport}/matches/{day}/{month}/{year}
or GET /api/{sport}/events/{day}/{month}/{year}. This example assembles one day from
a few categories, which is the right call when you only follow some countries.
Two options (see ../DailyMatches.md):

  1. By category:    /api/{sport}/category/{id}/events/{day}/{month}/{year}
                     (football: /api/category/{id}/events/{day}/{month}/{year})
  2. By tournament:  /api/{sport}/tournament/{id}/scheduled-events/{YYYY-MM-DD}
                     (football, cricket, esport, tennis)

This example uses option 1 over a configurable set of categories (default: football
category 1 = England). Enumerate every category via /api/{sport}/tournament/categories
(see list_all_leagues.py) and extend CATEGORY_IDS to widen coverage.

Run:
    export RAPIDAPI_KEY="your_key_here"
    pip install requests
    python filter_schedule_by_timezone.py            # defaults below
"""

import os
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests

HOST = os.environ.get("RAPIDAPI_HOST", "footapi7.p.rapidapi.com")
BASE_URL = f"https://{HOST}"
API_KEY = os.environ.get("RAPIDAPI_KEY")

# "" for football (footapi7); set to e.g. "/tennis" for another sport (and switch HOST).
SPORT_PREFIX = os.environ.get("SPORT_PREFIX", "")
# Categories (countries/tours) to assemble the day's schedule from. Comma-separated.
CATEGORY_IDS = [int(c) for c in os.environ.get("CATEGORY_IDS", "1").split(",") if c.strip()]


def get(path, *, timeout=15):
    if not API_KEY:
        sys.exit("Set RAPIDAPI_KEY in your environment first.")
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": HOST}
    resp = requests.get(f"{BASE_URL}{path}", headers=headers, timeout=timeout)
    if resp.status_code == 204:
        return None
    resp.raise_for_status()
    return resp.json()


def fetch_schedule(day, month, year):
    """All events on a UTC date across CATEGORY_IDS (deduped).

    Union each category's schedule and dedupe by event id. Swap to
    /api{SPORT_PREFIX}/tournament/{uniqueTournamentId}/scheduled-events/{YYYY-MM-DD}
    (or .../schedules/{day}/{month}/{year}) to drive it by competition. The id is
    uniqueTournament.id.
    """
    events, seen = [], set()
    for cat_id in CATEGORY_IDS:
        data = get(f"/api{SPORT_PREFIX}/category/{cat_id}/events/{day}/{month}/{year}")
        for ev in (data or {}).get("events", []):
            if ev["id"] not in seen:
                seen.add(ev["id"])
                events.append(ev)
    return events


def matches_for_local_day(year, month, day, tz_name):
    """Return events that kick off on the given local calendar day, sorted by time."""
    tz = ZoneInfo(tz_name)
    local_start = datetime(year, month, day, tzinfo=tz)
    local_end = local_start + timedelta(days=1)
    start_ts, end_ts = int(local_start.timestamp()), int(local_end.timestamp())

    # The local day can overlap up to three UTC calendar dates. Fetch all and dedupe.
    seen, events = set(), []
    for offset in (-1, 0, 1):
        d = local_start + timedelta(days=offset)
        for ev in fetch_schedule(d.day, d.month, d.year):
            ts = ev.get("startTimestamp")
            if ev["id"] in seen or ts is None:
                continue
            if start_ts <= ts < end_ts:
                seen.add(ev["id"])
                events.append(ev)

    events.sort(key=lambda e: e.get("startTimestamp", 0))
    return events, tz


def main():
    # Defaults: today's date, Tokyo time. Override via env if you like.
    tz_name = os.environ.get("TZ_NAME", "Asia/Tokyo")
    today = datetime.now(ZoneInfo(tz_name))
    year = int(os.environ.get("YEAR", today.year))
    month = int(os.environ.get("MONTH", today.month))
    day = int(os.environ.get("DAY", today.day))

    events, tz = matches_for_local_day(year, month, day, tz_name)
    cats = ",".join(map(str, CATEGORY_IDS))
    print(f"{len(events)} matches on {year}-{month:02d}-{day:02d} "
          f"({tz_name}) across categories {cats}\n")
    for ev in events:
        kickoff = datetime.fromtimestamp(ev["startTimestamp"], tz)
        home, away = ev["homeTeam"]["name"], ev["awayTeam"]["name"]
        print(f"{kickoff:%H:%M}  {home} vs {away}")


if __name__ == "__main__":
    main()
