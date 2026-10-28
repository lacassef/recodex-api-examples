# Participants

Filled calls are in [Examples](../guides/examples.md). `categoryId` on the match list is the sport category.

## Participant matches

GET `/api/livescores/participants/{participantId}/matches`

Parameters:
- `participantId` (path, required)
- `sportId` (query, required)
- `categoryId` (query, required)
- `lang` (query, omit for `en`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant squad

GET `/api/livescores/participants/{participantId}/squad`

Parameters:
- `participantId` (path, required)
- `path` (query). Team path with no host: `team/{slug}/{participantId}`. The id has to match `participantId`.
- `slug` (query). Send this when `path` is omitted.

Response: `ParticipantSquadResponse`

## Participant news

GET `/api/livescores/participants/{participantId}/news`

Parameters:
- `participantId` (path, required)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant transfers

GET `/api/livescores/participants/{participantId}/transfers`

Parameters:
- `participantId` (path, required)
- `tab` (query, omit for `1`)
- `page` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant events

GET `/api/livescores/participants/{participantId}/events`

Parameters:
- `participantId` (path, required)
- `projectTypeId` (query, omit for `1`)
- `projectId` (query, omit for `2`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant event detail

GET `/api/livescores/participants/{participantId}/events/{eventId}/detail`

Parameters:
- `participantId` (path, required)
- `eventId` (path, required)
- `projectTypeId` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Participant last matches

GET `/api/livescores/participants/{participantId}/last-matches`

Parameters:
- `participantId` (path, required)
- `scope` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `JSONResult`
