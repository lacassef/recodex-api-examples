# GameStats

**GameStats** is the team-statistics body for one or more games.

**Where you'll see it:** the game-stats route. Pre-game comparison is a different route and does not use these keys.

**Related models:** [Lineup](Lineup.md). `4669892` is the game id in the [examples](../guides/examples.md). This route calls it `games`.

`filterId` on the next call is an id from `statisticsFilters`. This page does not name the keys inside that array.

## Properties

- **statistics** (`array`):
    - One entry per stat.

- **statistics[].name** (`string`):
    - Stat name.

- **statistics[].value** (`value`):
    - Stat value.

- **statistics[].valuePercentage** (`value`):
    - The same value as a percentage, when the stat has one.

- **statistics[].competitorId** (`number`):
    - Competitor the stat belongs to.

- **statistics[].isMajor** (`boolean`):
    - Headline stat. `onlyIsMajor` keeps these.

- **statistics[].order** (`number`):
    - Display order.

- **statisticsFilters** (`array`):
    - Tabs. An id from this array is `filterId` on the next stats call.
