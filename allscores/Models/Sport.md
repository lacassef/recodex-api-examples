# Sport

A **Sport** is one entry in the sports catalog.

**Where you'll see it:** `/sports`, and `sports` on list bodies that label their rows.

**Related models:** [Country](Country.md), [ScoresList](ScoresList.md). Ids are in [Sport ids](../reference/sport-ids.md).

`withCount` adds per-sport game counts. This page does not name the key that holds those counts. The catalog body also includes `lastUpdateId`, `requestedUpdateId`, and `ttl`.

### Example

`1` is football.

```json
{
  "id": 1
}
```

## Properties

- **id** (`number`):
    - Sport id. The next call names it `sport`, `sportId`, or `sportType`.

- **name** (`string`):
    - Display name.

- **nameForURL** (`string`):
    - Name used in a path.

- **imageVersion** (`number`):
    - Version to put in an image path. See [Image](Image.md).
