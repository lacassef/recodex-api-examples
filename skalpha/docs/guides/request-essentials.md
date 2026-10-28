# Parameters

Each parameter name is the one in the [OpenAPI](../../openapi/skalpha_openapi.yaml). Send only the ones the operation lists. Required, type, and enum are in the spec.

## Value shape

A list fits in one parameter, separated by commas: `filter_slugs=tgt,wmt`, `ticker_ids=62,1433`, `comment_ids=103368775,103339973`, `filter_periods=0,3,6`.

`page_size` is 1 to 50. `per_page` on `/tickers` is 1 to 100. `page_number` starts at 1. Omit the page when you want the first one.

Dates use `YYYY-MM-DD`. `referral_date` accepts ISO-8601, for example `2026-09-29T06:01:00.000-04:00`. `filter_since` and `filter_until` are unix seconds. Do not send `0`: omit the parameter.

Currency is three uppercase letters, such as `USD`.

A bool is `true` or `false`. If the filter is not part of the call, omit the parameter. On the earnings calendar, `filter_with_rating=false` is a valid value.

A slug uses letters, digits, and `: . _ -`. `tgt` and `TGT` are different path values. Pick one case and reuse it.

`lang` is `en`, or omit it. Do not send `undefined`.

`relative_periods` are integers from -23 to 23, in the same comma list: `0,1` or `-3,-2,-1,0,1`.

## Values by parameter

`period_type` on statements and estimates: `annual`, `quarterly`, `ttm`, `non_periodic`. On `/symbols/{slug}/fundamentals` only `annual` and `quarterly`. On `/symbols/rating/periods` the value is `weeks`. Estimates in the spec: `annual`, `quarterly`, `non_periodic`.

`statement_type`: `income-statement`, `balance-sheet`, `cash-flow-statement`.

`group_by` on dividends: `year`, `fiscal_year`, `month`. Also send `sort=-date`.

`filter_show_by` on historical prices: `month` or `week`.

`filter_only` on transcripts: `transcripts` or `earnings-slides`.

`filter_filing_category`: `all`, `financials`, `news`, `proxies`, `tenders`, `ownership`, `other`.

`filter_algos`: `main_quant`, `dividends`, `etf`, `reit`, `reit_dividend`.

`period` on `/charts/lua`: `1D`, `5D`, `1M`, `6M`, `1Y`, `3Y`, `5Y`, `10Y`, `YTD`, `MAX`.

`filter_field` on `/symbols/{slug}/fundamentals`: `ffo_per_share_diluted`, `reported_diluted_eps_excl_extra_items`, `total_revenue`. `filter_limit` is required on that route. EPS and FFO use 7. Revenue uses 5.

`source_type` on suggested: `similarities` or `peers_similarities`. `variation` on that route: `ds_v2`.

`referral_type`: `filings`, `presentation`, `press_release`, `transcript`.

`scope` on `/searches/{scope}`: `all`, `articles`, `headlines`, `news`, `pages`, `people`, `symbols`.

`filter_type` on search: `people`, `symbols`, `pages`, `shortcuts`, together in one value: `people,symbols,pages,shortcuts`.

`filter_type` on author ratings: `very_bullish`, `bullish`, `neutral`, `bearish`, `very_bearish`.

`filter_list`: `all`, `stocks`, `etfs`, `mutual_funds`, `cryptos`.

`filter_period` on search: `all`, `day`, `week`, `month`, `quarter`.

Screener: `type` is `analysis`, `etf`, or `stock`. On `/screener-filters`, `type` and `variation` are required. `variation` is `show`. On `/screeners`, only `type`.

`models_list` on the feed: `Article`, `MarketCurrent`, `Research`. Example: `Article,MarketCurrent`.

Autocomplete: `symbols`, `indices`, `crypto`, and `actively_traded` are `0` or `1`. Example: `1` on all four, `limit=20`, `currency=USD`.

