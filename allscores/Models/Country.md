# Country

A **Country** is one entry in the country catalog.

**Where you'll see it:** the countries route, and `countries` on list bodies.

**Related models:** [Sport](Sport.md). The body also includes `sports`, `lastUpdateId`, `requestedUpdateId`, and `ttl`.

### Example

`54` is the country id used with competition `5930` in the [examples](../guides/examples.md).

```json
{
  "id": 54
}
```

## Properties

- **id** (`number`):
    - Country id. On a competition image this is the fallback flag.

- **name** (`string`):
    - Display name.

- **nameForURL** (`string`):
    - Name used in a path.

- **imageVersion** (`number`):
    - Version for an image path. The flag route does not use it.

- **sportTypes** (`array`):
    - Sports this country is listed under.

- **totalGames** (`number`):
    - Game count for the request.

- **liveGames** (`number`):
    - Live game count for the request.
