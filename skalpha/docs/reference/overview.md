# Reference

Metrics, the calendar, screener definitions, and search. A screener here is read-only: filters, the list, and one definition by id. There is no POST.

## Metrics and grades

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/metrics` | Metrics by slug. | `filter_fields`, `filter_slugs` | `minified` | `filter_fields=marketcap,tev` and `filter_slugs=tgt`. `minified` is `true` or `false`. The page makes one request per field group. |
| `/api/skalpha/ticker-metric-grades` | Grades by algorithm. | `filter_fields`, `filter_slugs` | `filter_algos`, `minified` | `filter_algos`: `main_quant`, `dividends`, `etf`, `reit`, `reit_dividend`, comma-separated. Example: `main_quant,dividends` and `minified=false`. |
| `/api/skalpha/fundamental-metrics` | Metrics by numeric id. | — | `ticker_ids`, `fields_list` | `ticker_ids=62` and `fields_list=total_revenue_growth,total_revenue_3y_cagr`. Estimates use `/symbol-data/estimates`. |

## Earnings calendar

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/earnings-calendar/days` | A range of days. | — | `filter_start_date`, `filter_end_date`, `filter_with_rating`, `filter_currency` | Example: `filter_start_date=2026-08-30`, `filter_end_date=2026-10-04`, `filter_with_rating=false`, `filter_currency=USD`. |
| `/api/skalpha/earnings-calendar/tickers` | One day. | `filter_selected_date` | `filter_with_rating`, `filter_currency` | Same toggles. Date `YYYY-MM-DD`. |

## Screeners

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/screener-filters` | Filter metadata. | `type`, `variation` | `lang` | `type`: `analysis`, `etf`, `stock`. Page `variation`: `show`. |
| `/api/skalpha/screeners` | Directory. | `type` | `lang` | `type` is `stock` or `etf`. |
| `/api/skalpha/screeners/{id}` | One definition. | `id` | `lang` | `id` is a short hex string, for example `922b797269`. |

## Search

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/search` | Autocomplete. | `term` | `limit`, `symbols`, `indices`, `crypto`, `actively_traded`, `currency` | Flags are `0` or `1`. Example: `1` on all four, `limit=20`, `currency=USD`. |
| `/api/skalpha/searches` | Global search. | — | `filter_query`, `filter_type`, `filter_list`, `filter_period`, `filter_tags`, `filter_defunct`, `page_size`, `page_number` | `filter_type` is one value: `people,symbols,pages,shortcuts`. `filter_list`: `all`, `stocks`, `etfs`, `mutual_funds`, `cryptos`. `filter_period`: `all`, `day`, `week`, `month`, `quarter`. |
| `/api/skalpha/searches/{scope}` | One tab. | `scope` | `filter_query`, `filter_list`, `filter_period`, `filter_tags`, `filter_defunct`, `page_size`, `page_number` | `scope`: `all`, `articles`, `headlines`, `news`, `pages`, `people`, `symbols`. For people, `filter_defunct=true` includes inactive records. Headlines example: `filter_tags=transcripts,evergreen-seo`. |

Ready-made examples are in [Examples](../guides/examples.md).
