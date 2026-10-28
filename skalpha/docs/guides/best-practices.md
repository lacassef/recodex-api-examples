# Best practices

Send the parameters the operation lists in the OpenAPI, with the enum values. The rest of this page is what the screens ask for.

## Send only the fields you need

News list: `include=primaryTickers,secondaryTickers` and a `page_size` of 5, 10, or 25. Filings: `include=formType`. Article author: `include=authorResearch,userBioTags`. Use the include for that resource.

`fields_news`, `fields_article`, and `fields_tag` shrink the object. Article trending: `fields_article=title,links,author` and `fields_author=nick,image`. Without those fields, the list is larger.

## Omit empty values

Do not send an empty value.

- With no time bound, omit `filter_since` and `filter_until`. Do not send `0`.
- The first page is `page_number=1`, or omit it. Do not send `0`.
- Do not send a parameter the operation does not list, such as `isMounting`.
- `lang` is `en` or absent. Do not send `undefined`.
- On tickers, GICS is `include_gics=true`. Do not send `include=undefined`.
- Without the related-analysis filter, omit `filter_related`.
- On the feed, `without_list` takes real tokens: `transcripts`, `earnings-slides`, `exclude-feed`.

On the calendar, `filter_with_rating=false` is the value the call sends.

## Lists

Separate with commas in the parameter the operation lists: `filter_slugs=tgt,wmt`, `ticker_ids=62,1433`, `fields_list=pe_nongaap,pe_ratio`, `comment_ids=103368775,103339973`.

The field name changes by route. `/metrics` uses `pe_nongaap`. `/symbol-data` uses `peRatioFwd`. Copy the name from that route's example.

## Pagination

`page_size` is 1 to 50. Ask for the size you need, not the maximum, except `full-news/trending`, which uses 50. Analysis, filings, transcripts, and press releases for one symbol use 40.

`page_number` is 1-based. A high `page_size` with a long `include` is the heaviest request. Hold the next page until you need it.

`per_page` is only on `/tickers`, with a ceiling of 100. The page sends 100.

## Dates in the same format

`from`, `to`, and `filter_for_date` use `YYYY-MM-DD`. On a range, use the same format.

`referral_date` is ISO-8601 with an offset, such as `2026-09-29T06:01:00.000-04:00`.

`relative_periods` runs from -23 to 23. Outside that range the response is `400`.

## Numeric id and slug

The slug identifies the page (`tgt`, `btc-usd`; `BRK.B` fits the pattern because of the dot). The numeric id identifies the quote, the option, the LUA chart, and estimates. Find the id at `/quotes/realtime?sa_slugs=tgt` or on the profile. Do not hardcode `62` outside the TGT example.

Case: `/symbols/tgt/...` and `/symbols/TGT` both appear on the pages. Pick one case per resource and reuse it.

## Content detail

For an article and a news item, send `sa_page_url` with the `links.self` path, including the title slug. `sa_referrer` is the path of the previous page, with no host.

Press releases, filings, and authors use the same parameter when the operation lists it: `/pr/{id}-{slug}`, `/filing/{id}`, `/author/{slug}`.

Do not send an account cookie or token.

## Cache and repeats

Read the response `Cache-Control` before repeating the same URL. Fire the list once and page through it.

## Error without a field name

A `400` with `title: Bad Request` does not name the parameter. Check the name and the enum in the YAML. A `400` with the string `invalid parameters` names `filter_since=0`, `filter_until=0`, and `page_number=0`.

An empty `204` means there is no data for those parameters. Do not repeat the same request.

`502`, `503`, and `504` mean the response could not be obtained. The body is `{"error":{"status","title","request_id"}}`.

## What is left out

There is no `POST /screener-results`. For a screener, read `/screener-filters?type=stock&variation=show`, the list at `/screeners?type=stock`, and the definition at `/screeners/{id}`.

There is no route outside the OpenAPI list.
