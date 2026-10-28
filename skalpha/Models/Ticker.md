# Ticker

A **Ticker** is a symbol attached to an item, or a row from `/tickers`.

**Where you'll see it:** `include` values `primaryTickers`, `secondaryTickers`, and `tickers`. `/tickers` loads metadata by slug. `include_gics=true` includes the classification. The guides do not name the key that holds it.

**Related models:** [Article](Article.md), [NewsItem](NewsItem.md), [SymbolData](SymbolData.md).

The guides do not name the keys inside a ticker object. What you carry next is already named as a parameter:

- The slug goes to `/symbols/{slug}` and to `slug`, `slugs`, `slugs_list`, and `sa_slugs`. `tgt` and `TGT` are different path values. The examples use `tgt` in a symbol path and `TGT` in `slugs`.
- The numeric id goes to `ticker_ids`, `ticker_id`, and `sa_ids`. `62` is the id in the fundamental-metrics example.

The guides do not name the JSON keys inside this object. Read the slug from autocomplete. Read the numeric id from the profile or from the quote. Which call that is, is in [Workflows](../docs/guides/workflows.md#quote-a-ticker).
