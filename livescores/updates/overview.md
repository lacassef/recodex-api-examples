# Updates and system

Filled calls are in [Examples](../guides/examples.md).

## Updates

GET `/api/livescores/updates`

Parameters:

- `sportId` (query, required)
- `scope` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Updates list

GET `/api/livescores/updates/list`

Parameters:

- `sportId` (query, required)
- `projectId` (query, omit for `2`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

This route does not take `scope`.

## Update counts

GET `/api/livescores/updates/counts`

Parameters:

- `projectId` (query, omit for `2`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## System status

GET `/api/livescores/system/status`

Parameters:

- `scope` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`
