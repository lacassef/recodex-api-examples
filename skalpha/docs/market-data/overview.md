# Market

Quotes, history, options, status, charts, ETFs, and symbol aggregates. Values and dates are in [Parameters](../guides/request-essentials.md). The TGT page is in [Symbol page](../articles/symbol-page.md).

## Prices

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/historical-prices` | Daily history. | `slug` | `slugs_list`, `from`, `to`, `sort`, `filter_show_by`, `filter_for_date`, `page_size`, `page_number` | `slug` is the ticker, for example `tgt`. Several symbols go in `slugs_list`. `from` and `to` are `YYYY-MM-DD`. Sort example: `as_of_date`. `filter_show_by`: `month` or `week`. Several dates in `filter_for_date`, separated by commas. |

## Intraday and derivatives

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/quotes/realtime` | Quote. | one of `sa_ids`, `sa_slugs` | `lang` | Commas in the same parameter: `sa_ids=62` or `sa_slugs=tgt,wmt`. |
| `/api/skalpha/options/chain` | Chain. | `ticker_id`, `expiration_date` | `lang` | Date `YYYY-MM-DD`. The numeric id comes from the quote or the profile. The dates come from `/symbols/{slug}/option-expirations`. |

## Market view

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/market-open` | US session. | — | `lang` | `marketOpen` and the next open/close. |
| `/api/skalpha/day-watch` | Day's movers. | — | `sort` | `percent_change` or `ext_percent_change`. |
| `/api/skalpha/global-indices` | Indices. | — | `include` | Example: `include=tickers`. |
| `/api/skalpha/sectors-hub` | One sector page. | `sector` | `lang` | Examples: `information-technology`, `consumer-discretionary`. |
| `/api/skalpha/sector-metrics` | Revisions by sector id. | `filter_fields`, `filter_sector_ids` | — | Commas in both: `filter_fields=analysts_up_percent,analysts_down_percent` and `filter_sector_ids=25,45`. This is not `/symbols/{slug}/sector_metrics`. |
| `/api/skalpha/equities` | Stock list with a category. | — | `filter_category` | Accepts an article category, a news category, or a symbol-news category. |
| `/api/skalpha/dividend-investing` | Dividend view. | — | — | No query. |

## Charts

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/charts/lua` | Chart series. | `ticker_id` | `period`, `from`, `to` | `period`: `1D`, `5D`, `1M`, `6M`, `1Y`, `3Y`, `5Y`, `10Y`, `YTD`, `MAX`. The body is not JSON:API. |

## ETFs

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/etf-performance-categories` | Group slugs. | — | — | Discover the slug here. |
| `/api/skalpha/etf-performance-categories/{category}` | One group. | `category` | — | Examples: `key_markets`, `bonds`, `commodities`, `countries`, `currencies`, `strategies`, `cryptocurrency`. |

## Aggregates

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbol-data` | Fields by slug. | `slugs` | `fields_list` | `slugs=TGT` or `slugs=tgt,sp500`. Fields in `fields_list`, for example `peRatioFwd,lastClosePriceEarningsRatio`. |
| `/api/skalpha/symbol-data/charting` | Metric series. | — | `start`, `end`, `metrics`, `metrics_list`, `slugs_list` | Send `metrics` or `metrics_list`, comma-separated. Dates `YYYY-MM-DD`. |
| `/api/skalpha/symbol-data/estimates` | Estimates and revisions. | — | `estimates_data_items`, `revisions_data_items`, `period_type`, `relative_periods`, `group_by_month`, `return_window`, `ticker_ids` | `ticker_ids=62` or `ticker_ids=1309,1517`. `period_type`: `annual`, `quarterly`, `non_periodic`. `relative_periods` from -23 to 23. |
| `/api/skalpha/symbol-data/estimated-earning-announces` | Estimated earnings date. | `slug` | — | `tgt` and `TGT` are both valid. Pick one case and reuse it. |
| `/api/skalpha/symbol-data/profile` | Company profile. | `slugs` | — | `slugs=tgt` or `slugs=tgt,wmt`. |
| `/api/skalpha/symbol-data/widgets` | Page widget. | `slug` | `date` | `date` is unix seconds. |
