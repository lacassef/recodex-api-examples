# HeadToHead

**HeadToHead** is the previous meetings for one game.

**Where you'll see it:** the h2h route. Select the fixture with `gameId` or with `matchupId` as `homeId-awayId-competitionId`. `4669892` and `1266-1773-116` are those two values in the [examples](../guides/examples.md).

**Related models:** [Competitor](Competitor.md), [ScoresList](ScoresList.md).

## Properties

- **game.h2hGames** (`array`):
    - Previous meetings. The key path is `h2hGames` on `game`.

- **recentGames** (`array`):
    - Recent matches on the home and away competitors.
