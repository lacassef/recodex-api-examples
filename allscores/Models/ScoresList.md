# ScoresList

A **ScoresList** is the body of a games route: the rows, the catalogs that label them, and the polling fields. `games` holds the rows. This page does not name the property inside a row that stores the game id. Read that id from `games` and send it as the next route asks.

**Where you'll see it:** games-scores, games-top, the slider, fixtures, results, custom scores, and the other list routes that return games. Suggestions put `suggestedGames` on the body. Contextual predictions can put `promotedPredictions` and `playersBetsPredictions` on each game.

**Related models:** [Sport](Sport.md), [Country](Country.md), [Competition](Competition.md), [Competitor](Competitor.md), [Paging](Paging.md).

Descriptions name status, start time, clock, venue, officials, stage scores, events, lineups, top performers, members, lineup flags, and home and away scores on a row. Those words are not confirmed JSON keys here. Odds are present when the route accepts `showOdds` and you set it.

A competitor with no highlight clips still returns `lastUpdateId` and `ttl`.

### Example (envelope)

`1` is the football sport id from the [sport list](../reference/sport-ids.md). The arrays are empty on purpose. This is not a captured payload.

```json
{
  "sports": [{ "id": 1 }],
  "countries": [],
  "competitions": [],
  "competitors": [],
  "games": [],
  "bookmakers": [],
  "summary": {},
  "paging": {
    "nextPage": "",
    "previousPage": ""
  }
}
```

## Properties

- **games** (`array`):
    - The rows. Read the game id from each row.

- **suggestedGames** (`array`):
    - Rows on the suggestions route when you send competitions and competitors.

- **summary** (`object`):
    - The summary that list routes return with the rows.

- **sports** (`array of Sport`):
    - Sports referenced by the rows.

- **countries** (`array of Country`):
    - Countries referenced by the rows.

- **competitions** (`array of Competition`):
    - Competitions referenced by the rows.

- **competitors** (`array of Competitor`):
    - Competitors referenced by the rows.

- **bookmakers** (`array`):
    - Bookmakers referenced by the rows. The array can be empty on a `200`.

- **competitionFilters** (`array`):
    - Filters on fixtures and results.

- **paging** (`Paging`):
    - Cursors on fixtures and results. See [Paging](Paging.md).

- **lastUpdateId** (`number`):
    - Polling cursor. Send it on the next call. Omit it on that call for a full response.

- **requestedUpdateId** (`number`):
    - The cursor this response was built for.

- **ttl** (`number`):
    - How long this body stays current.

- **promotedPredictions** (`array`):
    - On a game in contextual predictions.

- **playersBetsPredictions** (`array`):
    - On a game in contextual predictions.
