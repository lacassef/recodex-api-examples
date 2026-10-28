# Examples

Host is `skalpha1.p.rapidapi.com`. Send `X-RapidAPI-Key` and `X-RapidAPI-Host` with it. The names are the OpenAPI names. Numeric ids (`62`, `4938289`, `4635195`) are TGT examples. Another ticker has another id.

## Market

Quote by id and by slug. One of the two is enough.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/quotes/realtime?sa_ids=62"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/quotes/realtime?sa_slugs=tgt,wmt,cost,dltr,bj,kr"
```

Daily price of TGT against the S&P.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/historical-prices?slug=tgt&slugs_list=tgt,sp500&from=2026-08-11&to=2026-09-30&sort=as_of_date"
```

A single date:

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/historical-prices?slug=tgt&filter_for_date=2026-09-30"
```

One-year chart. `62` is the TGT id in these examples.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/charts/lua?ticker_id=62&period=1Y"
```

Options chain. The date comes from `/symbols/TGT/option-expirations`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/TGT/option-expirations"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/options/chain?ticker_id=62&expiration_date=2026-10-02"
```

Session, day's movers, indices.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/market-open"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/day-watch?sort=percent_change"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/global-indices?include=tickers"
```

## Symbol

Profile, dividends, and peers. The dividends page groups by calendar year or fiscal year.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/dividends?years=5&group_by=year&sort=-date"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/suggested?source_type=similarities&variation=ds_v2"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/people_also_follow?include=sector,sub_industry"
```

Card news. `id` is the slug. You can omit it. Do not send `filter_since=0`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/news?filter_category=news_card&include=author,primaryTickers,secondaryTickers,sentiments,otherTags&page_size=12&lang=en"
```

Transcripts or slides. Filings on the financials tab. Press releases.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/transcripts?filter_only=transcripts&include=author,primaryTickers,secondaryTickers,sentiments&page_size=40&page_number=1"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/sec-filings?filter_filing_category=financials&include=formType&page_size=40&page_number=1"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/press-releases?include=author,primaryTickers&page_size=40&page_number=1"
```

The statement and the short chart series. Do not mix the two routes.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/fundamentals_metrics?period_type=annual&statement_type=income-statement&target_currency=USD"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/fundamentals?period_type=quarterly&filter_field=total_revenue&filter_limit=5"
```

Estimates and the growth aggregate. `ticker_ids` and `fields_list` are comma-separated.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data/estimates?ticker_ids=62&period_type=annual&estimates_data_items=eps_primary&relative_periods=0,1&group_by_month=false"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/fundamental-metrics?ticker_ids=62&fields_list=total_revenue_growth,total_revenue_3y_cagr,total_revenue_5y_cagr"
```

Metrics and grades. `minified` is `true` or `false`. `filter_fields` is comma-separated.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/metrics?filter_slugs=tgt&filter_fields=marketcap,tev,total_cash,total_debt&minified=false"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/ticker-metric-grades?filter_slugs=tgt&filter_fields=pe_nongaap,pe_ratio&filter_algos=main_quant,dividends&minified=false"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/sector_metrics?filter_fields=analysts_up,analysts_down,analysts_up_percent,analysts_down_percent"
```

Rating offsets `0`, `3`, and `6`. The batch route, with no slug in the path, takes `period_type=weeks`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/rating/periods?filter_periods=0,3,6"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/rating/periods?slugs_list=tgt,wmt&period_type=weeks&filter_periods=0,1,2,4"
```

The earnings summary points at a filing or a press release.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/earning_summaries?referral_type=press_release&referral_date=2026-09-29T06:01:00.000-04:00"
```

Top discussions and a ticker search with GICS.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbols/tgt/top_discussions?include=subject,subject.author,comments,comments.user&page_size=20&lang=en"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/tickers?filter_slugs=wmt,cost,dltr,bj,kr&include_gics=true&per_page=100"
```

## Content

List and trending. An article category and a news category do not mix. `stock-ideas` does not work on `/news`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles?filter_category=latest-articles&include=author,primaryTickers,secondaryTickers,sentiments&page_size=10&page_number=1&lang=en"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles/trending?filter_category=latest-articles&fields_article=title,links,author&fields_author=nick,image&include=author&page_size=10"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/news?filter_category=market-news::notable-calls-insights&fields_news=title,publish_on&include=primaryTickers,secondaryTickers&page_size=25&lang=en"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/news/trending?filter_category=market-news::all&include=author&page_size=25&page_number=1"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/full-news/trending?filter_category=market-news::trending&fields_news=title,date,comment_count&fields_tag=slug,name&include=primaryTickers,secondaryTickers&page_size=50&page_number=1"
```

