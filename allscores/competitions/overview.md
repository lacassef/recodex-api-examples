# Competitions

Take the competition id from `id` on `competitions` in a list or in search. Details, standings, brackets, and stats call it `competition`. Fixtures, results, history, and team of the week call it `competitions`. Filled calls are in [Examples](../guides/examples.md).

## Lists

GET `/api/allscores/featured-competitions`

- `sport`, `competitions`, `countries`, `limit`
- `withSeasons`
- `type` — empty, `stats`, or `standings`

GET `/api/allscores/top-competitions`

- `sport`, `limit`, `countries`

Each competition has `id`, `name`, `countryId`, `sportId`, `currentSeasonNum`, `currentStageNum`, and flags such as `hasStandings`, `hasBrackets`, `hasStats`, `hasTransfers`, and `hasBets`.

## One competition

GET `/api/allscores/competition-details`

- `competition`
- `withSeasons`, `withBestOdds`, `isDashboard`
- `type` — empty, `stats`, or `standings`
- `sport`, `countries`, `limit`, `lastUpdateId`

GET `/api/allscores/competition-standings`

- `competition`, `seasonNum`, `stageNum`
- `competitor` — highlights that side
- `withSeasonsFilter`, `live`, `isPreview`, `groupCategory`
- `type` — table layout, such as `1` or `6`
- `context`, `lastUpdateId`

`seasonNum` comes from `currentSeasonNum`. `stageNum` comes from `currentStageNum`.

GET `/api/allscores/competition-brackets`

- `competition` or `competitor`
- `live`, `type`, `topBookmaker`, `lastUpdateId`

GET `/api/allscores/competition-history`

- `competitions`

GET `/api/allscores/competition-team-of-the-week`

- `competitions`, `weekKey`

A competition with no published selection returns an empty object and HTTP `200`.

## Fixtures, results, leaders

GET `/api/allscores/fixtures`

GET `/api/allscores/results`

- `competitions` or `competitorIds`
- `includeTopBettingOpportunity`
- the score filters this operation lists
- `lastUpdateId`

Both return `games`, `summary`, `competitionFilters`, and `paging`. Pass `paging.nextPage` or `paging.previousPage` to `/paging`.

GET `/api/allscores/stats`

- `competition` for the leader table, or `competitorId` for one side
- `phaseNum`, `withSeasons`

`stats.athletesStats` and `stats.competitorsStats` are tables.
