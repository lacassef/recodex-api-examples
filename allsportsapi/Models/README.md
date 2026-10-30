# Models

Shapes of the JSON you parse, and how those objects link. Paths are in [Routes](Routes.md). Parameters and operation ids are in [openapi/](../openapi/).

A `200` body is the payload for that route. A `204` body is empty: the route is valid and there is nothing for those parameters. Do not parse it as JSON. Error bodies are in the [FAQ](../FAQ.md#what-does-204-mean-and-what-does-an-error-look-like).

## The data model

```
Sport
└── Category              country, region, or tour (England, ATP)
    └── UniqueTournament  the competition across seasons (Premier League)
        └── Season        one edition (Premier League 24/25)
            └── Tournament / UniqueStage / Round
                └── Event  one match
                    ├── Team (home and away)
                    │   ├── Player
                    │   └── Subteam
                    ├── Status
                    ├── Time
                    ├── Score
                    ├── Incidents
                    └── EventStatistics
```

- A **Category** groups **UniqueTournaments**. Walk category, then the tournaments in it, to list the competitions in a sport.
- A **UniqueTournament** is the competition that stays the same across years. A **Tournament** plus a **Season** is one edition, group, or stage. `tournament.uniqueTournament.id` is the competition id that schedule routes expect. `tournament.id` is that edition or group.
- An **Event** is one match. It points at its tournament, season, both teams, a status, a clock, and a score.
- A **Player** belongs to a **Team**. A move between teams is a **Transfer**.

Recipes for leagues, a full day, the match clock, and incidents are in the [FAQ](../FAQ.md) and [Workflows](../Workflows.md).

## Keys at the top of a 200 body

| What you asked for | Key |
|--------------------|-----|
| A list of matches | `events` |
| One match | `event` |
| A player | `player` |
| Categories | `categories` |
| League tables | `standings` (each entry has `rows`) |
| Competitions in a category | `groups`, then `uniqueTournaments` inside each group. Some responses also put `uniqueTournaments` at the top level |
| Competitions on a date | `scheduled`, `hasNextPage`, `timezoneEventCount` |
| Odds for one match | `markets` and `eventId` |
| Featured odds | `featured` and `hasMoreOdds` |

Read the key for that route. Extra keys can appear. Ignore the ones you do not use. A missing key and `null` mean the same thing: that fact is not in this response. Coverage depends on the sport, the competition, and the match.

Timestamps are Unix seconds. `startTimestamp` on an [Event](Event.md) is the start in UTC.

## Shotmaps and heatmaps

A `200` body is the object below. A `204` has no body. Drawing steps are in [Footapi](../Footapi/README.md) and [Basketapi](../Basketapi/README.md).

### Football shots

`GET /api/match/{id}/shotmap` and `GET /api/match/{id}/player/{playerId}/shotmap` return `{ "shotmap": [ ... ] }`.

Each item has `playerCoordinates` `{x, y, z}`, `goalMouthCoordinates` `{x, y, z}`, and `blockCoordinates` `{x, y, z}` when the shot was saved or blocked. `shotType` is `goal`, `save`, `post`, `miss`, or `block`. `situation` and `bodyPart` use hyphens (`set-piece`, `fast-break`, `free-kick`, `left-foot`). `goalType`, when present, is `regular`, `penalty`, or `own`.

`draw` is what the attacking-third graphic uses. `draw.start.x` is `playerCoordinates.y` and `draw.start.y` is `playerCoordinates.x`. On that graphic `x` is 0–100 across the pitch and `y` is 0 on the goal line, growing to about 35. The line ends at `draw.block` when that point exists, otherwise at `draw.end` (`end.y` is 0). `draw.goal` is a separate goal-mouth picture: `goal.y = 100 - goalMouthCoordinates.z`. Do not plot `draw.goal` on the 35-deep pitch.

`goalMouthCoordinates.x` is usually 0. `y` runs across the goal, 0–100 (right-to-left from the shooter's view). `z` is the height, 0–100. `draw.end.x` is `100 - goalMouthCoordinates.y`.

`GET /api/match/{id}/player/{playerId}/goalkeeper-shotmap` is a separate route. This page does not list its item keys.

### Football heatmaps

| Route | Body |
|-------|------|
| Player in a match, `GET /api/match/{id}/player/{playerId}/heatmap` | `heatmap`: array of `{x, y}` |
| Team in a match, `GET /api/match/{id}/team/{teamId}/heatmap` | `playerPoints` and `goalkeeperPoints`, each an array of `{x, y}` |
| Player in a season, `GET /api/player/{id}/tournament/{tournamentId}/season/{seasonId}/heatmap` | `points`: array of `{x, y, count}`; `matches` is an integer; `events` is an array |

`x` and `y` are 0–100 on the full pitch. On a season map, `count` is already how many times that point was visited. Draw a team map from both `playerPoints` and `goalkeeperPoints`. Team `x` can be fractional.

### Basketball shots

Both routes return `{ "shotmap": [ ... ] }`. The origin `(0, 0)` is the basket. `x` is about −250 to 250. `y` grows from the basket toward half-court and can be slightly negative.

| Route | Each item |
|-------|-----------|
| Team, `GET /api/basketball/match/{id}/team/{teamId}/shotmap` | `x`, `y`, `made`, `missed`, `saved` |
| Player, `GET /api/basketball/match/{id}/player/{playerId}/shotmap` | `x`, `y`, `type`, `typeName`, `isHome`, `id`, `period` |

On a player shot, `type` 1 and `typeName` `"made"` are a make. `type` 0 and `"missed"` are a miss. `period` is a quarter label such as `1Q` or `2Q`.

## Routes

[Routes.md](Routes.md) lists every published path once. `{sport}` stands for the sport slug (`basketball`, `tennis`, `esport`, `ice-hockey`, and the rest). Football match, player, and team routes have no slug.

The comment on each row is the summary for that route. Names in the Query column are optional query parameters. `page` on search, team, and player lists starts at 0. `page` on `scheduled-tournaments` starts at 1. Season player statistics use a `page` that starts at 1, and `limit` is required from page 2.

Path placeholders are the names in the path: `id`, `playerId`, `teamId`, `tournamentId`, `seasonId`, `categoryId`, `date`, `entityType`, and the others written there. Send those names. `{day}`, `{month}`, and `{year}` are unpadded integers. `{date}` is `YYYY-MM-DD`.

## Entity pages

The type in parentheses is a JSON type (`string`, `number`, `boolean`, `array of X`) or the name of another object (`Score`, `Team`, `Status`). A name with its own page is in the tables below. Field names are camelCase, exactly as written. A listed field is a key that appears. It is not a promise that every response includes it.

### Core hierarchy

| Model | What it represents |
|-------|--------------------|
| [Category](Category.md) | A country, region, or tour that groups competitions. |
| [UniqueTournament](UniqueTournament.md) | A competition that persists across seasons. |
| [Tournament](Tournament.md) | A competition pinned to a season, group, or stage. |
| [UniqueStage](UniqueStage.md) | A stage within a competition, such as a motorsport stage. |
| [Event](Event.md) | One match. |

### Participants

| Model | What it represents |
|-------|--------------------|
| [Team](Team.md) | A club or national team. |
| [Subteam](Subteam.md) | An affiliated side: doubles, relay, reserve. |
| [Player](Player.md) | One person: profile, physical data, market value, contract. |
| [PlayerCharacteristics](PlayerCharacteristics.md) | Strengths, weaknesses, and the characteristic type codes. |
| [Transfer](Transfer.md) | A move between teams: fee, type, dates. |

### Match detail

| Model | What it represents |
|-------|--------------------|
| [Incidents](Incidents.md) | Timeline rows: goals, cards, substitutions, periods. |
| [EventStatistics](EventStatistics.md) | Container of per-period statistics. |
| [EventStatisticsPeriod](EventStatisticsPeriod.md) | Statistics for one period. |
| [EventStatisticsGroup](EventStatisticsGroup.md) | A named group inside a period. |
| [EventStatisticsItem](EventStatisticsItem.md) | One stat row. |

### Sport-specific

| Model | Sport | What it represents |
|-------|-------|--------------------|
| [Inning](Inning.md) | Cricket | One innings. |
| [Batsman](Batsman.md) | Cricket | One batting line. |
| [AmericanFootballDownDistance](AmericanFootballDownDistance.md) | American football | Down, distance, yard line, possession. |
| [EsportsGameStatistics](EsportsGameStatistics.md) | Esports | Per-team map stats. |
| [EsportsGameStatisticsResponse](EsportsGameStatisticsResponse.md) | Esports | Home and away game statistics. |
