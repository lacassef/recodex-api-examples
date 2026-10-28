# Tournaments

Filled calls are in [Examples](../guides/examples.md). The order of calls is in [Workflows](../guides/workflows.md).

## Where the ids come from

- `sections[].categories[].id` on `/sports/{sportId}/categories` is `categoryId`.
- `tournament_template_id` on the category tournament list is `templateId`.
- `/tournaments/resolve` returns `tournamentId`, `stageId`, and `templateId`.
- A match list also has `tournament_id` and `sharedindexes_tournament_stage_id`.

## Matches, fixtures, and results

GET `/api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/matches`

- `sportId`, `categoryId`, `templateId` (path, required)
- `lang` (query, omit for `en`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/fixtures`

- `sportId`, `categoryId`, `templateId` (path, required)
- `round` (query, required)
- `page` (query, omit for `1`)
- `lang` (query, omit for `en`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{sportId}/{categoryId}/{templateId}/results`

- `sportId`, `categoryId`, `templateId` (path, required)
- `segment` (query, omit for `1`)
- `projectId` (query, omit for `2`)
- `lang` (query, omit for `en`)
- `page` (query, omit for `1`)
- `group` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

`categoryId` on these routes is the sport category.

## By tournament and stage

GET `/api/livescores/tournaments/{tournamentId}/tables/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{tournamentId}/top-scorers/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{tournamentId}/overview/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `tab` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{tournamentId}/list/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{tournamentId}/draw/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `groupId` (query, when you want one group)
- `version` (query, omit for `2`)

Response: `FeedResponse`

GET `/api/livescores/tournaments/{tournamentId}/seasons/{stageId}`

- `tournamentId`, `stageId` (path, required)
- `projectId` (query, omit for `2`)

Response: `JSONResult`

## Resolve and archive

GET `/api/livescores/tournaments/resolve`

Send `path`, or send `sport`, `country`, and `slug` together. `path` has no host, for example `football/england/premier-league`.

Response: `TournamentResolveResponse`

GET `/api/livescores/tournaments/archive`

The same parameters as resolve.

Response: `TournamentArchiveResponse`

## Season calendar

GET `/api/livescores/sports/{sportId}/season-calendar`

- `sportId` (path, required)
- `projectId` (query, omit for `2`)

Response: `JSONResult`
