# Workflows

A workflow is the order of calls and what you carry from one response into the next request. Each call is `GET /api/allscores/...`. Take the parameter names from that operation in the [OpenAPI](../openapi/allscores_openapi.yaml). Value shape is in [Parameters](request-essentials.md). Filled requests are in [Examples](examples.md).

Send only the parameters that step needs. Omit a value you are not changing.

## Scores for a day, then a game

1. Pick the sport from the [sport list](../reference/sport-ids.md).
2. Call `/games-scores`. Put the sport in `sport`. Put the day in `startDate` and `endDate`, in the locale short pattern. Omit `langId` when you want the default language.
3. Read the game id from `games`. That value is `gameId` on the game routes that ask for one game, and `games` on the routes that ask for a list.
4. Call `/game-details` with `gameId`. When you have home, away, and competition ids and no game id, send `matchupId` as `homeId-awayId-competitionId` instead.
5. Keep `currentSeasonNum`, competition id, and competitor ids from the game when the next page is a competition or a competitor.

Countries for that sport are `/countries` with `sportId`. The sports catalog is `/sports`. `withCount=true` adds per-sport game counts.

A short highlighted list is `/featured-games` or `/games-top`. The slider is `/games-slider`. Suggestions are `/games-suggestions`. A chosen set of competitions and competitors over a date range is `/custom-scores`, with `competitions` and `competitorIds`.

## Game page

You already have `gameId`. Pick the block. Do not call every game route up front.

1. Stats are `/game-stats`. Put the game id in `games`. `onlyIsMajor` keeps the headline stats. Read a `statisticsFilters` id and send it as `filterId` when you want that tab.
2. Pre-game comparison is `/stats-pregame`. That route calls the game id `game`.
3. Lineups are `/game-lineups` with `gameId`. Send `athleteId` when you want one player on that sheet. `matchWeekKey` selects a week.
4. Head to head is `/h2h` with `gameId` or `matchupId`. `addMainOdds` attaches the main line.
5. Highlights are `/game-highlights` with `competitors` or `competitions`. `numberOfGames` caps the list.
6. Point by point is `/point-by-point` with `gameId`, for a game that publishes that sequence, such as tennis or volleyball.
7. Commentary is `/playbyplay-comments`. Put the game id in `sportifiergameid`. Put the provider fixture key in `fixtureid`. `lang` is the numeric language id. This route does not take `langId`.

Send `lastUpdateId` from the previous response when you are refreshing that block.

## Competition

1. Call `/featured-competitions` or `/top-competitions` with `sport`, or call `/search` with the text in `query`.
2. Read `id` from `competitions`. That value is `competition` on details, standings, brackets, and stats. The same id, comma-separated when you send more than one, is `competitions` on fixtures, results, history, and team of the week.
3. Call `/competition-details`. `withSeasons` adds seasons. `type` is empty, `stats`, or `standings`.
4. Read `currentSeasonNum` and `currentStageNum`. Call `/competition-standings` with `competition`, `seasonNum`, and `stageNum`. On this route `type` is the table layout, such as `1` or `6`. Send `competitor` when the table should highlight that side.
5. Upcoming games are `/fixtures`. Finished games are `/results`. Both take `competitions` or `competitorIds`.
6. Read `paging.nextPage` or `paging.previousPage`. Call `/paging` with that string in `paging`.
7. The draw is `/competition-brackets`. Past winners are `/competition-history`. The published selection is `/competition-team-of-the-week`, with `weekKey` when you want one week. Season leaders are `/stats` with `competition`.

## Competitor

1. Take the competitor id from `/top-competitors` or from `competitors` on `/search`. Read `id`.
2. Call `/competitor-details` with `competitorId`. `withSeasons` adds the competitions that competitor is in. `isDashboard=true` is the dashboard view.
3. Squad is `/competitor-squads` with `competitorId`.
4. Games in progress are `/competitor-current-games` with `competitorId`.
5. The form strip is `/competitor-recent-form`. This route calls the id `competitor`. `numOfGames` is how many recent games.
6. Transfers are `/transfers` with `competitors` or `competitions`. `onlyConfirmed` keeps confirmed deals. `lastTransferId` is the cursor of the last transfer already shown.
7. Linked competitions and athletes are `/related-entities` with `competitors`.

Fixtures and results for that competitor use `competitorIds`.

## Athlete

1. Call `/search` with `query`, or `/top-athletes` with `sportType`.
2. Read the athlete id from `athletes`. Call `/athlete-details` with `athleteId`. `fullDetails=true` adds the bio, matches, transfers, trophies, and career stats. `competitionId` scopes the profile. The same operation also accepts `competition`.
3. Games are `/athlete-games` with `athleteId` and, when you want one competition, `competitionId`.
4. Career is `/athlete-career`. `seasonKey` `-1` is every season.
5. One competition's record is `/athlete-trophy-stats` with `athleteId` and `competitionId`.
6. The next game is `/athlete-next-game` with `athletes`. `fullDetails` expands that game.
7. Shot and goal charts are `/athlete-chart-events` with `athletes`.

## News

1. Call `/news` with `sport`, or with `games`, `competitions`, `competitors`, or `athletes`.
2. `isPreview` selects the short list. Omit it for the full list.
3. Read `id`, `title`, `publishDate`, `image`, and `url` from each card. There is no separate article route.

## Odds

1. Lines for a game are `/game-bet-line` with the game id in `games`.
2. The best price is `/best-odds`. Send `games`, or send `competition`, `sport`, `minGames`, and `maxGames` for a competition window.
3. Outrights are `/bets-outrights` with `competitors`, `athletes`, or `competitions`. Read `lineId`. Call `/bets-outright-details` with that `lineId`. An entity with no market returns an empty object and HTTP `200`.
4. Trend cards are `/trends`, with `games` or with `sportType` and `date`. Read `trend.id`. Call `/trend-details` with `trendId`.
5. Proposition markets are `/bets-proposition` with `gameId`. Send `athleteId` to limit the markets to one athlete.
6. The teaser is `/bets-teaser` with `gameId`. Prediction cards are `/game-predictions` with `competitors`. Contextual predictions are `/game-predictions-contextual`.

## Images

Take `imageVersion` from the country, sport, competitor, or athlete you already loaded.

1. Athlete photo: `/img/small/athlete/{athleteId}/version/{imageVersion}` or the `large` route. Small is 40x40. Large is 84x84.
2. Competitor logo: `/img/small/competitor/{competitorId}/version/{imageVersion}` or `large`. Small is 34x34. Large is 64x64.
3. Competition list logo: the `light` routes, with `countryId`, `competitionId`, and `imageVersion`. Small is 24x24. Large is 40x40. `countryId` is the fallback flag.
4. The other competition logo routes are 20x20 and 68x68.
5. The flag is `/img/flag/country/{countryId}`. It has no image version. The trophy is `/img/trophy/{trophyId}`. It has no image version.

The body is `image/png`.
