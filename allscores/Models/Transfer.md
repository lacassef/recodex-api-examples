# Transfer

A **Transfer** is one player move.

**Where you'll see it:** the transfers route. The body also includes the related athletes and competitors.

**Related models:** [Athlete](Athlete.md), [Competitor](Competitor.md).

## Properties

- **id** (`number`):
    - Transfer id.

- **type** (`value`):
    - Kind of move.

- **origin** (`value`):
    - Where the player moved from.

- **target** (`value`):
    - Where the player moved to.

- **time** (`value`):
    - When the move happened.

- **price** (`value`):
    - The fee.

- **athleteId** (`number`):
    - The player.

- **statusName** (`string`):
    - Status label.

- **positionId** (`number`):
    - Position id.

- **isArrival** (`boolean`):
    - The move is an arrival.

- **isDeparture** (`boolean`):
    - The move is a departure.
