# PlayerMatchRecordResponse

Season rows for one player. Each table has a `type` and a list of records. Surface columns are strings.

**Where you'll see it:** `/players/{playerId}/match-record`.

### Example

```json
{
  "playerId": "UkhgIFEq",
  "slug": "alcaraz-garfia-carlos",
  "path": "player/alcaraz-garfia-carlos/UkhgIFEq",
  "tables": [
    {
      "type": "singles",
      "records": [
        {
          "season": "2025",
          "rank": "1",
          "titles": "2",
          "allMatches": "10",
          "hard": "4",
          "clay": "3",
          "grass": "3"
        }
      ]
    }
  ]
}
```

## Properties

- **playerId** (`string`):
    - The player id.

- **slug** (`string`):
    - The slug, when present.

- **path** (`string`):
    - `player/{slug}/{playerId}`.

- **tables** (`array of PlayerMatchRecordTable`):
    - One table per type.

- **tables[].type** (`string`):
    - The table type.

- **tables[].records** (`array of PlayerMatchRecord`):
    - The season rows.

- **records[].season** (`string`):
    - The season label.

- **records[].rank** (`string`):
    - The rank cell.

- **records[].titles** (`string`):
    - The titles cell.

- **records[].allMatches** (`string`):
    - Matches across surfaces.

- **records[].hard** (`string`), **records[].clay** (`string`), **records[].grass** (`string`):
    - Surface cells.
