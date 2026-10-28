# Matches on a date

Two calls cover a normal day. One lists the competitions that have matches. The next lists the matches in the competitions you care about.

Football has no sport-wide day list. `GET /api/matches/{day}/{month}/{year}` is discontinued. Build the football day from scheduled tournaments, then the competition schedule. That walk is below.

Other sports still publish one list for the whole sport, when you want every match and you do not need to pick competitions first:

- Team sports and esports: `GET /api/{sport}/matches/{day}/{month}/{year}`
- Tennis, table tennis, badminton, darts, snooker, padel: `GET /api/{sport}/events/{day}/{month}/{year}`

`{day}` and `{month}` are not zero-padded. The body is `{ "events": [ ... ] }`. A `204` means nothing is scheduled.

That list is in UTC for the date you asked. A kickoff near midnight can fall on the previous or next local day. Filter with `event.startTimestamp`. The [timezone example](Examples/filter_schedule_by_timezone.py) does that.

The competition walk below is also the one to use when the sport-wide list is larger than you need, or when you already follow a set of leagues.

## Quick reference

| Sport | Competitions on that day | Matches for one competition |
|-------|--------------------------|-----------------------------|
| Football | `GET /api/scheduled-tournaments/{day}/{month}/{year}/page/{page}` | `GET /api/tournament/{uniqueTournamentId}/scheduled-events/{YYYY-MM-DD}` or `.../schedules/{day}/{month}/{year}` |
| Team sports | `GET /api/{sport}/scheduled-tournaments/{day}/{month}/{year}/page/{page}` | `GET /api/{sport}/tournament/{uniqueTournamentId}/schedules/{day}/{month}/{year}` |
| Cricket and tennis | the same scheduled-tournaments call | `schedules/{day}/{month}/{year}` or `scheduled-events/{YYYY-MM-DD}` |
| Esports | `GET /api/esport/scheduled-tournaments/{day}/{month}/{year}/page/{page}` | `GET /api/esport/tournament/{uniqueTournamentId}/scheduled-events/{YYYY-MM-DD}` only |
| Tennis, table tennis | `GET /api/{sport}/calendar/{day}/{month}/{year}/categories` | `GET /api/{sport}/category/{id}/events/{day}/{month}/{year}` |
| MMA | `GET /api/mma/main-events/{YYYY-MM-DD}/extended` | one card, no second step |
| Motorsport | `GET /api/motorsport/stage/scheduled/{YYYY-MM-DD}` | `GET /api/motorsport/stage/{id}/substages` |
| Cycling | no by-date list | team, then season, then races |

Team sports here: american-football, aussie-rules, bandy, baseball, basketball, beach-volley, cricket, floorball, futsal, handball, ice-hockey, minifootball, rugby, volleyball, and waterpolo. Esports uses the same tournament index and the ISO date form only.

The runnable version of the team-sport walk is [Examples/day_schedule.py](Examples/day_schedule.py).

## Scheduled tournaments

`page` starts at **1**.

```json
{
  "scheduled": [
    {
      "tournament": {
        "id": 137866,
        "name": "Campeonato Mineiro",
        "uniqueTournament": { "id": 23389, "name": "Campeonato Mineiro" }
      },
      "timezoneEventCount": { "0": 1, "3600": 1, "7200": 0 }
    }
  ],
  "hasNextPage": false
}
```

Read pages until `hasNextPage` is false or `scheduled` is empty.

`tournament.id` is the group or edition on that day. `tournament.uniqueTournament.id` is the competition id. Pass **`uniqueTournament.id`** to `schedules` and `scheduled-events`.

`timezoneEventCount` maps a timezone offset, in seconds east of UTC, to how many of this competition's events fall on that local day. The key is a string. UTC is `"0"`. UTC+2 is `"7200"`. UTC−3 is `"-10800"`. Skip a competition when your viewers' offset is missing or `0`.

Then:

```text
GET /api/volleyball/tournament/23389/schedules/29/9/2026
```

Football, cricket, esports, and tennis also accept an ISO date:

```text
GET /api/tournament/23389/scheduled-events/2026-09-29
```

The body is `{ "events": [ ... ] }`. Dedupe by `event.id` if you merge several competitions.

## By category

Use this when you want one country or one tour, and you already know the category id.

1. `GET /api/tournament/categories` (football) or `GET /api/{sport}/tournament/categories`.
2. `GET /api/category/{categoryId}/events/{day}/{month}/{year}` or `GET /api/{sport}/category/{categoryId}/events/{day}/{month}/{year}`.

MMA, cycling, and motorsport list categories on their own prefix: `/api/mma/categories`, `/api/cycling/categories`, `/api/motorsport/categories`.

Cache the category list. It changes slowly.

Tennis and table tennis can skip the full category list. `GET /api/{sport}/calendar/{day}/{month}/{year}/categories` returns only the categories that have play that day. Then call the category events route for each id.

## MMA

`GET /api/mma/main-events/{YYYY-MM-DD}/extended` returns `{ "events": [ ... ] }` for that date.

To walk one promotion:

1. `GET /api/mma/categories`
2. `GET /api/mma/category/{categoryId}/unique-tournaments`
3. `GET /api/mma/unique-tournament/{uniqueTournamentId}/schedules/{day}/{month}/{year}`

The month form is `.../schedules/{month}/{year}`. Months that have cards: `GET /api/mma/calendar/unique-tournament/{id}/{timezoneOffset}/months-with-events`. `timezoneOffset` is seconds east of UTC.

The tournaments route returns groups:

```json
{ "groups": [ { "uniqueTournaments": [ { "id": 19906, "name": "UFC" } ] } ] }
```

## Motorsport

A stage is a race weekend.

- `GET /api/motorsport/stage/scheduled/{YYYY-MM-DD}`
- `GET /api/motorsport/categories`
- `GET /api/motorsport/category/{categoryId}/stages/all`
- `GET /api/motorsport/stage/{stageId}`
- `GET /api/motorsport/stage/{stageId}/substages`
- `GET /api/motorsport/stage/featured` for the next highlighted event

## Cycling

There is no route that takes a calendar date and returns every race.

1. `GET /api/cycling/search/{term}` or `GET /api/search/all?q={term}&sport=cycling&page=0`
2. `GET /api/cycling/team/{teamId}/stage/seasons`
3. `GET /api/cycling/team/{teamId}/stage/season/{seasonId}/races`
4. `GET /api/cycling/stage/{stageId}` for one race

`GET /api/calendar/season/{seasonId}/{year}/days-with-events` tells you which days in that season have something on the calendar, so you can skip empty dates.

## Live, and days that have matches

| Need | Route |
|------|-------|
| In play now | `GET /api/matches/live`, `GET /api/{sport}/matches/live`, or `GET /api/{sport}/events/live` |
| Competitions in play | `GET /api/tournaments/live` or `GET /api/{sport}/tournaments/live` |
| Categories in play | `GET /api/tournament/categories/live` or `GET /api/{sport}/tournament/categories/live` |
| Days in a season that have matches | `GET /api/calendar/season/{seasonId}/{year}/days-with-events` |
| How many events each sport has today, for one offset | `GET /api/sport/event-count/{timezoneOffset}` |

`event-count` returns one number per sport slug. The offset is seconds east of UTC, for example `0` or `7200`. It is not a sport name.
