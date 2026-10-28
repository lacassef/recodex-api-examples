# Rankings

Filled calls are in [Examples](../guides/examples.md).

## Resolve

GET `/api/livescores/rankings/resolve`

Send `path`, or send `sport` and `slug`. `path` has no host. The form is `{sport}/rankings/{slug}`, for example `tennis/rankings/atp`.

Response: `RankingIDResponse`

Read `rankingId`.

## Resolve by slug

GET `/api/livescores/rankings/{sport}/{slug}/id`

Parameters:

- `sport` (path, required)
- `slug` (path, required)

Response: `RankingIDResponse`

## Table

GET `/api/livescores/rankings/{rankingId}`

Parameters:

- `rankingId` (path, required)
- `tab` (query, omit for `1`)
- `variant` (query, `ran` or `ral`, omit for `ran`)
- `version` (query, omit for `2`)

Response: `FeedResponse`
