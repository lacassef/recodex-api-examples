# LivescoresAPI

How to call the `GET` routes under `/api/livescores`. Each route's parameters are in the [OpenAPI](openapi/livescoresapi_openapi.yaml).

Send `X-RapidAPI-Key` and `X-RapidAPI-Host`. The host is the one on the LivescoresAPI product page. Paths stay `/api/livescores/...`.

`204` means the route exists and there is no data for those parameters.

## Map

- [Parameters](guides/request-essentials.md) — value shape, ids, and the parameters that change by route.
- [Building a request](guides/building-requests.md) — what to put on the query.
- [Workflows](guides/workflows.md) — which call comes next, and which field of the response fills the next parameter.
- [FAQ](guides/faq.md) — status codes, ids, and the parameters that differ by route.
- [Examples](guides/examples.md) — curls.
- [Best practices](guides/best-practices.md) — what to send and what to omit.
- [Feeds and scoreboards](feeds/overview.md) — scoreboard, refresh, odds list, featured.
- [Feed names](feeds/feed-patterns.md) — the `feed` path on `/feed/{version}/{feed}`.
- [Navigation](navigation/overview.md) — navigation, categories, tournament lists.
- [Tournaments](tournaments/overview.md) — fixtures, results, tables, draw.
- [Matches](matches/overview.md) — one event.
- [Participants](participants/overview.md) — team and participant resources.
- [Players](players/overview.md) — profile and player tables.
- [Rankings](rankings/overview.md) — resolve a ranking, then the table.
- [News](news/overview.md) — list, article, entity news.
- [Search](search/overview.md) — search and suggestions.
- [Updates](updates/overview.md) — updates and status.
- [Persisted queries](graphql/overview.md) — `_hash` on `/graphql` and `/odds`.
- [Media](media/overview.md) — banners, stats, images.
- [Schemas](reference/schemas.md) — response objects.
- [Models](Models/README.md) — JSON objects and the route catalog.
- [Sport ids](reference/sport-ids.md) — `sportId` values.

## Smallest request

Call `https://{host}/api/livescores/sports/{sportId}/scoreboard`. `{host}` is the LivescoresAPI host from the product page. Take `sportId` from the [sport list](reference/sport-ids.md). Omit `dayOffset` for today. Send only parameters the operation lists. An invalid value returns `400`. A filled call is in [Examples](guides/examples.md).
