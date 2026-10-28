# Athletes

Take the athlete id from search or from top athletes. Details, games, career, and trophy stats call it `athleteId`. Next game and chart events call a list `athletes`. Filled calls are in [Examples](../guides/examples.md).

## Profile

GET `/api/allscores/top-athletes`

- `sportType`, `limit`

GET `/api/allscores/athlete-details`

- `athleteId` — one id, or several separated by commas, such as `817,45579`
- `competitionId` or `competition`
- `fullDetails`, `topBookmaker`

Without `fullDetails`, each athlete has age, position, club, and nationality. `fullDetails=true` adds jersey, contract, injury, `shortBio`, `highlightStats`, `lastMatches`, transfers, trophies, and `careerStats`.

## Games and career

GET `/api/allscores/athlete-games`

- `athleteId`, `competitionId`
- `statType`, `lastMatchLimit`

GET `/api/allscores/athlete-career`

- `athleteId`
- `seasonKey` — `-1` is every season

GET `/api/allscores/athlete-trophy-stats`

- `athleteId`, `competitionId`

`stats` is a table with columns, rows, and the competitor that row belongs to.

GET `/api/allscores/athlete-next-game`

- `athletes`, `fullDetails`
- `lastUpdateId`, `topBookmaker`

GET `/api/allscores/athlete-chart-events`

- `athletes`

`chartEvents` includes zones, penalty totals, and events with pitch position, plus the games those events belong to.
