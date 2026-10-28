# Routes

Every published SKAlpha route, one row per path. A `*` after a query name means that parameter is required. Omit an optional one you are not using.

A `200` body is JSON. A `204` body is empty. `/charts/lua` is not a JSON:API document. `/filings/pdf/{id}` is the file, not JSON. The objects callers parse are in [README](README.md). Machine-readable parameters are in [openapi/](../openapi/).

## article-page-content-recommendations

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/article-page-content-recommendations` | article_id, variation | Article page content recommendations |

## articles

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/articles` | fields_article, filter_category, filter_since, filter_until, include, page_size, page_number | Articles list |
| `GET /api/skalpha/articles/trending` | fields_article, fields_author, filter_category, include, page_size, page_number | Trending articles |
| `GET /api/skalpha/articles/{id}` | include, lang, sa_page_url, sa_referrer, sa_query | Article by ID |
| `GET /api/skalpha/articles/{id}/author` | include | Article author |
| `GET /api/skalpha/articles/{id}/comment-maps` | include, sort | Article comment maps |
| `GET /api/skalpha/articles/{id}/comments` | comment_ids, include, sort, lang | Article comments |

## authors

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/authors/{slug}` | include, sa_page_url, sa_referrer, sa_query | Author by slug |
| `GET /api/skalpha/authors/{slug}/article/ticker-counts` |  | Author article ticker counts |
| `GET /api/skalpha/authors/{slug}/top-covered-symbols` |  | Author top covered symbols |

## breaking-news

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/breaking-news` | lang | Breaking news |

## charts

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/charts/lua` | period, from, to, ticker_id* | LUA charts |

## comments

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/comments/{id}/sub-comments` | include, sort, lang | Comment replies |

## day-watch

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/day-watch` | sort | Day watch |

## dividend-investing

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/dividend-investing` |  | Dividend investing |

## earnings-calendar

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/earnings-calendar/days` | filter_start_date, filter_end_date, filter_with_rating, filter_currency | Earnings calendar days |
| `GET /api/skalpha/earnings-calendar/tickers` | filter_selected_date*, filter_with_rating, filter_currency | Earnings calendar tickers |

## education-top-articles

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/education-top-articles` | filter_category, lang, page_size | Education top articles |

## equities

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/equities` | filter_category | Equities |

## etf-performance-categories

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/etf-performance-categories` |  | ETF performance categories |
| `GET /api/skalpha/etf-performance-categories/{category}` |  | ETF performance by category |

## feed

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/feed` | models_list*, all_list, any_tags_list, any_primary_list, include, page_size, page_number, filter_since, filter_until, custom_sort, without_list | Feed |

## filings

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/filings/pdf/{id}` |  | Filings PDF |
| `GET /api/skalpha/filings/{id}` | include, sa_page_url, sa_referrer, sa_query | Filings by ID |
| `GET /api/skalpha/filings/{id}/comment-maps` | include, sort | Filings comment maps |

## full-news

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/full-news/trending` | filter_category, fields_news, fields_tag, include, page_size, page_number | Full news trending |

## fundamental-metrics

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/fundamental-metrics` | fields_list, ticker_ids | Fundamental metrics |

## global-indices

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/global-indices` | include | Global indices |

## historical-prices

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/historical-prices` | slug*, slugs_list, from, to, sort, filter_show_by, filter_for_date, page_size, page_number | Historical prices |

## leading-news-stories

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/leading-news-stories` |  | Leading news stories |

## market-open

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/market-open` | lang | Market open |

## metrics

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/metrics` | filter_fields*, filter_slugs*, minified | Metrics |

## news

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/news` | fields_news, fields_tag, filter_category, filter_since, filter_until, include, filter_unread, lang, page_size, page_number | News list |
| `GET /api/skalpha/news/trending` | filter_category, include, page_size, page_number | Trending news |
| `GET /api/skalpha/news/{id}` | include, lang, sa_page_url, sa_referrer, sa_query | News by ID |
| `GET /api/skalpha/news/{id}/comment-maps` | include, sort, lang | News comment maps |
| `GET /api/skalpha/news/{id}/comments` | comment_ids, include, sort, lang | News comments |

## news-page-content-recommendations

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/news-page-content-recommendations` | market_current_id, variation | News page content recommendations |

## options

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/options/chain` | ticker_id*, expiration_date*, lang | Options chain |

## press-releases

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/press-releases/{id}` | include, sa_page_url, sa_referrer, sa_query | Press release by ID |
| `GET /api/skalpha/press-releases/{id}/comment-maps` | include, sort | Press release comment maps |

## quotes

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/quotes/realtime` | sa_ids, sa_slugs, lang | Real-time quotes |

## screener-filters

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/screener-filters` | type*, variation* | Screener filters |

## screeners

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/screeners` | type* | Screeners |
| `GET /api/skalpha/screeners/{id}` |  | Screener by ID |

## search

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/search` | term*, limit, symbols, indices, crypto, actively_traded, currency | Search autocomplete |

## searches

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/searches` | filter_query, filter_type, filter_list, filter_period, filter_tags, filter_defunct, page_size, page_number | Searches |
| `GET /api/skalpha/searches/{scope}` | filter_query, filter_list, filter_period, filter_tags, filter_defunct, page_size, page_number | Searches by scope |

