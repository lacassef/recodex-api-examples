# Players

Filled calls are in [Examples](../guides/examples.md). Match record, tournaments won, and injuries need `path` or `slug`.

## Player profile

GET `/api/livescores/players/{playerId}/profile`

Parameters:
- `playerId` (path, required)
- `projectId` (query, omit for `2`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

## Player match record

GET `/api/livescores/players/{playerId}/match-record`

Parameters:
- `playerId` (path, required)
- `path` (query). Player path with no host: `player/{slug}/{playerId}`. The id has to match `playerId`.
- `slug` (query). Send this when `path` is omitted.

Response: `PlayerMatchRecordResponse`

## Player tournaments won

GET `/api/livescores/players/{playerId}/tournaments-won`

Parameters:
- `playerId` (path, required)
- `path` (query). Same shape as the match record.
- `slug` (query). Send this when `path` is omitted.

Response: `PlayerTournamentsWonResponse`

## Player injuries

GET `/api/livescores/players/{playerId}/injuries`

Parameters:
- `playerId` (path, required)
- `path` (query). Same shape as the match record.
- `slug` (query). Send this when `path` is omitted.

Response: `PlayerInjuriesResponse`
