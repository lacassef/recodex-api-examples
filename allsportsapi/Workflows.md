# Workflows

Sequences for the calls people make first. Paths below are football. Add the sport slug for every other sport (`/api/basketball/...`), and use `event` instead of `match` when the [path table](README.md#path-rules) says so. Send `X-RapidAPI-Key` and `X-RapidAPI-Host` on every call.

A `204` is an empty result. Stop that branch. Do not retry it.

## Live board

1. `GET /api/matches/live`
2. Read `events`. Each item has `id`, `homeTeam`, `awayTeam`, `homeScore`, `awayScore`, `status`, `startTimestamp`, and `tournament`.
3. Poll this route every 10–30 seconds while you are showing a live screen.
4. For a match the user opens, continue with [one match](#one-match).

`status.type` is the coarse state: `notstarted`, `inprogress`, `finished`, `postponed`, `canceled`, `interrupted`, `suspended`, `delayed`, `willcontinue`, `preliminary`. `status.description` is the label to print (`1st half`, `Ended`, `Halftime`). `status.code` is the numeric code. See the [FAQ](FAQ.md#how-do-i-interpret-incidents-and-status).

While `status.type` is `inprogress`, `time` carries the clock. On a finished match `time` is often `{}`. The clock recipe is in the [FAQ](FAQ.md#how-do-i-determine-the-match-time).

## One match

You need `event.id` from a list, from search, or from a team fixture.

| What you want | Route | Body |
|---------------|-------|------|
| Core object | `GET /api/match/{id}` | `{ "event": { ... } }` |
| Timeline | `GET /api/match/{id}/incidents` | `{ "incidents": [ ... ] }` |
| Lineups and player stats | `GET /api/match/{id}/lineups` | `confirmed`, `home`, `away` |
| Team stats | `GET /api/match/{id}/statistics` | periods, then groups, then items |
| Odds, full board | `GET /api/match/{id}/odds/1/all` | `{ "markets": [ ... ], "eventId": ... }` |
| Odds, short list | `GET /api/match/{id}/odds/1/featured` | `{ "featured": ..., "hasMoreOdds": true }` |
| Previous meetings | `GET /api/match/{customId}/h2h` | `{ "events": [ ... ] }` |
| Head-to-head totals | `GET /api/match/{id}/duel` | `teamDuel`, `managerDuel` |
| Recent form | `GET /api/match/{id}/form` | `homeTeam` and `awayTeam`, each with `form` (`W`, `D`, `L`) |
| Highlight clips | `GET /api/match/{id}/highlights` | clip list |
| Commentary | `GET /api/match/{id}/commentary` | football. Other sports use `.../comments` |
| Win probability | `GET /api/match/{id}/win-probability` | graph points |

`customId` comes from the event. It looks like `BLcsubhd`. The numeric `id` will not work on the head-to-head route.

Lineups, for a team sport:

```json
{
  "confirmed": true,
  "home": {
    "players": [
      {
        "player": { "id": 123, "name": "Example", "position": "M" },
        "teamId": 42,
        "position": "M",
        "substitute": false,
        "statistics": { "rating": 7.4, "goals": 1 }
      }
    ]
  },
  "away": { "players": [] }
}
```

`confirmed` is false while the sheet is provisional. `statistics` is empty until the match has numbers. Badminton, darts, snooker, and padel do not publish lineups. They publish `GET /api/{sport}/event/{id}/point-by-point`. Padel also has `.../tennis-power`.

Player totals for one match are on the lineup entry. A single player is also at `GET /api/match/{id}/player/{playerId}/statistics` where that route exists (see the OpenAPI file for the sport).

A score object uses `current` for the match score and `period1`, `period2`, ... for the parts. `display` is the number to print when the sport's score is not the sum of the periods (sets won, for example).

```json
{
  "id": 17101340,
  "customId": "BLcsubhd",
  "startTimestamp": 1790654400,
  "status": { "code": 100, "description": "Ended", "type": "finished" },
  "winnerCode": 1,
  "homeTeam": { "id": 392569, "name": "Uzbekistan", "nameCode": "UZB" },
  "awayTeam": { "id": 392570, "name": "Opponent", "nameCode": "OPP" },
  "homeScore": { "current": 3, "display": 3, "period1": 25, "period2": 25, "period3": 25 },
  "awayScore": { "current": 1, "display": 1, "period1": 22, "period2": 23, "period3": 18 },
  "tournament": {
    "id": 68040,
    "name": "Asian Games, Pool A",
    "uniqueTournament": { "id": 11344, "name": "Asian Games" }
  },
  "season": { "id": 103682, "name": "Asian Games 2026", "year": "2026" }
}
```

`winnerCode` `1` means the home side won. `2` means the away side won. `3` is a draw. The field is absent until there is a result.

## League table and fixtures

From the event, take `tournament.uniqueTournament.id` and `season.id`.

| What you want | Route |
|---------------|-------|
| Table | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/standings/total` |
| Home or away table | `.../standings/home`, `.../standings/away` |
| Seasons of a competition | `GET /api/tournament/{uniqueTournamentId}/seasons` |
| Clubs in the season | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/teams` |
| Rounds | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/rounds` |
| Matches in a round | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/matches/round/{round}` |
| Upcoming and recent | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/matches/next/0` and `.../matches/last/0` |

Tennis, table tennis, badminton, darts, snooker, and padel use `events` instead of `matches` on those last three routes (`.../events/last/0`, `.../events/next/0`).

Standings:

```json
{
  "standings": [
    {
      "name": "Name of the table",
      "rows": [
        {
          "position": 1,
          "matches": 20,
          "wins": 14,
          "draws": 3,
          "losses": 3,
          "scoresFor": 40,
          "scoresAgainst": 15,
          "points": 45,
          "team": { "id": 42, "name": "Example" }
        }
      ]
    }
  ]
}
```

Draws and points appear for sports that use them. A baseball or volleyball row uses wins, losses, and the score columns instead. `team.id` is the id for the squad and the logo.

`matches/last/{page}` and `matches/next/{page}` (or `events/...` on the event sports) are **0-based**. Page `0` is the first page. Stop on `204` or an empty list.

## Find an id

`GET /api/search/{entityType}?q={text}&page=0`

`entityType` is one of: `all`, `teams`, `player-team-persons`, `events`, `unique-tournaments`, `news`, `managers`, `referees`, `venues`.

`page` is **0-based**. Add `sport=basketball` (the slug) to stay inside one sport. A sport product also has `GET /api/{sport}/search/{term}?page=0`, which searches that sport only.

Suggestions, while the user is still typing: `GET /api/search/suggestions/{entityType}?q={text}`.

Store the id you pick. Do not search again on every page view.

## Odds

1. List the books for a country: `GET /api/odds/providers/{countryCode}/{type}`
   `countryCode` is an alpha-2 code such as `GB`. `type` is `web`, `web-featured`, or `web-odds`.
2. Full board for one event: `GET /api/match/{id}/odds/{providerId}/all`
   Provider `1` is the default board. The short route `GET /api/match/{id}/odds` is that same board on the sports that publish it.
3. Featured prices only: `GET /api/match/{id}/odds/{providerId}/featured`
4. Featured events for a sport, ordered by popularity: `GET /api/matches/odds/featured-by-popularity/{providerId}`
   Tennis, table tennis, and MMA use `/events/odds/featured-by-popularity/{providerId}`.

```json
{
  "eventId": 16814491,
  "markets": [
    {
      "marketName": "Full time",
      "marketGroup": "1X2",
      "marketPeriod": "Full-time",
      "isLive": false,
      "suspended": false,
      "choices": [
        { "name": "1", "fractionalValue": "7/4", "initialFractionalValue": "11/10" }
      ]
    }
  ]
}
```

`name` is the selection (`1`, `X`, `2`, or a player or total). `fractionalValue` is the current price. `initialFractionalValue` is the opening price. Skip a market when `suspended` is true. `204` means that event has no odds.

Cycling and motorsport hang odds on the stage: `GET /api/cycling/stage/{id}/odds/provider/{providerId}/all` and the same shape under `/api/motorsport/stage/{id}/odds/provider/{providerId}/all`.

For a deeper odds feed, Pinaculo and Uniodds are separate products on RapidAPI.

## Season player statistics

Football route: `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/statistics`

| Query | Rule |
|-------|------|
| `page` | Starts at **1**. Page 1 is the first page |
| `limit` | Page size. Required from page 2 onward. `20` is a sensible size |
| `order` | A statistic name. A leading minus sorts descending, for example `-rating` |
| `group` | `summary`, `attack`, `defence`, `passing`, or `goalkeeper`. Leave it out on the detailed view |
| `accumulation` | `total`, `perGame`, or `per90` |
| `minApps` | `yes`, or omit the parameter |
| `fields` | Comma-separated statistic names for the detailed view |
| `filters` | Comma-separated `field.operator.value` conditions |

`operator` is `GT`, `LT`, `EQ`, or `in`. Several values inside one `in` are joined with `~`.

```text
position.in.G~D~M~F,type.EQ.home
```

`position` is `G`, `D`, `M`, `F`. `type` is `home` or `away`. `preferredFoot` is `Both`, `Right`, or `Left`. `appearances` and `age` take a number. `team` takes team ids. `nationality` takes country codes.

The statistic names that exist for that season are at `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/player-statistics/types`.

## Images

| Image | Route |
|-------|-------|
| Team logo | `GET /api/team/{id}/image` |
| Player photo | `GET /api/player/{id}/image` |
| Manager photo | `GET /api/manager/{id}/image` |
| Competition logo | `GET /api/tournament/{uniqueTournamentId}/image` |
| Dark logo | `.../image/dark` where the sport publishes it |
| Country flag | `GET /api/country/{alpha2}/flag` |

Prefix the sport on team, player, manager, and tournament images when the sport is not football. Padel photos are `GET /api/padel/player/{id}/image`. Badminton, darts, and snooker photos are `GET /api/{sport}/team/{id}/image`.

The body is bytes. Cache them. The [image notes](Examples/README.md) show fetch-as-blob and a server proxy.

## A team page

1. `GET /api/team/{id}`
2. `GET /api/team/{id}/players` for the squad (team sports).
3. `GET /api/team/{id}/matches/near` for the fixtures around today.
4. `GET /api/team/{id}/matches/previous/0` and `.../next/0` for older and newer pages. Page `0` is first.
5. `GET /api/team/{id}/image` for the logo.
6. `GET /api/team/{id}/standings/seasons` when you want every table that team appears in.

Transfers: `GET /api/team/{id}/transfers?page=1&sort=-transferFee`. `type` on a transfer is `1` loan, `2` end of loan, `3` permanent. Details are in [Models/Transfer.md](Models/Transfer.md).
