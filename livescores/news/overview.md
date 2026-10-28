# News

Filled calls are in [Examples](../guides/examples.md).

## News list

GET `/api/livescores/news`

Parameters:

- `sportId` (query, required)
- `sectionId` (query). The news section id.
- `categoryId` (query). The same section id when `sectionId` is omitted.
- `version` (query, omit for `2`)

Send `sectionId` or `categoryId`. This `categoryId` is not the sport category used by tournaments.

Response: `FeedResponse`

Read the article id from the list, then call the article route.

## News article

GET `/api/livescores/news/articles/{articleId}`

Parameters:

- `articleId` (path, required)

Response: `JSONResult`

## Entity news

GET `/api/livescores/news/entities/{entityTypeId}/{entityId}`

News for a team, a tournament, or a player.

Parameters:

- `entityTypeId` (path, required)
- `entityId` (path, required)
- `layoutTypeId` (query, omit for `2`)
- `page` (query, omit for `1`)
- `perPage` (query, omit for `10`)
- `projectId` (query, omit for `2`)

Response: `JSONResult`
