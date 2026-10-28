# Filing

A **Filing** JSON body is a [Resource](Resource.md). The PDF route is the file.

**Where you'll see it:** `/filings/{id}` and `/symbols/{slug}/sec-filings` return JSON. `/filings/pdf/{id}` returns the file, not JSON.

**Related models:** [Resource](Resource.md), [Ticker](Ticker.md).

`310003947` is the filing id in the [examples](../docs/guides/examples.md). Its `links.self` path in those examples is `/filing/310003947`. The detail example asks for `include=ticker`. The symbol list asks for `include=formType`.

`filter_filing_category` on the symbol list is `all`, `financials`, `news`, `proxies`, `tenders`, `ownership`, or `other`. Those are request values, not body keys.

This page does not name keys inside `formType` or `ticker`.
