# Lineup

A **Lineup** is the players on the pitch for one game.

**Where you'll see it:** the game-lineups route.

**Related models:** [Athlete](Athlete.md), [GameStats](GameStats.md). `gameId` `4669892` is the game in the [examples](../guides/examples.md).

`members` includes status, position, formation, jersey, ranking, and per-player stats. This page lists those single-word keys. It does not name a key for the per-player stats. `chartEvents` lists shots and other plotted events. Item keys inside `chartEvents` are not named here. Athlete chart events use the same key on [Athlete](Athlete.md).

## Properties

- **members** (`array`):
    - Players in the lineup.

- **members[].status** (`value`):
    - Status of that player.

- **members[].position** (`value`):
    - Position.

- **members[].formation** (`value`):
    - Formation.

- **members[].jersey** (`value`):
    - Jersey.

- **members[].ranking** (`value`):
    - Ranking.

- **chartEvents** (`array`):
    - Shots and other plotted events.
