# Competition

A **Competition** is one league, cup, or tournament.

**Where you'll see it:** featured competitions, top competitions, competition details, and `competitions` on a [ScoresList](ScoresList.md) or a [Search](Search.md).

**Related models:** [Standings](Standings.md), [Bracket](Bracket.md), [History](History.md), [SeasonStats](SeasonStats.md), [Country](Country.md), [Sport](Sport.md).

`id` is `competition` on details, standings, brackets, stats, trends, and best odds. Athlete games and trophy stats call it `competitionId`. A comma-separated list is `competitions`. `currentSeasonNum` is `seasonNum`. `currentStageNum` is `stageNum`.

Featured and top lists name `popularityRank` and, on the top list, `color`. Details name `colors` and add `seasons` when `withSeasons` is set. This page lists both keys. A response includes the ones that route returns.

### Example

`5930` is the competition id in the [examples](../guides/examples.md). `54` is the country id paired with it there. `1` is football.

```json
{
  "id": 5930,
  "countryId": 54,
  "sportId": 1,
  "hasStandings": true,
  "hasBrackets": true,
  "hasStats": true,
  "hasTransfers": true,
  "hasBets": true
}
```

## Properties

- **id** (`number`):
    - Competition id.

- **name** (`string`):
    - Display name.

- **countryId** (`number`):
    - Country of the competition. On a competition image this is the fallback flag.

- **sportId** (`number`):
    - Sport id.

- **currentSeasonNum** (`number`):
    - Season to send as `seasonNum`.

- **currentStageNum** (`number`):
    - Stage to send as `stageNum`.

- **popularityRank** (`number`):
    - Rank on featured and top lists.

- **color** (`value`):
    - Color on the top-competitions list. The description does not pick a JSON type.

- **colors** (`value`):
    - Colors on competition details.

- **hasStandings** (`boolean`):
    - The competition has a table.

- **hasBrackets** (`boolean`):
    - The competition has a draw.

- **hasStats** (`boolean`):
    - The competition has season stats.

- **hasTransfers** (`boolean`):
    - The competition has transfers.

- **hasBets** (`boolean`):
    - The competition has bets.

- **seasons** (`array`):
    - Present when the request sets `withSeasons`. This page does not name the keys inside a season.
