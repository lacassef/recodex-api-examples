# SeasonStats

**SeasonStats** is the leader table for a competition, or one side's table.

**Where you'll see it:** `stats` on the competition season-stats route. Send `competition` for the leader table, or `competitorId` for one side.

**Related models:** [Competition](Competition.md), [Competitor](Competitor.md), [Career](Career.md).

`stats.athletesStats` and `stats.competitorsStats` are tables. This page does not name the column and row keys inside a table.

## Properties

- **stats.athletesStats** (`array`):
    - Athlete tables. The key path is `athletesStats` on `stats`.

- **stats.competitorsStats** (`array`):
    - Competitor tables. The key path is `competitorsStats` on `stats`.

- **seasons** (`array`):
    - Present when the request sets `withSeasons`.
