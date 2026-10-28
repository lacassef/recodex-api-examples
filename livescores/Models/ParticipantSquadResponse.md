# ParticipantSquadResponse

The squad sheet for one participant. Sections group the rows. A row can carry a player and a map of cell text.

**Where you'll see it:** `/participants/{participantId}/squad`.

### Example

```json
{
  "participantId": "lId4TMwf",
  "slug": "liverpool",
  "path": "team/liverpool/lId4TMwf",
  "sections": [
    {
      "name": "Goalkeepers",
      "rows": [
        {
          "cells": { "jersey": "1" },
          "player": {
            "name": "Player",
            "id": "player-id",
            "url": "player/player/player-id",
            "country": "Country",
            "flagId": "21",
            "absence": ""
          }
        }
      ]
    }
  ]
}
```

`lId4TMwf` is the participant id from the [examples](../guides/examples.md). Cell keys depend on the table.

## Properties

- **participantId** (`string`):
    - The participant id.

- **slug** (`string`):
    - The slug, when present.

- **path** (`string`):
    - The team path, `team/{slug}/{participantId}`.

- **sections** (`array of SquadSection`):
    - Groups such as a position.

- **sections[].name** (`string`):
    - The section label.

- **sections[].rows** (`array of SquadRow`):
    - The players in that section.

- **rows[].cells** (`object`):
    - String keys to string values. The columns of that table.

- **rows[].player** (`SquadPlayer`):
    - The player on that row, when the row has one.

- **player.name** (`string`):
    - The player's name.

- **player.id** (`string`):
    - The player id.

- **player.url** (`string`):
    - The player path.

- **player.country** (`string`):
    - The country label.

- **player.flagId** (`string`):
    - The flag id.

- **player.absence** (`string`):
    - An absence note, when the row has one.
