# FAQ

Parameter names, required flags, and enums are in the [OpenAPI](../../openapi/skalpha_openapi.yaml). Sequences of calls are in [Workflows](workflows.md).

## Where do the parameters come from?

From the operation you are calling. Send only names that operation lists. Do not reuse another route's query.

## Are there POST routes?

No. Every route is `GET /api/skalpha/...`. A screener here is the filter metadata, the directory, and one definition by id.

## What does an empty 204 mean?

The route exists and there is no data for those parameters. Do not repeat the same request.

## The 400 does not name the bad field

A `400` with `title: Bad Request` and a `request_id` does not name the parameter. Check the name and the enum in the OpenAPI.

A `400` whose body is the string `invalid parameters` names `filter_since=0`, `filter_until=0`, or `page_number=0`. Omit those parameters instead of sending `0`. `filter_periods=0` is different: on rating periods, `0` is the current week.

## What are 502, 503, and 504?

The response could not be obtained. The body is `{"error":{"status","title","request_id"}}`.

## How big is a page?

`page_size` is 1 to 50. `page_number` starts at 1. Omit `page_number` for the first page.

`full-news/trending` uses 50. Analysis, filings, transcripts, and press releases for one symbol use 40. `per_page` exists only on `/tickers`, up to 100.

## How do I send a list?

One parameter, separated by commas: `filter_slugs=tgt,wmt`, `ticker_ids=62,1433`, `comment_ids=103368775,103339973`.

## Slug or numeric id?

The slug identifies `/symbols/{slug}` and the slug parameters (`slug`, `slugs`, `slugs_list`, `sa_slugs`). `tgt` and `TGT` are different path values. Pick one case and reuse it.

The numeric id identifies the quote (`sa_ids`), the options chain (`ticker_id`), the LUA chart (`ticker_id`), and estimates (`ticker_ids`). Read it from `/quotes/realtime?sa_slugs=tgt` or from the profile.

On `analysis`, `news`, `transcripts`, `press-releases`, and `related-analysis`, the query `id` is the slug, not a cursor. You can omit it. The route uses the path slug.

## Do I send both sa_ids and sa_slugs?

No. `/quotes/realtime` needs one of them.

## Which category goes on which list?

Article categories, including `stock-ideas` and `latest-articles`, go on `/articles` and `/articles/trending`. News categories, including `market-news::technology`, go on `/news`, `/news/trending`, and `/full-news/trending`. Symbol news uses `dividend_news`, `earnings_news`, `m_n_a_news`, and `news_card`.

`/equities` accepts all three lists. The tokens are in [Parameters](request-essentials.md#categories).

## Which period_type?

It depends on the route.

| Route | Values |
| --- | --- |
| `/symbols/{slug}/fundamentals_metrics` | `annual`, `quarterly`, `ttm`, `non_periodic` |
| `/symbol-data/estimates` | `annual`, `quarterly`, `non_periodic` |
| `/symbols/{slug}/fundamentals` | `annual`, `quarterly` |
| `/symbols/rating/periods` | `weeks` |

`/symbols/{slug}/fundamentals` is one field for a chart. It also requires `filter_field` and `filter_limit`. `/symbols/{slug}/fundamentals_metrics` is the statement and also requires `statement_type` and `target_currency`.

## What is sa_page_url?

When the operation lists it, send the `links.self` path from the list response, with no host. Examples: `/article/{id}-{slug}`, `/news/{id}-{slug}`, `/pr/{id}-{slug}`, `/filing/{id}`, `/author/{slug}`.

`sa_referrer` is the path of the previous page, with no host. `sa_query` is the query string. Omit `sa_query` when you have none. Omit all three when the operation does not list them. Lists, trending, and comments do not use them.

## How do comments work?

`comment-maps` returns the ids. The next call sends those ids in `comment_ids`, comma-separated, with `include=user` and `sort=-top_parent_id`. Replies to one comment are `/comments/{id}/sub-comments`.

## Why does the same field have two names?

`/metrics` uses `pe_nongaap`. `/symbol-data` uses `peRatioFwd`. Copy the name from the operation you are calling.

`/symbols/{slug}/sector_metrics` is the sector of that symbol. `/sector-metrics` takes `filter_sector_ids`.

## Should I send filter_with_rating=false?

Yes, on the earnings calendar, when you want that call. A bool you do not want is omitted. `false` is a real value when the operation lists it and you mean false.

## Should I send lang, isMounting, or undefined?

`lang` is `en`, or omit it. Do not send `undefined`. Do not send `isMounting`. Do not send a parameter the operation does not list.

## Can I call a route that is not in the OpenAPI?

No. Tooltips and campaigns are not in this API.

## Do I send an account cookie or token?

No.

## Should I repeat the same URL?

Read `Cache-Control` on the response before you repeat it. Fetch the list once and page through it.
