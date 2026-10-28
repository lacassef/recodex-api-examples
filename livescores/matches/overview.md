# Matches

Every match route takes `eventId` in the path. Read it from `records[].fields.sharedindexes_event_id` on a scoreboard or a match list. A match can return `204` for a route that has no data.

Feed routes below return `FeedResponse` and accept `version`. Omit `version` to use `2`. JSON routes return `JSONResult`. Filled calls are in [Examples](../guides/examples.md). Which call comes next is in [Workflows](../guides/workflows.md).

## Feed routes

- GET `/api/livescores/matches/{eventId}/hashes`
- GET `/api/livescores/matches/{eventId}/stats`
- GET `/api/livescores/matches/{eventId}/box-score`
- GET `/api/livescores/matches/{eventId}/box-score/names`
- GET `/api/livescores/matches/{eventId}/timeline` — live table
- GET `/api/livescores/matches/{eventId}/commentary`
- GET `/api/livescores/matches/{eventId}/commentary-only`
- GET `/api/livescores/matches/{eventId}/point-by-point`
- GET `/api/livescores/matches/{eventId}/h2h`
- GET `/api/livescores/matches/{eventId}/news`
- GET `/api/livescores/matches/{eventId}/report`
- GET `/api/livescores/matches/{eventId}/tv/long` — vertical summary
- GET `/api/livescores/matches/{eventId}/tv/short` — horizontal summary
- GET `/api/livescores/matches/{eventId}/odds-detail`
- GET `/api/livescores/matches/{eventId}/highlights` — current tennis game
- GET `/api/livescores/matches/{eventId}/highlights/videos`
- GET `/api/livescores/matches/{eventId}/top-scorers`
- GET `/api/livescores/matches/{eventId}/detail-config`

## Overview

GET `/api/livescores/matches/{eventId}/overview`

The tournament table tab opened from a match.

- `tab` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant row

GET `/api/livescores/matches/{eventId}/participants/{participantId}/detail`

- `eventId` (path, required)
- `participantId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Lineups

GET `/api/livescores/matches/{eventId}/lineups`

- `projectId` (query, omit for `2`)

Response: `JSONResult`

GET `/api/livescores/matches/{eventId}/lineups/updates`

- `projectId` (query, omit for `2`)
- `providerId` (query, from the lineups response)

Response: `JSONResult`

## Missing players

GET `/api/livescores/matches/{eventId}/missing-players`

- `projectId` (query, omit for `2`)

GET `/api/livescores/matches/{eventId}/missing-players/updates`

- `providerId` (query, from the missing-players response)

Response: `JSONResult`

## Momentum

GET `/api/livescores/matches/{eventId}/momentum`

- `projectId` (query, omit for `2`)

GET `/api/livescores/matches/{eventId}/momentum/stats`

- `providerId` (query, from the momentum response)

GET `/api/livescores/matches/{eventId}/momentum/updates`

No query parameters.

Response: `JSONResult`

## Player statistics

GET `/api/livescores/matches/{eventId}/player-statistics`

- `projectId` (query, omit for `2`)

GET `/api/livescores/matches/{eventId}/player-statistics/detail`

- `providerId` (query, from the player-statistics response)

GET `/api/livescores/matches/{eventId}/player-statistics/updates`

- `providerId` (query, from the player-statistics response)

Response: `JSONResult`

## Summary odds form

GET `/api/livescores/matches/{eventId}/stage`

- `projectId` (query, omit for `2`)

Response: `JSONResult`

## News layout

GET `/api/livescores/matches/{eventId}/news-layout`

- `layoutTypeId` (query, omit for `2`)
- `projectId` (query, omit for `2`)

Response: `JSONResult`

## Report HTML

GET `/api/livescores/matches/{eventId}/report/html`

- `version` (query, omit for `2`)

Response: `text/html`
