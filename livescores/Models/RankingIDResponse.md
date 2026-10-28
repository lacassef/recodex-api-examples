# RankingIDResponse

The id that opens a ranking table. Call `/rankings/{rankingId}` with `rankingId`.

**Where you'll see it:** `/rankings/resolve` and `/rankings/{sport}/{slug}/id`.

### Example

```json
{
  "path": "tennis/rankings/atp",
  "rankingId": "4KeVObqb",
  "sport": "tennis",
  "slug": "atp",
  "feeds": {}
}
```

`4KeVObqb` belongs to the [examples](../guides/examples.md). `feeds` is a map of string to string when the response includes it.

## Properties

- **path** (`string`):
    - The path that resolved.

- **rankingId** (`string`):
    - The id for `/rankings/{rankingId}`.

- **sport** (`string`):
    - The sport slug, when present.

- **slug** (`string`):
    - The ranking slug, when present.

- **feeds** (`object`):
    - String keys to string values, when present.
