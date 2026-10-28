# Competitors

Take the competitor id from `id` on `competitors` in top competitors or search. Details, current games, and squads call it `competitorId`. Recent form calls it `competitor`. Filled calls are in [Examples](../guides/examples.md).

## List and profile

GET `/api/allscores/top-competitors`

- `sport`, `limit`, `withSeasons`, `isDashboard`
- `promoteNational` — omit to leave national teams unpromoted

GET `/api/allscores/competitor-details`

- `competitorId`
- `withSeasons`, `isDashboard`, `lastUpdateId`

The body has `name`, `symbolicName`, colors, `mainCompetitionId`, and flags such as `hasSquad`, `hasTransfers`, `hasTrophies`, and `hasHighlights`.

## Squad, current games, form

GET `/api/allscores/competitor-squads`

- `competitorId`

`squads` groups athletes by position.

GET `/api/allscores/competitor-current-games`

- `competitorId` or `competitions`
- `includeTopBettingOpportunity`
- the score filters this operation lists

This route does not take `showOdds`.

GET `/api/allscores/competitor-recent-form`

- `competitor`
- `numOfGames`

## Transfers and related entities

GET `/api/allscores/transfers`

- `competitions` or `competitors`
- `onlyConfirmed`, `limit`, `lastTransferId`, `lastUpdateId`

Each transfer has `id`, `type`, origin, target, time, price, `athleteId`, and `statusName`.

GET `/api/allscores/related-entities`

- `competitors`, `competitions`, or `athletes`

Each related entity has `id`, `name`, and `nameForURL`.
