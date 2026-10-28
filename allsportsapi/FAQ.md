# FAQ

Short answers for people calling the API. Start with the [README](README.md) if you have not made a request yet. Field lists are in [Models](Models/README.md). Step-by-step calls are in [Workflows](Workflows.md).

**Contents**

- [Where can I subscribe?](#where-can-i-subscribe)
- [How do I get live and pre-match data?](#how-do-i-get-live-and-pre-match-data)
- [How do I get player statistics from a match?](#how-do-i-get-player-statistics-from-a-match)
- [How do I display images?](#how-do-i-display-images)
- [How do I determine the match time?](#how-do-i-determine-the-match-time)
- [Do you provide betting odds?](#do-you-provide-betting-odds)
- [How do I interpret incidents and status?](#how-do-i-interpret-incidents-and-status)
- [How do I navigate the API?](#how-do-i-navigate-the-api)
- [Why are there no widgets?](#why-are-there-no-widgets)
- [How do I get all leagues of a sport?](#how-do-i-get-all-leagues-of-a-sport)
- [How do I retrieve all teams in a league?](#how-do-i-retrieve-all-teams-in-a-league)
- [How do I get all matches on a date?](#how-do-i-get-all-matches-on-a-date)
- [Why do I see matches from the previous or next day?](#why-do-i-see-matches-from-the-previous-or-next-day)
- [Which page number do I send?](#which-page-number-do-i-send)
- [What does 204 mean, and what does an error look like?](#what-does-204-mean-and-what-does-an-error-look-like)
- [What is customId?](#what-is-customid)
- [How do I search?](#how-do-i-search)
- [What if the data I need is missing?](#what-if-the-data-i-need-is-missing)
- [What do transfer types mean?](#what-do-transfer-types-mean)
- [Where can I get help?](#where-can-i-get-help)

---

## Where can I subscribe?

| Marketplace | What's available |
|-------------|------------------|
| [RapidAPI](https://rapidapi.com/fluis.lacasse) | The All Sports bundle and every single-sport API that has its own listing |
| [API.market](https://api.market/store/recodex/allsportsapi) | The All Sports bundle only |

The host you send in `X-RapidAPI-Host` is on the product page. The [README](README.md) lists the hosts that are published today. Paths are the same on the bundle and on a single-sport product.

---

## How do I get live and pre-match data?

Live and pre-match detail is on the match routes: the event itself, statistics, incidents, lineups, odds, form, and highlights. The map is in [Workflows](Workflows.md#one-match).

The list of matches that are in play right now:

- Football: `GET /api/matches/live`
- Team sports and esports: `GET /api/{sport}/matches/live`
- Tennis, table tennis, badminton, darts, snooker, padel: `GET /api/{sport}/events/live`

Pre-match data for a match that has not started is on the same detail routes. Many of them return `204` until the match is close enough to have that data (no lineup yet, no odds yet).

---

## How do I get player statistics from a match?

On a team sport, `GET /api/match/{id}/lineups` (with the sport prefix) returns every player and, once the match has numbers, a `statistics` object on each player.

A single player, where the sport publishes it: `GET /api/match/{id}/player/{playerId}/statistics`.

Badminton, darts, snooker, and padel do not have lineups. Use `GET /api/{sport}/event/{id}/point-by-point`.

Season totals are a different route. See [Workflows](Workflows.md#season-player-statistics).

---

## How do I display images?

Image routes return bytes. `Content-Type` is `image/png`, `image/webp`, or `image/svg+xml` for a placeholder. They require the two auth headers, so an `<img>` tag pointed at the route will be rejected.

1. **Fetch the bytes** and use a blob or object URL as the image source.
2. **Base64**, if you need a data URL.
3. **Your own server**, which adds the key and serves the bytes to the browser. This is the one to use in production.
4. **Canvas**, if you need to draw on the image.

Working code is in [Examples](Examples/).

---

## How do I determine the match time?

`status`, `lastPeriod`, and `time` sit on the event, next to each other. `time` is often an empty object when the match is not in progress. Then the clock is just `status.description`.

### Fields

- **`status.code`** is the numeric code.
- **`status.description`** is the label, for example `1st half`.
- **`status.type`** is the coarse state: `inprogress`, `finished`, `notstarted`, and the others listed under incidents below.
- **`lastPeriod`** is the current period, for example `period1`.
- **`time.initial`** is the offset before the period starts, often `0`.
- **`time.max`** is the regular length of the period in seconds. `2700` is 45 minutes.
- **`time.extra`** is allocated added time, in seconds.
- **`time.currentPeriodStartTimestamp`** is the Unix second when the current period started.
- **`time.injuryTime`** is the added time the referee has given, in minutes, when it is published.

### Elapsed time

When `status.type` is `inprogress`, `lastPeriod` names the current period, and `currentPeriodStartTimestamp` is greater than 0:

```text
elapsed = nowSeconds - time.currentPeriodStartTimestamp
```

`nowSeconds` is your clock in Unix seconds. If that elapsed value is greater than `time.max`, the difference is added time.

```text
added = elapsed - time.max
```

A football half with `time.max` of `2700` and an elapsed time of `2800` is 45 minutes plus 100 seconds.

If the period is already over, use the recorded length `time.initial + time.max + time.extra` for that period.

### Example

```json
{
  "status": { "code": 6, "description": "1st half", "type": "inprogress" },
  "lastPeriod": "period1",
  "time": {
    "initial": 0,
    "max": 2700,
    "extra": 540,
    "currentPeriodStartTimestamp": 1727861400
  }
}
```

If the current Unix time is `1727862000`, elapsed time is `600` seconds (10 minutes).

The [match clock example](Examples/match_clock.py) runs this offline on a sample event.

All timestamps are Unix seconds. If `currentPeriodStartTimestamp` is missing or `0`, do not subtract it. Period names run `period1` through `period7`. Use the ones that sport actually plays.

---

## Do you provide betting odds?

Yes. The full board for an event is `GET /api/match/{id}/odds/{providerId}/all`. Provider `1` is the default board. The short `GET /api/match/{id}/odds` route, on the sports that have it, is that same board.

`204` means that event has no odds. Markets with `suspended: true` should not be shown as live prices.

Books for a country: `GET /api/odds/providers/{countryCode}/web`. `countryCode` is alpha-2.

Cycling and motorsport put odds on the stage: `GET /api/{sport}/stage/{id}/odds/provider/{providerId}/all`.

The shape and the other odds routes are in [Workflows](Workflows.md#odds).

Pinaculo and Uniodds, on RapidAPI, are separate products when you need a dedicated odds feed.

---

## How do I interpret incidents and status?

### Incidents

`GET /api/match/{id}/incidents` returns `{ "incidents": [ ... ] }`. Read `incidentType`, then `incidentClass` or `text`.

Football values you will see:

| `incidentType` | `incidentClass` or `text` |
|----------------|---------------------------|
| `goal` | `regular`, `penalty`, `ownGoal` |
| `card` | `yellow`, `red`, `yellowRed` |
| `substitution` | `injury`, or no class |
| `period` | `text` is `HT`, `FT`, `ET`, `PEN`, or a period name such as `1. set` |
| `injuryTime` | the added minutes |
| `varDecision` | `goalAwarded`, `penaltyNotAwarded`, `cardUpgrade`, plus `confirmed` |
| `inGamePenalty` | `missed` |
| `penaltyShootout` | `scored`, `missed` |

Other sports add their own types. Cricket uses `incidentType` `ball`, with `incidentClass` such as `4`, `6`, `W`, or `WD`. A set sport uses `period` rows with the set score in `homeScore` and `awayScore`.

The full field list is [Models/Incidents.md](Models/Incidents.md).

### Status

`status` has three fields.

`code` is an integer. Codes you can rely on for football and the sports that share its clock:

| Code | Meaning |
|------|---------|
| 0 | Not started |
| 6 | 1st half, in progress (the description confirms the period) |
| 31 | Halftime |
| 32 | Awaiting extra time |
| 33 | Extra-time halftime |
| 34 | Awaiting penalties |
| 40 | Overtime |
| 41 | First extra-time period |
| 42 | Second extra-time period |
| 50 | Penalties |
| 100 | Ended |
| 110 | After extra time |
| 120 | After penalties |

`type` is `inprogress`, `finished`, `notstarted`, `postponed`, `canceled`, `interrupted`, `suspended`, `delayed`, `willcontinue`, or `preliminary`.

`description` is the text to show. It varies by sport: `1st half`, `2nd half`, `Halftime`, `Ended`, `Postponed`, `Not started`, `AET`, `AP`, `1st set`, `FT`.

Other sports use further codes. A set uses `8` for `1st set`. Cricket uses `21` for `1st Inning`. `60` is postponed and `70` is canceled when those states apply. Prefer `type` for logic and `description` for the label. Do not switch on description text alone.

`winnerCode` after the match has a result: `1` home won, `2` away won, `3` draw.

---

## How do I navigate the API?

Pick one sport. The tree is the same.

```text
category  →  unique tournament  →  season  →  event
(country or tour)  (the competition)  (one edition)  (one match)
```

Football paths omit the sport name. Every other sport uses `/api/{sport}/...`. Esports uses the slug `esport`.

Four groups cover most screens:

- **Matches** are schedules, lineups, statistics, incidents, highlights, odds.
- **Teams** are squads, results, logos, transfers.
- **Players** are profiles, season stats, photos.
- **Managers** are career, photo, recent matches.

The path table is in the [README](README.md#path-rules). One sport's routes are in its file under [openapi](openapi/).

---

## Why are there no widgets?

A widget in the page would need your key in the browser. Call the API from your server and render the HTML yourself. The [proxy examples](Examples/) are the starting point. We help you wire that up while you are building.

---

## How do I get all leagues of a sport?

1. Categories: `GET /api/tournament/categories` or `GET /api/{sport}/tournament/categories`.
   MMA, cycling, and motorsport use `/api/mma/categories`, `/api/cycling/categories`, and `/api/motorsport/categories`.
2. Tournaments in one category: `GET /api/tournament/all/category/{categoryId}` or `GET /api/{sport}/tournament/all/category/{categoryId}`.
   MMA uses `GET /api/mma/category/{categoryId}/unique-tournaments`.

The tournaments body is grouped:

```json
{
  "groups": [
    { "uniqueTournaments": [ { "id": 17, "name": "Premier League", "slug": "premier-league" } ] }
  ]
}
```

Flatten `groups[].uniqueTournaments`. Some responses also put `uniqueTournaments` at the top. Read whichever key is present. The id you keep is `uniqueTournament.id`.

`GET /api/tournament/categories/all` includes categories that have no live match. The shorter `categories` route is the one most screens need.

The [list-all-leagues example](Examples/list_all_leagues.py) does this walk. Cache the result for hours or days.

---

## How do I retrieve all teams in a league?

The clubs in one season:

```text
GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/teams
```

The table, with a `team` on every row:

```text
GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/standings/total
```

Prefix the sport when it is not football. A competition with groups returns several objects inside `standings`. Read every `rows` array. Each row's `team.id` is the id for the squad and the logo.

The squad of one team is `GET /api/team/{id}/players`.

---

## How do I get all matches on a date?

Football has no sport-wide day list. `GET /api/matches/{day}/{month}/{year}` is discontinued. Build that day from scheduled tournaments, then the competition schedule. The recipe is [DailyMatches.md](DailyMatches.md).

Other sports still publish one list for the whole sport:

```text
GET /api/basketball/matches/7/3/2026       a team sport
GET /api/tennis/events/7/3/2026            tennis, and the other event sports
```

Use the competition walk when you want specific leagues, or when you want to skip competitions that have no matches in the viewer's timezone. The full recipe, including MMA, motorsport, and cycling, is [DailyMatches.md](DailyMatches.md).

The id on `schedules` and `scheduled-events` is `tournament.uniqueTournament.id` from the scheduled-tournaments row, not `tournament.id`.

---

## Why do I see matches from the previous or next day?

`startTimestamp` is a Unix second. The date you put in the path is a calendar date, read in UTC. A match at 23:30 UTC is still that UTC date, and it is already the next day in UTC+2. A match at 00:30 UTC is the previous evening in the Americas.

Keep an event when this is true:

```text
localMidnight <= startTimestamp < localMidnight + 86400
```

`localMidnight` is midnight in the viewer's timezone, converted to Unix seconds. The [filter example](Examples/filter_schedule_by_timezone.py) does this, including the neighboring UTC date when the local day crosses midnight UTC.

On `scheduled-tournaments`, `timezoneEventCount` already answers "does this competition have a match on that local day?". The key is the offset in seconds east of UTC, as a string. `"7200"` is UTC+2. Skip rows whose count for that key is `0` or missing.

---

## Which page number do I send?

| Route | First page | Stop when |
|-------|------------|-----------|
| `scheduled-tournaments/.../page/{page}` | 1 | `hasNextPage` is false, or `scheduled` is empty |
| Team, player, or manager `previous/{page}` and `next/{page}` | 0 | `204`, or `events` is empty |
| Season `matches/last/{page}` and `matches/next/{page}` (football and team sports). Event sports use `events/last` and `events/next` | 0 | `204`, or the list is empty |
| `GET /api/search/{entityType}?page=` | 0 | the page is short, or `204` |
| Season player `statistics?page=&limit=` | 1 | the page is shorter than `limit`. `limit` is required from page 2 |

Sending page `1` to a 0-based route skips the first page. Sending page `0` to scheduled-tournaments or to season statistics is the wrong page.

---

## What does 204 mean, and what does an error look like?

`204` means the route is valid and there is nothing for those parameters: no match that day, no lineup yet, no odds, an unknown id, an empty search. The body is empty. Do not call `response.json()` on it. Do not retry it.

`400` means a path or query value is not valid (a month of `13`, a bad page). Fix the request.

```json
{ "error": { "status": 400, "title": "Bad Request", "request_id": "…" } }
```

A bad date on some routes returns a one-line text body instead of that JSON. Either way, the status is `400`.

`401` and `403` come from the marketplace: the key is missing, wrong, or does not match the host.

`429` is the plan limit. Wait for `Retry-After` when it is set, otherwise back off.

`500`, `502`, `503`, and `504` are temporary. Retry with backoff. The JSON uses the same `error` object, with `title` `Internal Server Error`, `Bad Gateway`, `Service Unavailable`, or `Gateway Timeout`. Include `request_id` if you ask us about one of these.

---

## What is customId?

`id` is the numeric event id. Use it for the match, lineups, statistics, incidents, and odds.

`customId` is a short string on the same event, for example `BLcsubhd`. Use it only for head-to-head:

```text
GET /api/match/{customId}/h2h
GET /api/tennis/event/{customId}/h2h
```

The two ids are not interchangeable.

---

## How do I search?

```text
GET /api/search/all?q=arsenal&page=0
GET /api/search/teams?q=arsenal&page=0&sport=football
GET /api/basketball/search/lakers?page=0
```

`page` starts at 0. `sport` is the slug (`football`, `ice-hockey`, `esport`, `table-tennis`). Entity types are `all`, `teams`, `player-team-persons`, `events`, `unique-tournaments`, `news`, `managers`, `referees`, `venues`.

Take the id from the result and call the detail route. Do not keep searching to render a page you already have an id for.

---

## What if the data I need is missing?

A `204` on a detail route usually means that match, team, or season does not have that data. Coverage depends on the sport and the competition. A lower league often has a score and no shotmap, no odds, and no player ratings.

If the fact is not in these routes at all, the [Allscores API](https://rapidapi.com/fluis.lacasse/api/allscores/) is a different product and a different JSON shape. Ask us either way. If a route should have returned data and you got `502` or `504`, send the path and the `request_id`.

---

## What do transfer types mean?

On a transfer, `type` is a number.

| `type` | Meaning |
|--------|---------|
| 1 | Loan |
| 2 | End of loan |
| 3 | Permanent transfer |

The rest of the fields are in [Models/Transfer.md](Models/Transfer.md).

---

## Where can I get help?

The About tab of the API on RapidAPI, or the listing on [API.market](https://api.market/store/recodex/allsportsapi). Help during development is free.
