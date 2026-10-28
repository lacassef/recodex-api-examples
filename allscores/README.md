# AllScores API

How to call the `GET` routes under `/api/allscores`. Each route's parameters are in the [OpenAPI](openapi/allscores_openapi.yaml).

Subscribe on [RapidAPI](https://rapidapi.com/fluis.lacasse/api/allscores). Send `X-RapidAPI-Key` and `X-RapidAPI-Host: allscores.p.rapidapi.com`. The base URL is `https://allscores.p.rapidapi.com`. Copy the host from the Endpoints tab if that listing prints a different one.

The spec lists `204` when the route exists and there is no data for those parameters. Some routes still return `200` with an empty object or an empty list. Those cases are on the area pages.

## Map

- [Parameters](guides/request-essentials.md) — value shape, ids, and the parameter name that changes by route.
- [Building a request](guides/building-requests.md) — what to put on the query.
- [Workflows](guides/workflows.md) — which call comes next, and which field of the response fills the next parameter.
- [FAQ](guides/faq.md) — status codes, ids, and the parameters that differ by route.
- [Examples](guides/examples.md) — curls.
- [Best practices](guides/best-practices.md) — what to send and what to omit.
- [Scores](scores/overview.md) — countries, sports, and score lists.
- [Games](games/overview.md) — one game, stats, lineups, commentary.
- [Competitions](competitions/overview.md) — competition, table, fixtures, results.
- [Competitors](competitors/overview.md) — team, squad, form, transfers.
- [Athletes](athletes/overview.md) — profile, career, games.
- [Bets](bets/overview.md) — lines, trends, outrights.
- [News](news/overview.md) — news cards.
- [Search](search/overview.md) — competitions, competitors, and athletes.
- [Images](images/overview.md) — photos, logos, flags, trophies.
- [Schemas](reference/schemas.md) — response fields named by the routes.
- [Models](Models/README.md) — JSON objects and the route catalog.
- [Sport ids](reference/sport-ids.md) — `sport`, `sportId`, and `sportType`.
- [Languages and enums](reference/enums.md) — `langId`, status, and odds.

## Smallest request

Call `https://allscores.p.rapidapi.com/api/allscores/sports`. Omit `langId` for the default language. Send only parameters the operation lists. An invalid value returns `400`. A filled call is in [Examples](guides/examples.md).
