# History

**History** is the past-winners table for a competition.

**Where you'll see it:** `table` on the competition history route.

**Related models:** [Competition](Competition.md), [Competitor](Competitor.md). The body also includes the competitors the rows name.

A competition without a team-of-the-week selection is a different route. That one returns an empty object and HTTP `200`. It is not this table.

## Properties

- **title** (`string`):
    - Table title.

- **rows** (`array`):
    - Winner rows. This page does not name the keys inside a row.

- **rowEntityType** (`value`):
    - Kind of entity a row names.

- **isChampionByKnockout** (`boolean`):
    - Whether the champion came from the knockout.
