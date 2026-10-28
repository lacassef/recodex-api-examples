# Symbols

The prefix is `/api/skalpha/symbols/{slug}`, except two routes: the batch `/api/skalpha/symbols/rating/periods` and the search `/api/skalpha/tickers`. Slug: letters, digits, and `: . _ -`.

On `analysis`, `news`, `transcripts`, `press-releases`, and `related-analysis`, `id` is the slug (`tgt`, `btc-usd`). You can omit it: the route uses the path slug. It is not a cursor.

With no time bound, omit `filter_since` and `filter_until`. Do not send `0`.

## Profile and neighbors

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}` | Ticker profile. | `slug` | `lang` | Examples: `TGT`, `BTC-USD`. |
| `/api/skalpha/symbols/{slug}/random` | Another symbol from the same batch. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/insiders_sell_buy` | Insider buys and sells. | `slug` | — | — |
| `/api/skalpha/tickers` | Metadata by slug. | `filter_slugs` | `include_gics`, `per_page`, `include` | `include_gics=true` to include the classification. `per_page` up to 100. |

## Events and position

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}/dividends` | Dividend history. | `slug` | `years`, `group_by`, `sort` | `group_by`: `year`, `fiscal_year`, `month`. Sort example: `-date`. `years`: 1, 5, or 12. |
| `/api/skalpha/symbols/{slug}/splits` | Splits. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/option-expirations` | Dates for the chain. | `slug` | — | The next step is `/options/chain` with the numeric id. |
| `/api/skalpha/symbols/{slug}/payout_ratios` | Payout by period. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/shares` | Count and float. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/invested_etfs` | ETFs that hold the symbol. | `slug` | — | — |

## Fundamentals

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}/fundamentals_metrics` | Statement in the requested currency. | `slug`, `period_type`, `statement_type`, `target_currency` | — | `period_type`: `annual`, `quarterly`, `ttm`, `non_periodic`. `statement_type`: `income-statement`, `balance-sheet`, `cash-flow-statement`. Currency example: `USD`. |
| `/api/skalpha/symbols/{slug}/fundamentals` | One field's series, for a chart. | `slug`, `period_type`, `filter_field`, `filter_limit` | `lang` | This is not the route above. `period_type`: `annual` or `quarterly`. Field: `ffo_per_share_diluted`, `reported_diluted_eps_excl_extra_items`, `total_revenue`. Limit 7 for EPS and FFO, 5 for revenue. |
| `/api/skalpha/symbols/{slug}/earning_summaries` | Earnings card. | `slug` | `referral_type`, `referral_date` | Type: `filings`, `presentation`, `press_release`, `transcript`. ISO-8601 date. |
| `/api/skalpha/symbols/{slug}/sector_metrics` | Metrics for the symbol's sector. | `slug` | `filter_fields` | Comma-separated: `pe_nongaap,pe_ratio` or `analysts_up,analysts_down,analysts_up_percent,analysts_down_percent`. |
| `/api/skalpha/symbols/{slug}/etf_category_metrics` | Median of the ETF category. | `slug` | `filter_fields`, `filter_fund_type` | Fields comma-separated. Dividend example: `filter_fund_type=cef`. |

## Symbol research and filings

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}/analysis` | Analysis for the symbol. | `slug` | `filter_related`, `filter_since`, `filter_until`, `id`, `include`, `page_size`, `page_number` | Example include: `author,primaryTickers,secondaryTickers`. Omit `filter_related` when you do not want that filter. |
| `/api/skalpha/symbols/{slug}/related-analysis` | Related analysis. | `slug` | `filter_since`, `filter_until`, `id`, `include`, `page_size`, `page_number` | Same include. |
| `/api/skalpha/symbols/{slug}/news` | News for the symbol. | `slug` | `filter_category`, `filter_since`, `filter_until`, `id`, `include`, `page_size`, `page_number` | Categories: `dividend_news`, `earnings_news`, `m_n_a_news`, `news_card`. Omitting it returns all of them. Include: `author,primaryTickers,secondaryTickers,sentiments,otherTags`. |
| `/api/skalpha/symbols/{slug}/press-releases` | Press releases. | `slug` | `filter_until`, `id`, `include`, `page_size`, `page_number` | Example include: `author,primaryTickers`. |
| `/api/skalpha/symbols/{slug}/sec-filings` | Filings for the symbol. | `slug` | `filter_filing_category`, `include`, `page_size`, `page_number` | `all`, `financials`, `news`, `proxies`, `tenders`, `ownership`, `other`. Include `formType`. |
| `/api/skalpha/symbols/{slug}/transcripts` | Transcripts and slides. | `slug` | `filter_only`, `filter_until`, `id`, `include`, `page_size`, `page_number` | `filter_only`: `transcripts` or `earnings-slides`. |
| `/api/skalpha/symbols/{slug}/faq` | Questions for the symbol. | `slug` | `lang` | — |

## Ratings and discussion

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}/author_ratings` | Author ratings. | `slug` | `include`, `filter_type`, `page_size`, `page_number` | Include `article,author`. `filter_type`: `very_bullish`, `bullish`, `neutral`, `bearish`, `very_bearish`, comma-separated. Example: `page_size=3`. |
| `/api/skalpha/symbols/{slug}/rating/periods` | Offsets for one symbol. | `slug` | `filter_periods` | Example: `0,3,6`. `0` is the current week. |
| `/api/skalpha/symbols/rating/periods` | The same, in a batch. | `slugs_list`, `period_type` | `filter_periods` | `slugs_list=tgt,wmt` and `period_type=weeks`. Offsets: `0`, `1`, `2`, `4`. |
| `/api/skalpha/symbols/{slug}/rating/histories` | Daily history. | `slug` | `filter_from`, `page_size`, `page_number` | Example: `page_number=1`. |
| `/api/skalpha/symbols/{slug}/discussions` | Recent threads. | `slug` | `include`, `page_size` | No `page_number` on this route. |
| `/api/skalpha/symbols/{slug}/top_discussions` | Top threads. | `slug` | `include`, `page_size`, `page_number` | Example include: `subject,subject.author,comments,comments.user`. `page_size=20`. |

## Discovery

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/symbols/{slug}/people_also_follow` | Co-followed symbols. | `slug` | `include` | Example: `include=sector,sub_industry`. |
| `/api/skalpha/symbols/{slug}/suggested` | Suggestions. | `slug` | `source_type`, `variation` | Card: `similarities`. Peers tab: `peers_similarities`. `variation=ds_v2`. |
| `/api/skalpha/symbols/{slug}/peers/stocks/most_mentioned` | Stocks most mentioned together. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/peers/stocks/people_follow` | Co-followed stocks. | `slug` | — | — |
| `/api/skalpha/symbols/{slug}/peers/etfs/exposure` | ETFs with exposure. | `slug` | — | — |
