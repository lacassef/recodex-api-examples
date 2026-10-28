# SymbolData

**SymbolData** is the object whose keys are the names you sent in `fields_list`.

**Where you'll see it:** `/symbol-data` and `/fundamental-metrics`. Estimates use `/symbol-data/estimates`.

**Related models:** [Ticker](Ticker.md). `slugs` on symbol data takes the slug. `ticker_ids` on fundamental metrics takes the numeric id.

A listed name is a key you asked for. It is not a key every response includes. Names in the guides:

- `peRatioFwd`, `lastClosePriceEarningsRatio`
- `pe_nongaap`, `pe_ratio`
- `total_revenue_growth`, `total_revenue_3y_cagr`, `total_revenue_5y_cagr`

`62` is the ticker id for those growth fields in the [examples](../docs/guides/examples.md). `TGT` is the slug for the ratio fields there.
