# Building a request

Every route is `GET /api/allscores/...`. There is no body. Image routes put the ids in the path. The other routes put them in the query.

Filled calls are in [Examples](examples.md). The order of calls is in [Workflows](workflows.md).

## Steps

1. Open the operation in the [OpenAPI](../openapi/allscores_openapi.yaml) or in the [map](../README.md).
2. Copy that operation's parameter names. Do not invent a name and do not reuse another route's query.
3. Fill in the required ones. An optional parameter goes in only when you want that value.
4. Take the value shape from [Parameters](request-essentials.md).
5. Omit `langId`, `timezone`, `publisherId`, `campaign`, and `userCountryId` when the default is the value you want.

## Choosing the id

`sport`, `sportId`, and `sportType` come from the [sport list](../reference/sport-ids.md). `1` is football. Countries use `sportId`. Trends and top athletes use `sportType`. The other sport filters use `sport`.

The competition id comes from `id` on a competition in featured competitions, top competitions, or search. Details, standings, brackets, stats, trends, and best odds call it `competition`. Athlete games and trophy stats call it `competitionId`. A comma-separated list is `competitions`.

The competitor id comes from `id` on a competitor in top competitors or search. Details, current games, and squads call it `competitorId`. Recent form, standings, brackets, and trends call it `competitor`. Fixtures, results, and custom scores call a list `competitorIds`. The other lists call it `competitors`.

The game id comes from `games` on a scores list. Details, head to head, lineups, point by point, proposition, and teaser call it `gameId`. Pre-game stats call it `game`. Play-by-play calls it `sportifiergameid`. A list of game ids is `games`.

`matchupId` is `homeId-awayId-competitionId` when you have those three ids.

The athlete id comes from the athletes list on search or top athletes. Details, games, career, and trophy stats call it `athleteId`. Next game, chart events, news, and outrights call a list `athletes`.

`currentSeasonNum` and `currentStageNum` on a competition are `seasonNum` and `stageNum` on standings.

`imageVersion` on a country, sport, competitor, or athlete is the `imageVersion` in the image path.

`trend.id` is `trendId`. `lineId` on an outright is `lineId` on outright details. `statisticsFilters` on game stats supplies `filterId` for the next stats call. `paging.nextPage` and `paging.previousPage` are the `paging` value.