`sort` on day watch: `percent_change` or `ext_percent_change`. On comments: `-top_parent_id`. On prices: `as_of_date`.

`include` depends on the route. The values the pages use are in the notes column of each overview.

## Categories

`filter_category` takes one of these tokens.

### Articles

`dividends`, `dividends::dividend-ideas`, `dividends::dividend-quick-picks`, `dividends::dividend-strategy`, `dividends::reits`, `editors-picks`, `education::401k`, `education::cryptocurrency`, `education::dividends`, `education::etf`, `education::investing`, `education::ira`, `education::mutual-funds`, `education::portfolio-management`, `education::quant-ratings`, `etfs-and-funds`, `etfs-and-funds::closed-end-funds`, `etfs-and-funds::etf-analysis`, `etfs-and-funds::mutual-funds`, `investing-strategy`, `investing-strategy::fixed-income`, `investing-strategy::portfolio-strategy`, `investing-strategy::retirement`, `latest-articles`, `podcast`, `market-outlook`, `market-outlook::commodities`, `market-outlook::cryptocurrency`, `market-outlook::economy`, `market-outlook::forex`, `market-outlook::gold-and-precious-metals`, `market-outlook::todays-market`, `sectors::communication-services`, `sectors::consumer-staples`, `sectors::energy`, `sectors::real-estate`, `stock-ideas`, `stock-ideas::ai-tech-stocks`, `stock-ideas::basic-materials`, `stock-ideas::consumer-goods`, `stock-ideas::financial`, `stock-ideas::healthcare`, `stock-ideas::industrial-goods`, `stock-ideas::ipos`, `stock-ideas::long-ideas`, `stock-ideas::quick-picks`, `stock-ideas::technology`, `stock-ideas::utilities`.

Article trending uses `latest-articles`. Top education uses the `education::` branch.

### News

`earnings::earnings-news`, `market-news::all`, `market-news::buybacks`, `market-news::commodities`, `market-news::consumer`, `market-news::crypto`, `market-news::dividend-funds`, `market-news::dividend-stocks`, `market-news::earnings`, `market-news::energy`, `market-news::financials`, `market-news::global`, `market-news::guidance`, `market-news::healthcare`, `market-news::ipos`, `market-news::issuance`, `market-news::m-a`, `market-news::market-pulse`, `market-news::mlps`, `market-news::notable-calls`, `market-news::notable-calls-insights`, `market-news::on-the-move`, `market-news::politics`, `market-news::reits`, `market-news::spacs`, `market-news::technology`, `market-news::trending`, `market-news::top-news`, `market-news::us-economy`.

News trending uses `market-news::all` or `market-news::trending`.

### Symbol news

`dividend_news`, `earnings_news`, `m_n_a_news`, `news_card`. Use `news_card` for the summary list. With no `filter_category`, the route returns all of them.

`/equities` accepts all three lists.

## Article, news, press release, filing, and author detail

When the operation lists `sa_page_url`, send the `links.self` path, with no host. Examples: `/article/4938289-target-corporation-tgt-q2-2026-earnings-call-transcript`, `/news/4635195-target-projects-around-5-percent-fy2026-net-sales-growth`, `/pr/20666771-headline-slug`, `/filing/310003947`, `/author/{slug}`.

`sa_referrer` is the path of the previous page, with no host, for example `/symbol/TGT/news`. `sa_query` is the query string. Omit it when you have none. Omit `sa_page_url`, `sa_referrer`, and `sa_query` when the operation does not list them.

## Errors

`400` is an invalid parameter. The body has `title: Bad Request` and a `request_id`. The field name is not in the JSON. Check the name and the enum in the YAML.

Another `400` is the string `invalid parameters`. The causes named in that text are `filter_since=0`, `filter_until=0`, and `page_number=0`.

An empty `204` means the route exists and there is no data for those parameters.

`502`, `503`, and `504` mean the response could not be obtained. The body is `{"error":{"status","title","request_id"}}`.
