# Workflows

A workflow is the order of calls and what you carry from one response into the next request. Each call is `GET /api/skalpha/...`. Take the parameter names and enums from that operation in the [OpenAPI](../../openapi/skalpha_openapi.yaml). Value shape is in [Parameters](request-essentials.md). Filled requests are in [Examples](examples.md).

Send only the parameters that step needs. Omit a filter you are not using. Do not send `0` for `filter_since`, `filter_until`, or `page_number`.

## Quote a ticker

Start with the text the user typed.

1. Call `/search`. Put the text in `term`. Turn on the kinds of result you want with `symbols`, `indices`, `crypto`, and `actively_traded`. Read the slug from the result.
2. Call `/symbols/{slug}` with that slug in the path. Read the numeric id from the profile.
3. Call `/quotes/realtime`. Put the slug in `sa_slugs`, or the numeric id in `sa_ids`. Send one of the two.
4. To load neighbors, call `/tickers` with those slugs in `filter_slugs`. Set `include_gics` when you want the classification.

Keep the slug and the numeric id. Later steps use one or the other, not interchangeably.

## Price and chart

You already have the slug and the numeric id.

1. Call `/historical-prices`. Put the main ticker in `slug`. Put every series you want, including a benchmark, in `slugs_list`. Put the range in `from` and `to`.
2. For individual dates instead of a range, put them in `filter_for_date`. Use one form of date filter, not both, unless you mean both.
3. Call `/charts/lua` with the numeric id in `ticker_id` and the window in `period`. This route does not take the slug.

`from`, `to`, and `filter_for_date` are `YYYY-MM-DD`. The chart body is not JSON:API.

## Options

You already have the slug and the numeric id.

1. Call `/symbols/{slug}/option-expirations`. Read the expiration dates from the response.
2. Call `/options/chain`. Put the numeric id in `ticker_id` and one date from step 1 in `expiration_date`. The chain does not take the slug.

## Symbol research

You already have the slug. Put it in the path of `/symbols/{slug}/...`. The route list is in [Symbols](../symbols/overview.md). A full page of calls is in [Symbol page](../articles/symbol-page.md).

Pick the tab you are rendering. Do not call every sub-resource up front.

1. News: `/symbols/{slug}/news`. Set `filter_category` only when you want one symbol-news category. Omit it to get all of them. Use `news_card` for the summary list.
2. Filings: `/symbols/{slug}/sec-filings`. Set `filter_filing_category` to the tab you are showing.
3. Transcripts or slides: `/symbols/{slug}/transcripts`. Set `filter_only` to which of the two you want.
4. A statement: `/symbols/{slug}/fundamentals_metrics`. Set `period_type`, `statement_type`, and `target_currency`.
5. One field for a chart: `/symbols/{slug}/fundamentals`. Set `period_type`, `filter_field`, and `filter_limit`. This is not the statement route.
6. Dividends: `/symbols/{slug}/dividends`. Set `years`, `group_by`, and `sort`.

On `analysis`, `news`, `transcripts`, `press-releases`, and `related-analysis`, the query `id` is the slug. Omit it. The route uses the path slug.

Page with `page_size` and `page_number` only when the operation lists them. Ask for the next page when the user asks for it.

## Article or news, then comments

Start from the section the user opened. Article categories go on `/articles`. News categories go on `/news`. Do not swap them. The tokens are in [Parameters](request-essentials.md#categories).

1. Call the list with `filter_category` and the `include` for that resource. Read each item's id and `links.self`.
2. Call `/articles/{id}` or `/news/{id}` with that id in the path. When the operation lists `sa_page_url`, put the `links.self` path there, with no host. Put the previous page path in `sa_referrer`, also with no host. Put a query string in `sa_query` only when you have one.
3. Call `comment-maps` on that same item. Read the comment ids from the response.
4. Call `comments` on that same item. Put the ids from step 3 in `comment_ids`.
5. For replies to one comment, call `/comments/{id}/sub-comments` with that comment's id in the path.

Use `include=user` and `sort=-top_parent_id` on the comment calls when the operation lists them. Press releases and filings follow the same two steps, on their own `comment-maps` and detail routes. Lists, trending, and comments do not take `sa_page_url`.

A sidebar recommendation is a separate call after the detail. News uses `/news-page-content-recommendations` with the news id in `market_current_id`. Articles use `/article-page-content-recommendations` with the article id in `article_id`. Set `variation` from that operation's enum.

## Search, then open the item

1. Call `/searches` for the combined result. Put the text in `filter_query`. Put the result types you want in `filter_type`.
2. For one tab, call `/searches/{scope}` with that tab in the path and the same text in `filter_query`. Set `filter_period` for that tab. On people, set `filter_defunct` only when inactive records should be included. Otherwise omit it.
3. When the result is an article or a news item, continue at [Article or news, then comments](#article-or-news-then-comments). Put the returned id in the path. Put `links.self` in `sa_page_url`.

A symbol result continues at [Quote a ticker](#quote-a-ticker) from the slug. An author result continues at `/authors/{slug}`.

## Earnings calendar

1. Call `/earnings-calendar/days` with the range in `filter_start_date` and `filter_end_date`. Set `filter_with_rating` and `filter_currency` when you want those filters. `false` is a valid value for `filter_with_rating`.
2. Call `/earnings-calendar/tickers` with one day from that range in `filter_selected_date`. Carry the same rating and currency settings forward when the day call should match the range call.

Dates are `YYYY-MM-DD`.

## Screener definition

There is no execution call.

1. Call `/screener-filters` with `type` and `variation` to read the filter metadata for that screener kind.
2. Call `/screeners` with the same `type` to read the directory.
3. Call `/screeners/{id}` with an id from that directory to read one definition.

## Metrics and estimates

You already have the slug and, for estimates, the numeric id.

1. Call `/metrics` with the slugs in `filter_slugs` and the fields for one group in `filter_fields`. Repeat the call for the next group. Do not pack every group into one request.
2. Call `/ticker-metric-grades` with the slugs, the grade fields, and the algorithms in `filter_algos`.
3. For the sector of one symbol, call `/symbols/{slug}/sector_metrics` and put the fields in `filter_fields`.
4. For several sectors by numeric sector id, call `/sector-metrics` with those ids in `filter_sector_ids`. This is not step 3.
5. Call `/symbol-data/estimates` with the numeric ids in `ticker_ids`. Set `period_type` from that operation's enum. Put actuals and the projection in separate calls by changing `relative_periods`. Put revisions in `revisions_data_items` when you want revisions rather than the estimate items.

`period_type` is not the same list on every route. Estimates, the statement, the one-field chart, and rating periods each have their own enum. Use the one on the operation you are calling.
