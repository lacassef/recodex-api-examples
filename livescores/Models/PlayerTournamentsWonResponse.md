# PlayerTournamentsWonResponse

Titles for one player, grouped by table type and then by year.

**Where you'll see it:** `/players/{playerId}/tournaments-won`.

### Example

```json
{
  "playerId": "UkhgIFEq",
  "slug": "alcaraz-garfia-carlos",
  "path": "player/alcaraz-garfia-carlos/UkhgIFEq",
  "tables": [
    {
      "type": "singles",
      "years": [
        {
          "year": "2025",
          "wins": [
            {
              "tournament": "Tournament",
              "url": "tennis/tournament",
              "country": "Country",
              "surface": "Hard",
              "prizeMoney": ""
            }
          ]
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

- **tables** (`array of TournamentWinTable`):
    - One table per type.

- **tables[].type** (`string`):
    - The table type.

- **tables[].years** (`array of TournamentWinYear`):
    - Years that have at least one win in this table.

- **years[].year** (`string`):
    - The year label.

- **years[].wins** (`array of TournamentWinEntry`):
    - The titles in that year.

- **wins[].tournament** (`string`):
    - The tournament name.

- **wins[].url** (`string`):
    - The tournament path.

- **wins[].country** (`string`):
    - The country label.

- **wins[].surface** (`string`):
    - The surface label.

- **wins[].prizeMoney** (`string`):
    - The prize cell, when present.
