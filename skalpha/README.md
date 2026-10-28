# SKAlpha

How to call the `GET` routes under `/api/skalpha`. Each route's parameters are in the [OpenAPI](openapi/skalpha_openapi.yaml). That file is a copy of `docs/oai/skalpha_openapi.yaml`, the output of `go run ./cmd/openapi-gen`. Do not edit it by hand. When the routes change, run the generator and copy it again.

`204` means the route exists and there is no data for those parameters.

## Map

- [Parameters](docs/guides/request-essentials.md) — value shape, enums, and categories.
- [Building a request](docs/guides/building-requests.md) — what to put on the query.
- [Workflows](docs/guides/workflows.md) — which call comes next, and which field of the response fills the next parameter.
- [FAQ](docs/guides/faq.md) — status codes, ids, categories, and the parameters that differ by route.
- [Examples](docs/guides/examples.md) — curls.
- [Best practices](docs/guides/best-practices.md) — what to send and what to omit.
- [Models](Models/README.md) — JSON objects and the route catalog.
- [Symbol page](docs/articles/symbol-page.md) — which call each block of a symbol screen makes, and which parameter it sets.
- [News and articles](docs/articles/news-and-articles.md) — list, then the item, then comments.
- [Content](docs/content/overview.md) — news, articles, filings, authors, feed.
- [Market](docs/market-data/overview.md) — prices, quotes, options, charts, ETFs, aggregates.
- [Symbols](docs/symbols/overview.md) — sub-resources of `/symbols/{slug}`.
- [Reference](docs/reference/overview.md) — metrics, calendar, screener, search.

## Smallest request

Call `/news`. Set `filter_category` to one news category and `page_size` to the size you want. `{api-host}` is this gateway's host. Send only parameters the operation lists. An invalid value returns `400`. A filled call is in [Examples](docs/guides/examples.md).
