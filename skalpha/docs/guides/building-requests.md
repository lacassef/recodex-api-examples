# Building a request

Every route is `GET /api/skalpha/...`. There is no body. The screener in this API is the definition: filters, the list, and an id. There is no POST execution.

Filled calls are in [Examples](examples.md). The order of calls is in [Workflows](workflows.md).

## Steps

1. Open the operation in the [OpenAPI](../../openapi/skalpha_openapi.yaml) or in the [map](../../README.md).
2. Copy that operation's parameter names. Do not invent a name and do not reuse another route's query.
3. Fill in the required ones. An optional parameter goes in only when you want that filter.
4. A list goes in one parameter, separated by commas.
5. Take the enum from that operation's list. The same values are repeated in [Parameters](request-essentials.md#values-by-parameter).
6. Send `lang=en` or omit it.

## Choosing the value

A price range uses `from` and `to`. Individual dates use `filter_for_date`, one date or several in the same parameter. Dates are `YYYY-MM-DD`.

Several ticker ids go in one `ticker_ids` value. Set `period_type` from the enum of the operation you are calling. `group_by_month` is `true` or `false` when that operation lists it.

`/metrics` and `/symbols/{slug}/sector_metrics` both take a field list in `filter_fields`. They are different routes. Copy the field names from the route you are calling. `/metrics` also takes the slugs in `filter_slugs` and `minified` when you want that flag.

On symbol news, analysis, transcripts, press releases, and related analysis, `id` is the slug, not a cursor. Omit it. The route uses the path slug.

Do not send `filter_since=0`. With no lower bound, omit the parameter. The same rule applies to `filter_until` and `page_number`.

## From slug to numeric id

Autocomplete returns the slug. The profile and the quote return the numeric id. Options, the chart, and estimates take that id, not the slug. How each response feeds the next call is in [Workflows](workflows.md). Status codes and the parameters that change by route are in the [FAQ](faq.md).

## Comments

`comment-maps` returns the ids. The next request puts those ids in `comment_ids`. Replies to one comment are `/comments/{id}/sub-comments`, with that comment's id in the path. Articles, news, press releases, and filings use `include=user` and `sort=-top_parent_id` when the operation lists them.

## Page

`page_number` starts at 1. `page_size` goes up to 50. Analysis, filings, transcripts, and press releases for one symbol use 40. `full-news/trending` uses 50.

On a detail call, if the operation lists `sa_page_url`, send the `links.self` path. See [Detail](request-essentials.md#article-news-press-release-filing-and-author-detail).
