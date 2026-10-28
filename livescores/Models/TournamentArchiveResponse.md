# TournamentArchiveResponse

Past seasons for a tournament path, and the winner of each season when the row has one.

**Where you'll see it:** `/tournaments/archive`.

**Related models:** [TournamentResolveResponse](TournamentResolveResponse.md).

### Example

```json
{
  "path": "football/england/premier-league",
  "tournamentId": "tournament-id",
  "stageId": "stage-id",
  "seasons": [
    {
      "season": "2024/2025",
      "seasonUrl": "football/england/premier-league-2024-2025",
      "winner": { "name": "Winner", "url": "team/winner/id", "id": "id", "logo": "logo" }
    }
  ]
}
```

## Properties

- **path** (`string`):
    - The archive path.

- **tournamentId** (`string`):
    - The tournament id, when present.

- **stageId** (`string`):
    - The stage id, when present.

- **seasons** (`array of TournamentArchiveSeason`):
    - One entry per past season.

- **seasons[].season** (`string`):
    - The season label.

- **seasons[].seasonUrl** (`string`):
    - The path for that season, when present.

- **seasons[].winner** (`TournamentArchiveWinner`):
    - The winner, when that season has one.

- **winner.name** (`string`):
    - The winner's name.

- **winner.url** (`string`):
    - The winner's path.

- **winner.id** (`string`):
    - The winner's id.

- **winner.logo** (`string`):
    - The winner's logo token.
