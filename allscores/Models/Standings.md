# Standings

**Standings** is the table for one competition season and stage.

**Where you'll see it:** `standings` on the competition standings route.

**Related models:** [Competition](Competition.md). Send `currentSeasonNum` as `seasonNum` and `currentStageNum` as `stageNum`. `type` on this route is the table layout. Example values are `1` and `6`.

This page names the keys on `standings`. It does not name the keys inside a group, a column, or a row.

## Properties

- **displayName** (`string`):
    - Title of the table.

- **groups** (`array`):
    - Groups in the table.

- **columns** (`array`):
    - Column definitions.

- **rows** (`array`):
    - The rows.

- **destinations** (`array`):
    - Destinations for the rows. The description does not list item keys.

- **filterTypes** (`array`):
    - Filters for the table.

- **competitionRules** (`value`):
    - Rules text or object for the competition. The description does not pick a JSON type.
