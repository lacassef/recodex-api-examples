"""
Matches for one competition-sized day.

1. Page through scheduled-tournaments (page starts at 1) until hasNextPage is false.
2. Keep competitions whose timezoneEventCount for TZ_OFFSET is greater than 0.
3. Load that competition's matches. The id is tournament.uniqueTournament.id.

Football, cricket, tennis, and esports use scheduled-events/{YYYY-MM-DD}.
Esports has that form only. Other team sports use
/api/{sport}/tournament/{id}/schedules/{day}/{month}/{year}.

Run:
    export RAPIDAPI_KEY="your_key_here"
    pip install requests
    python day_schedule.py

    DAY=29 MONTH=9 YEAR=2026 TZ_OFFSET=0 python day_schedule.py
    RAPIDAPI_HOST=volleyballapi.p.rapidapi.com SPORT_PREFIX=/volleyball python day_schedule.py
"""

import os
import sys

import requests

HOST = os.environ.get("RAPIDAPI_HOST", "footapi7.p.rapidapi.com")
API_KEY = os.environ.get("RAPIDAPI_KEY")
SPORT_PREFIX = os.environ.get("SPORT_PREFIX", "")  # "" football, "/volleyball", "/esport"
DAY = int(os.environ.get("DAY", "29"))
MONTH = int(os.environ.get("MONTH", "9"))
YEAR = int(os.environ.get("YEAR", "2026"))
TZ_OFFSET = os.environ.get("TZ_OFFSET", "0")  # seconds east of UTC, as a string key


def get(path):
    if not API_KEY:
        sys.exit("Set RAPIDAPI_KEY in your environment first.")
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": HOST}
    resp = requests.get(f"https://{HOST}{path}", headers=headers, timeout=20)
    if resp.status_code == 204:
        return None
    resp.raise_for_status()
    return resp.json()


def scheduled_tournaments():
    page = 1
    while True:
        data = get(
            f"/api{SPORT_PREFIX}/scheduled-tournaments/{DAY}/{MONTH}/{YEAR}/page/{page}"
        )
        if not data:
            return
        for row in data.get("scheduled") or []:
            yield row
        if not data.get("hasNextPage"):
            return
        page += 1


# Esports publishes the ISO date form only. Football, cricket, and tennis publish both.
ISO_DATE = {"", "/cricket", "/esport", "/tennis"}


def events_for(unique_tournament_id):
    if SPORT_PREFIX in ISO_DATE:
        path = (
            f"/api{SPORT_PREFIX}/tournament/{unique_tournament_id}/scheduled-events/"
            f"{YEAR:04d}-{MONTH:02d}-{DAY:02d}"
        )
    else:
        path = (
            f"/api{SPORT_PREFIX}/tournament/{unique_tournament_id}/schedules/"
            f"{DAY}/{MONTH}/{YEAR}"
        )
    data = get(path) or {}
    return data.get("events") or []


def main():
    kept = 0
    for row in scheduled_tournaments():
        counts = row.get("timezoneEventCount") or {}
        if int(counts.get(TZ_OFFSET) or 0) <= 0:
            continue
        tournament = row.get("tournament") or {}
        unique = tournament.get("uniqueTournament") or {}
        unique_id = unique.get("id")
        if unique_id is None:
            continue
        name = unique.get("name") or tournament.get("name")
        events = events_for(unique_id)
        kept += 1
        print(f"\n{name} ({len(events)} events)")
        for ev in events:
            home = (ev.get("homeTeam") or {}).get("name", "?")
            away = (ev.get("awayTeam") or {}).get("name", "?")
            status = (ev.get("status") or {}).get("description", "")
            print(f"  {ev.get('id')}  {home} vs {away}  {status}")
    print(f"\n{kept} competitions for offset {TZ_OFFSET}")


if __name__ == "__main__":
    main()
