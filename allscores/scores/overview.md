# Scores

Score lists and the catalogs behind them. Shared parameters and the score filters are in [Parameters](../guides/request-essentials.md). Filled calls are in [Examples](../guides/examples.md).

## Sports

GET `/api/allscores/sports`

- `withCount` — per-sport game counts
- `lastUpdateId`

Each sport has `id`, `name`, `nameForURL`, and `imageVersion`.

## Countries

GET `/api/allscores/countries`

- `sportId`
- `countries` — comma-separated country ids
- `lastUpdateId`

Each country has `id`, `name`, `nameForURL`, `imageVersion`, `sportTypes`, `totalGames`, and `liveGames`.

## Day scores

GET `/api/allscores/games-scores`

- `sport`
- `startDate`, `endDate`
- `onlyMajorGames`, `onlyLiveGames`, `withTop`
- `competitions`, `competitors`, `games`, `relation`
- the other score filters this operation lists
- `lastUpdateId`

This route does not take `showOdds`.

## Highlighted games

GET `/api/allscores/featured-games`

- `sport`, `competitions`, `competitors`, `numberOfGames`
- `context`, `showOdds`
- the other score filters this operation lists

GET `/api/allscores/games-top`

GET `/api/allscores/games-slider`

GET `/api/allscores/games-suggestions`

These three take `sport`, `startDate`, `endDate`, `showOdds`, `context`, `numberOfGames`, `matchupId`, `includeTopBettingOpportunity`, and the other score filters the operation lists. The slider body matches games-top. Suggestions can be an empty list when you send only `sport`.

## Custom scores

GET `/api/allscores/custom-scores`

- `competitions`, `competitorIds`
- `startDate`, `endDate`
- the other score filters this operation lists

## Next page

GET `/api/allscores/paging`

- `paging` (required) — `paging.nextPage` or `paging.previousPage` from fixtures or results
- `publisherId`, `campaign`, `userCountryId`

This route does not take `langId` or `timezone`.
