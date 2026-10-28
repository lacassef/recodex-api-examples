# Bets

Odds on a game, a competition, or a futures market. Omit `showOdds` on a scores route when you do not want odds there. These routes are the lines themselves. Filled calls are in [Examples](../guides/examples.md).

## Lines

GET `/api/allscores/game-bet-line`

- `games`, `lastUpdateId`

GET `/api/allscores/best-odds`

- `games`, or `competition` with `sport`, `minGames`, and `maxGames`
- `lineType`, `bookmakerId`, `context`, `withCompetitionFilter`, `topBookmaker`, `lastUpdateId`

The body has `lines`, `lineTypes`, `bookmakers`, and the games those lines belong to.

GET `/api/allscores/bets-proposition`

- `gameId`, `athleteId`
- `topBookmakerId`, `topBookmaker`, `fullData`

GET `/api/allscores/bets-teaser`

- `gameId`, `topBookmaker`

`bookmakers` can be empty.

GET `/api/allscores/bets-raffle-bookmaker`

Shared parameters only. `bookmakers` can be an empty array and the status can still be HTTP `200`.

## Outrights

GET `/api/allscores/bets-outrights`

- `competitors`, `athletes`, or `competitions`
- `lineTypeId`, `withProbabilityText`, `context`, `topBookmaker`, `lastUpdateId`

An entity with no outright market returns an empty object and HTTP `200`.

GET `/api/allscores/bets-outright-details`

- `lineId` from the outright
- `lastUpdateId`

`entityType` `4` is the competitor. An unknown `lineId` returns those ids as `0` and empty sports and countries.

## Trends and predictions

GET `/api/allscores/trends`

- `games`, or `sportType` and `date`
- `competition`, `competitor`, `matchupId`, `numOfGames`
- `isTop`, `context`, `topBookmaker`, `lastUpdateId`

A quiet date can return only `lastUpdateId` and `ttl`.

GET `/api/allscores/trend-details`

- `trendId` from `trend.id`
- `topBookmaker`, `lastUpdateId`

GET `/api/allscores/game-predictions`

- `sport`, `competitors`, `games`, `relation`
- the other score filters this operation lists

GET `/api/allscores/game-predictions-contextual`

- `sport`, `competitions`, `competitors`, `context`, `showOdds`
- the other score filters this operation lists

Each game can include `promotedPredictions` and `playersBetsPredictions`.