Detail. The `sa_page_url` path is that item's `links.self`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles/4938289?include=author,primaryTickers,secondaryTickers,otherTags,presentations,presentations.slides,author.authorResearch,author.userBio&lang=en&sa_page_url=/article/4938289-target-corporation-tgt-q2-2026-earnings-call-transcript&sa_referrer=/filing/310003947"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles/4938289/author?include=authorResearch,userBioTags"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/article-page-content-recommendations?article_id=4938289&variation=variation_a"
```

News. `sa_referrer` is the path of the previous page, with no host.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/news/4635195?include=author,primaryTickers,secondaryTickers,otherTags&lang=en&sa_page_url=/news/4635195-target-projects-around-5-percent-fy2026-net-sales-growth&sa_referrer=/symbol/TGT/news"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/news-page-content-recommendations?market_current_id=4635195&variation=variation_b"
```

Comments. The map first, then the ids.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles/4938289/comment-maps?include=user&sort=-top_parent_id"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/articles/4938289/comments?comment_ids=103525208,103517498&include=user&sort=-top_parent_id"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/comments/103525208/sub-comments?include=user&sort=-top_parent_id"
```

A press release and a filing take `sa_page_url` with the page path.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/press-releases/20666771?include=acquireService,primaryTickers&sa_page_url=/pr/20666771-headline-slug"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/filings/310003947?include=ticker&sa_page_url=/filing/310003947"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/filings/pdf/310003947"
```

Home feed and education.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/feed?models_list=Article,MarketCurrent&page_size=10&include=author,primaryTickers,secondaryTickers&without_list=transcripts,earnings-slides,exclude-feed&any_primary_list=tgt&lang=en"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/education-top-articles?filter_category=education::investing&page_size=3&lang=en"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/leading-news-stories"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/breaking-news"
```

## Search, calendar, screener, ETF

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/search?term=tgt&limit=20&symbols=1&indices=1&crypto=1&actively_traded=1&currency=USD"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/searches?filter_query=tgt&filter_type=people,symbols,pages,shortcuts&filter_list=all&filter_period=all&page_size=6&page_number=1"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/searches/headlines?filter_query=tgt&filter_list=all&filter_period=quarter&filter_tags=transcripts,evergreen-seo&page_size=10"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/searches/people?filter_query=tgt&filter_list=all&filter_period=all&filter_defunct=true&page_size=10"
```

To include inactive people in the people search, send `filter_defunct=true`. Without that filter, omit the parameter.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/earnings-calendar/days?filter_start_date=2026-08-30&filter_end_date=2026-10-04&filter_with_rating=false&filter_currency=USD"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/earnings-calendar/tickers?filter_selected_date=2026-09-30&filter_with_rating=false&filter_currency=USD"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/screener-filters?type=stock&variation=show"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/screeners?type=etf"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/screeners/922b797269"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/etf-performance-categories"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/etf-performance-categories/key_markets"
```

ETF category examples: `key_markets`, `bonds`, `commodities`, `countries`, `currencies`, `strategies`, `cryptocurrency`. The list for a call is whatever `/etf-performance-categories` returns.

The hub sector and the aggregate by sector id. This is not `/symbols/{slug}/sector_metrics`.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/sectors-hub?sector=information-technology"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/sector-metrics?filter_fields=analysts_up_percent,analysts_down_percent&filter_sector_ids=25,45"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/dividend-investing"
```

Fundamental chart series and profile.

```sh
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data/charting?slugs_list=tgt&metrics=total_assets,total_liabilities,total_revenue&start=2025-09-30&end=2026-09-30"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data?slugs=TGT&fields_list=peRatioFwd,lastClosePriceEarningsRatio"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data/profile?slugs=tgt"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data/estimated-earning-announces?slug=tgt"
curl "https://skalpha1.p.rapidapi.com/api/skalpha/symbol-data/widgets?slug=TGT&date=1787149800"
```
