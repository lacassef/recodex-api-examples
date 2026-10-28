# Symbol page

How to assemble the calls for one symbol. The order is not required. Call the block the screen is showing. Do not fire every route up front.

You need the slug and, for the quote, the chart, options, and estimates, the numeric id. How to get each one from the previous response is in [Workflows](../guides/workflows.md#quote-a-ticker). Filled calls are in [Examples](../guides/examples.md). Parameter names are in the [OpenAPI](../../openapi/skalpha_openapi.yaml).

`tgt` and `TGT` are different path values. Pick one case and reuse it. `btc-usd` is the slug on the tabs. `BTC-USD` is the slug on the profile and on random. Do not mix them on the same resource.

## Find the slug and the id

1. Call `/search`. Put the text in `term`. Set `symbols`, `indices`, `crypto`, and `actively_traded` for the kinds of result you want. Read the slug.
2. Call `/symbols/{slug}` for the profile. Read the numeric id.
3. Call `/quotes/realtime` with `sa_slugs` or `sa_ids`, not both.
4. Call `/tickers` with the neighboring slugs in `filter_slugs`. Set `include_gics` when you want the classification.
5. Call `/symbols/{slug}/random` when you want another symbol from the same batch. It returns a new slug. Start again from the profile if you follow it.

## Price and chart

1. Call `/historical-prices`. Put the symbol in `slug` and every series, including a benchmark, in `slugs_list`. Use `from` and `to` for a range, or `filter_for_date` for one or more dates.
2. Call `/charts/lua` with the numeric id in `ticker_id` and the window in `period`.
3. Call `/symbol-data/estimated-earning-announces` with the slug when you want the next earnings date.

## Valuation metrics

Call `/metrics` once per field group. Put that group's fields in `filter_fields` and the slug in `filter_slugs`. Set `minified` to `true` or `false` for that group. Repeat for the next group.

Call `/ticker-metric-grades` with the grade fields and the algorithms in `filter_algos`.

Call `/symbols/{slug}/sector_metrics` for the sector of this symbol. Put the fields in `filter_fields`. This is not `/sector-metrics`.

Estimates go to `/symbol-data/estimates`. Put the numeric id in `ticker_ids`, one `period_type` per call, and the items in `estimates_data_items`. Send actuals and the projection as separate calls by changing `relative_periods`. Put revisions in `revisions_data_items`.

A balance-sheet series goes to `/symbol-data/charting`. Put the slug in `slugs_list`, the series in `metrics` or `metrics_list`, and the range in `start` and `end`.

A statement goes to `/symbols/{slug}/fundamentals_metrics`. Set `period_type`, `statement_type`, and `target_currency`. Request each statement you need.

One field for a short chart goes to `/symbols/{slug}/fundamentals`. Set `period_type`, `filter_field`, and `filter_limit`. This is not the statement route.

## Dividends, shares, peers

These take the slug in the path and no extra parameter, except where noted:

- `/dividends` takes `years`, `group_by`, and `sort`.
- `/splits`, `/payout_ratios`, `/shares`, and `/insiders_sell_buy` take the slug only.
- `/invested_etfs` lists ETFs that hold the symbol.
- `/peers/stocks/most_mentioned`, `/peers/stocks/people_follow`, and `/peers/etfs/exposure` take the slug only.

For an ETF dividend block, call `/symbols/{slug}/etf_category_metrics`. Set `filter_fund_type` and put the fields in `filter_fields`.

## Content tabs

Put the slug in the path. On analysis, news, transcripts, press releases, and related analysis, omit the query `id`. It is the slug, and the route uses the path.

- News: set `filter_category` only for one symbol-news category. Use `news_card` for the summary. Omit it for every category. Set `include` for the objects you will render.
- Analysis and related analysis: set `include`. Set `filter_related` only when you want that filter.
- Transcripts: set `filter_only` to transcripts or to slides.
- Press releases: set `include`.
- Filings: set `filter_filing_category` to the tab, and `include` when you want the form type.

Do not send `filter_until=0` or `isMounting`. With no time bound, omit the filter. Page with `page_size` and `page_number` when the operation lists them.

## Ratings and discussion

- `/rating/periods` on one symbol takes week offsets in `filter_periods`. `0` is the current week.
- `/rating/histories` takes `page_number` and, when you want a start, `filter_from`.
- `/author_ratings` takes `include`, and `filter_type` when you want one rating bucket.
- `/top_discussions` takes `include` for the subject, the author, and the comments you will render.
- `/faq` takes the slug, and `lang` when you want it.

The batch route `/symbols/rating/periods` has no slug in the path. Put the slugs in `slugs_list` and set `period_type` to `weeks`.

## Who else, and the earnings card

`/people_also_follow` takes `include` for the sector fields you will show.

`/suggested` takes `source_type`. Use `similarities` for the card and `peers_similarities` for the peers list. Set `variation` from that operation's enum.

`/earning_summaries` points at the document you already opened. Put that kind in `referral_type` and that document's time in `referral_date`.

## Options

Call `/symbols/{slug}/option-expirations` first and read the dates. Then call `/options/chain` with the numeric id in `ticker_id` and one of those dates in `expiration_date`.

## Not in this API

Tooltips and campaigns are not in this API. Use the routes above.
