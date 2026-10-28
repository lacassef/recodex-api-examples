# TournamentResolveResponse

Ids for one tournament path. `tournamentId` and `stageId` open tables, the overview, the list, the draw, top scorers, and seasons. `templateId` opens matches, fixtures, and results.

**Where you'll see it:** `/tournaments/resolve`.

**Related models:** [TournamentArchiveResponse](TournamentArchiveResponse.md). The same `tournamentId` and `stageId` also appear on a match list as `tournament_id` and `sharedindexes_tournament_stage_id`.

### Example

```json
{
  "path": "football/england/premier-league",
  "templateId": "COuk57Ci",
  "sportId": 1,
  "tournamentId": "tournament-id",
  "stageId": "stage-id",
  "seasons": [
    { "id": "season-id", "name": "2025/2026", "path": "football/england/premier-league" }
  ]
}
```

`COuk57Ci` is the template id from the [examples](../guides/examples.md), for category `98`. `tournamentId` and `stageId` are the other two ids this object returns. The path form is `{sport}/{country}/{slug}`.

## Properties

- **path** (`string`):
    - The path you resolved.

- **tournamentId** (`string`):
    - The tournament id.

- **stageId** (`string`):
    - The stage id.

- **templateId** (`string`):
    - The template id.

- **sportId** (`number`):
    - The sport id.

- **selectedSeasonId** (`string`):
    - The season selected for this path.

- **seasons** (`array of TournamentSeason`):
    - Seasons on this competition.

- **seasons[].id** (`string`):
    - The season id.

- **seasons[].name** (`string`):
    - The season label.

- **seasons[].path** (`string`):
    - The path for that season.