## sector-metrics

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/sector-metrics` | filter_fields*, filter_sector_ids* | Sector metrics aggregate |

## sectors-hub

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/sectors-hub` | sector*, lang | Sectors hub |

## symbol-data

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/symbol-data` | fields_list, slugs* | Symbol data |
| `GET /api/skalpha/symbol-data/charting` | start, end, metrics, metrics_list, slugs_list | Symbol data charting |
| `GET /api/skalpha/symbol-data/estimated-earning-announces` | slug* | Symbol data estimated earning announces |
| `GET /api/skalpha/symbol-data/estimates` | estimates_data_items, revisions_data_items, period_type, relative_periods, group_by_month, return_window, ticker_ids | Symbol data estimates |
| `GET /api/skalpha/symbol-data/profile` | slugs* | Symbol data profile |
| `GET /api/skalpha/symbol-data/widgets` | date, slug* | Symbol data widgets |

## symbols

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/symbols/rating/periods` | slugs_list*, period_type*, filter_periods | Rating periods batch |
| `GET /api/skalpha/symbols/{slug}` | lang | Symbol |
| `GET /api/skalpha/symbols/{slug}/analysis` | filter_related, filter_since, filter_until, id, include, page_size, page_number | Symbol analysis |
| `GET /api/skalpha/symbols/{slug}/author_ratings` | include, filter_type, page_size, page_number | Author ratings |
| `GET /api/skalpha/symbols/{slug}/discussions` | include, page_size | Discussions |
| `GET /api/skalpha/symbols/{slug}/dividends` | years, group_by, sort | Symbol dividends |
| `GET /api/skalpha/symbols/{slug}/earning_summaries` | referral_type, referral_date | Earning summaries |
| `GET /api/skalpha/symbols/{slug}/etf_category_metrics` | filter_fields, filter_fund_type | ETF category metrics |
| `GET /api/skalpha/symbols/{slug}/faq` |  | FAQ |
| `GET /api/skalpha/symbols/{slug}/fundamentals` | period_type*, filter_field*, filter_limit*, lang | Fundamentals series |
| `GET /api/skalpha/symbols/{slug}/fundamentals_metrics` | period_type*, statement_type*, target_currency* | Fundamentals metrics |
| `GET /api/skalpha/symbols/{slug}/insiders_sell_buy` |  | Insider sell and buy |
| `GET /api/skalpha/symbols/{slug}/invested_etfs` |  | Invested ETFs |
| `GET /api/skalpha/symbols/{slug}/news` | filter_category, filter_since, filter_until, id, include, page_size, page_number | Symbol news |
| `GET /api/skalpha/symbols/{slug}/option-expirations` |  | Option expirations for symbol |
| `GET /api/skalpha/symbols/{slug}/payout_ratios` |  | Payout ratios |
| `GET /api/skalpha/symbols/{slug}/peers/etfs/exposure` |  | Symbol peers (ETFs exposure) |
| `GET /api/skalpha/symbols/{slug}/peers/stocks/most_mentioned` |  | Symbol peers (stocks most mentioned) |
| `GET /api/skalpha/symbols/{slug}/peers/stocks/people_follow` |  | Symbol peers (stocks people follow) |
| `GET /api/skalpha/symbols/{slug}/people_also_follow` | include | People also follow |
| `GET /api/skalpha/symbols/{slug}/press-releases` | filter_until, id, include, page_size, page_number | Symbol press releases |
| `GET /api/skalpha/symbols/{slug}/random` |  | Random symbol |
| `GET /api/skalpha/symbols/{slug}/rating/histories` | filter_from, page_size, page_number | Rating histories |
| `GET /api/skalpha/symbols/{slug}/rating/periods` | filter_periods | Rating periods |
| `GET /api/skalpha/symbols/{slug}/related-analysis` | filter_since, filter_until, id, include, page_size, page_number | Related analysis |
| `GET /api/skalpha/symbols/{slug}/sec-filings` | filter_filing_category, include, page_size, page_number | Symbol SEC filings |
| `GET /api/skalpha/symbols/{slug}/sector_metrics` | filter_fields | Sector metrics |
| `GET /api/skalpha/symbols/{slug}/shares` |  | Shares |
| `GET /api/skalpha/symbols/{slug}/splits` |  | Symbol splits |
| `GET /api/skalpha/symbols/{slug}/suggested` | source_type, variation | Suggested symbols |
| `GET /api/skalpha/symbols/{slug}/top_discussions` | include, page_size, page_number | Top discussions |
| `GET /api/skalpha/symbols/{slug}/transcripts` | filter_only, filter_until, id, include, page_size, page_number | Symbol transcripts |

## ticker-metric-grades

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/ticker-metric-grades` | filter_fields*, filter_slugs*, filter_algos, minified | Ticker metric grades |

## tickers

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/skalpha/tickers` | filter_slugs*, include_gics, per_page, include | Tickers |
