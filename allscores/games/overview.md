# Games

One game. Take `gameId` from `games` on a scores list, or send `matchupId` as `homeId-awayId-competitionId` on the routes that list it. Filled calls are in [Examples](../guides/examples.md).

## Details

GET `/api/allscores/game-details`

- `gameId` or `matchupId`
- `lastUpdateId`, `topBookmaker`

The body has status, start time, clock, venue, officials, stage scores, events, lineups when present, top performers, and members.

## Statistics

GET `/api/allscores/game-stats`

- `games` — the game id, or several
- `onlyIsMajor`
- `filterId` — a `statisticsFilters` id from a previous stats response
- `lastUpdateId`

GET `/api/allscores/stats-pregame`

- `game` — the game id on this route
- `onlyMajor`

Live and finished stats stay on game-stats.

## Lineups, meetings, highlights

GET `/api/allscores/game-lineups`

- `gameId`
- `athleteId`, `matchWeekKey`

GET `/api/allscores/h2h`

- `gameId` or `matchupId`
- `addMainOdds`
- `lastUpdateId`, `topBookmaker`

`game.h2hGames` lists the previous meetings.

GET `/api/allscores/game-highlights`

- `competitors` or `competitions`
- `numberOfGames`, `roundKey`

A competitor with no clips still returns `lastUpdateId` and `ttl`.

## Point by point and commentary

GET `/api/allscores/point-by-point`

- `gameId`

GET `/api/allscores/playbyplay-comments`

- `lang` — numeric language id
- `fixtureid` — provider fixture key
- `sportifiergameid` — game id
- `appType` — omit for the default
- `isLive`, `IsFinished`, `onlyPreview`

The body has `Messages`, `UpdateURL`, and `TTL`. This route does not take `langId`, `timezone`, `publisherId`, `campaign`, or `userCountryId`. `IsFinished` keeps that capitalization.
