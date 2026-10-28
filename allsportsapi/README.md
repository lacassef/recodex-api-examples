# AllSportsAPI

Live scores, fixtures, lineups, statistics, standings, and odds, with the same paths and the same JSON shapes across sports.

Learn one sport and the others follow. Football is the exception: its paths have no sport name. Every other sport puts the sport slug after `/api`.

## Where to subscribe

| Marketplace | What you can buy |
|-------------|------------------|
| [RapidAPI](https://rapidapi.com/fluis.lacasse) | The **All Sports** bundle and each single-sport API |
| [API.market](https://api.market/store/recodex/allsportsapi) | The **All Sports** bundle only |

Single-sport products (Football, Tennis, Basketball, and the others that have their own listing) are on RapidAPI. API.market sells the bundle only.

Copy `X-RapidAPI-Host` from the endpoint snippet on the product page. The hosts below are the ones published today.

| Product | Host |
|---------|------|
| All Sports | `allsportsapi2.p.rapidapi.com` |
| Football | `footapi7.p.rapidapi.com` |
| Tennis | `tennisapi1.p.rapidapi.com` |
| Basketball | `basketapi1.p.rapidapi.com` |
| Ice Hockey | `icehockeyapi.p.rapidapi.com` |
| American Football | `americanfootballapi.p.rapidapi.com` |
| Baseball | `baseballapi.p.rapidapi.com` |
| Cricket | `cricketapi21.p.rapidapi.com` |
| Esports | `esportapi1.p.rapidapi.com` |
| Motorsport | `motorsportapi.p.rapidapi.com` |
| Rugby | `rugbyapi2.p.rapidapi.com` |
| Volleyball | `volleyballapi.p.rapidapi.com` |
| Handball | `handballapi.p.rapidapi.com` |
| MMA | `mmaapi.p.rapidapi.com` |

Aussie rules, badminton, bandy, beach volleyball, cycling, darts, floorball, futsal, minifootball, padel, snooker, table tennis, and water polo are on the All Sports bundle. If a sport also has its own listing, use the host printed on that listing.

## Authentication

Every request needs two headers.

| Header | Value |
|--------|-------|
| `X-RapidAPI-Key` | Your key |
| `X-RapidAPI-Host` | The host of the product you subscribed to |

Keep the key on your server. A browser, a mobile app, or a public repository can leak it. The [server proxy examples](Examples/server_proxy_flask.py) show the pattern.

```bash
curl --request GET \
  --url 'https://footapi7.p.rapidapi.com/api/matches/live' \
  --header 'X-RapidAPI-Key: YOUR_API_KEY' \
  --header 'X-RapidAPI-Host: footapi7.p.rapidapi.com'
```

On the bundle, the same call is `https://allsportsapi2.p.rapidapi.com/api/matches/live` with host `allsportsapi2.p.rapidapi.com`. Paths do not change between the bundle and a single-sport product.

## Path rules

`{day}`, `{month}`, and `{year}` are numbers. `7/3/2026` is 7 March 2026. Do not zero-pad them. Where a path uses `{date}`, the value is `YYYY-MM-DD`.

| Family | Sports | One event | A day's list | Person or club |
|--------|--------|-----------|--------------|----------------|
| Football | football | `/api/match/{id}` | `/api/matches/...` | `/api/player/{id}`, `/api/team/{id}` |
| Team sports | american-football, aussie-rules, bandy, baseball, basketball, beach-volley, cricket, floorball, futsal, handball, ice-hockey, minifootball, rugby, volleyball, waterpolo | `/api/{sport}/match/{id}` | `/api/{sport}/matches/...` | `/api/{sport}/player/{id}`, `/api/{sport}/team/{id}` |
| Esports | esport | `/api/esport/event/{id}` | `/api/esport/matches/...` | `/api/esport/team/{id}` |
| Matches and sets | tennis, table-tennis | `/api/{sport}/event/{id}` | `/api/{sport}/events/...` | `/api/{sport}/player/{id}` (tennis also has `/team/{id}`) |
| Individual, published as a team | badminton, darts, snooker | `/api/{sport}/event/{id}` | `/api/{sport}/events/...` | `/api/{sport}/team/{id}` |
| Padel | padel | `/api/padel/event/{id}` | `/api/padel/events/...` | `/api/padel/player/{id}` |
| Fight cards | mma | `/api/mma/event/{id}` | `/api/mma/main-events/{date}/extended` | rankings and events under `/api/mma` |
| Stages | cycling, motorsport | `/api/{sport}/stage/{id}` | see [DailyMatches.md](DailyMatches.md) | team and rider routes under that prefix |

The esports slug in the path is `esport`, one word, no final `s`.

Badminton, darts, and snooker do not have a separate player route or a lineup route. The athlete id is the id on `/team/{id}`. Padel uses `/player/{id}` for that same kind of id.

## What a response looks like

A `200` body is the payload itself. A match list is `{ "events": [ ... ] }`. One match is `{ "event": { ... } }`. A table is `{ "standings": [ ... ] }`. Categories are `{ "categories": [ ... ] }`. There is no `head` wrapper around the payload.

Fields that do not apply to the sport are missing or `null`. Read nested objects only after you check them.

`startTimestamp` is Unix time in seconds. Treat it as UTC when you convert it to a local clock.

Image routes return bytes, not JSON. `Content-Type` is `image/png`, `image/webp`, or `image/svg+xml` for a placeholder. Send the same two auth headers. An `<img src>` cannot send them. See [Examples](Examples/).

Successful responses may include `Cache-Control`, `ETag`, and `Last-Modified`. Reuse them. Error responses do not carry cache headers.

## Status codes

| Code | Meaning | What to do |
|------|---------|------------|
| 200 | Payload or image bytes | Read the body |
| 204 | The route exists and there is nothing for those parameters | Empty body. Do not parse JSON. Treat it as an empty list or a missing image |
| 400 | A path or query value is invalid | Fix the request. The body is JSON `{"error":{"status":400,"title":"Bad Request","request_id":"..."}}`, or a short text line for a bad date |
| 401, 403 | Key or host rejected by the marketplace | Check the key and `X-RapidAPI-Host` |
| 429 | Plan limit | Wait. Honor `Retry-After` when it is present, then back off |
| 500 | Unexpected failure | Retry with backoff |
| 502 | The data could not be fetched | Retry with backoff |
| 503 | Temporarily unavailable | Retry with backoff |
| 504 | The request timed out | Retry with backoff |

`request_id` is present when the error body includes one. Send it when you ask for help.

The [quickstart](Examples/quickstart.py) retries 429 and 5xx and treats 204 as no data.

## Ids you will reuse

| Id | Where you get it | Where you send it |
|----|------------------|-------------------|
| `event.id` | Any list of events | `/match/{id}` or `/event/{id}`, then lineups, incidents, statistics, odds |
| `event.customId` | The same event object | Head-to-head. This is a short string, not the numeric id |
| `event.tournament.uniqueTournament.id` | The event, or a scheduled-tournament row | Seasons, standings, a competition's matches on a date |
| `event.tournament.id` | The event | The edition or group playing that match. Do not send this id to a unique-tournament route |
| `event.season.id` | The event | `/season/{seasonId}/...` |
| `homeTeam.id`, `awayTeam.id` | The event | Team, squad, and logo routes |
| `player.id` | Lineups, squads, search | Player routes. On padel, badminton, darts, and snooker this is the participant id described above |
| Category `id` | `/tournament/categories` | Tournaments in that country or tour, and that category's matches on a date |

`winnerCode` on a finished event: `1` the home side won, `2` the away side won, `3` draw. It is absent before the match has a result.

## Common tasks

| Goal | Start here |
|------|------------|
| Live matches | `GET /api/matches/live` for football, `GET /api/{sport}/matches/live` for team sports and esports, `GET /api/{sport}/events/live` for tennis, table tennis, badminton, darts, snooker, and padel |
| One day's matches | [DailyMatches.md](DailyMatches.md) |
| One match | [Workflows.md](Workflows.md) |
| Every league | Categories, then the tournaments in each category. See the [FAQ](FAQ.md) |
| A league table | `GET /api/tournament/{uniqueTournamentId}/season/{seasonId}/standings/total` (prefix the sport when the sport is not football) |
| Odds | `GET /api/match/{id}/odds/{providerId}/all` or the short `.../odds` route. Provider `1` is the default board |
| A name, when you do not have an id | `GET /api/search/all?q={text}&page=0` |
| A logo or a photo | `GET /api/team/{id}/image`, `GET /api/player/{id}/image`, with the sport prefix when needed |

Worked sequences are in [Workflows.md](Workflows.md). Questions that come up on every integration are in the [FAQ](FAQ.md).

## Reading the rest of this folder

| Path | Use it for |
|------|------------|
| [FAQ.md](FAQ.md) | Auth, images, the match clock, incidents, leagues, dates, pages, errors |
| [DailyMatches.md](DailyMatches.md) | A full day, per sport |
| [Workflows.md](Workflows.md) | Live board, one match, a table, search, odds, season stats |
| [Models/](Models/) | JSON objects (`Event`, `Team`, `Player`, incidents, statistics) and the [route catalog](Models/Routes.md) |
| [openapi/](openapi/) | OpenAPI 3.0 files for clients and API tools |
| [Examples/](Examples/) | Python and Node you can run |
| [Footapi/](Footapi/), [Basketapi/](Basketapi/), [Tennisapi/](Tennisapi/) | Shotmap, heatmap, and cup-tree drawings |

Import [openapi/allsports_simplified_openapi.yaml](openapi/allsports_simplified_openapi.yaml) when a tool struggles with the full file. It describes the same routes, with shared path segments collapsed. Per-sport files are the easiest way to read one sport.

## Habits that save quota

Cache categories, tournament lists, squads, and finished results. Poll a live list every 10–30 seconds, not faster. Resolve ids through search or the tree, then store them. A 204 is a normal empty result, so do not retry it as a failure.

## Support

Use the About tab of the API on RapidAPI, or the listing on [API.market](https://api.market/store/recodex/allsportsapi). Help while you are building is free.

If a fact you need is not in these routes, the [Allscores API](https://rapidapi.com/fluis.lacasse/api/allscores/) is a separate product with a different shape.
