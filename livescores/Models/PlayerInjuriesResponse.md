# PlayerInjuriesResponse

Injury rows for one player.

**Where you'll see it:** `/players/{playerId}/injuries`.

### Example

```json
{
  "playerId": "UkhgIFEq",
  "slug": "alcaraz-garfia-carlos",
  "path": "player/alcaraz-garfia-carlos/UkhgIFEq",
  "injuries": [
    { "from": "01.01.", "until": "15.01.", "name": "Knee", "hidden": false }
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

- **injuries** (`array of PlayerInjury`):
    - One row per injury.

- **injuries[].from** (`string`):
    - The start label.

- **injuries[].until** (`string`):
    - The end label.

- **injuries[].name** (`string`):
    - The injury name.

- **injuries[].hidden** (`boolean`):
    - Whether the row is hidden.
