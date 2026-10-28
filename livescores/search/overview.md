# Search

Filled calls are in [Examples](../guides/examples.md). What to open next is in [Workflows](../guides/workflows.md).

## Search

GET `/api/livescores/search`

Parameters:

- `q` (query, required)

Response: `JSONResult`

A team result continues with `participantId`. A player result continues with `playerId`. A tournament result continues with the path or the ids in that result.

## Top search

GET `/api/livescores/top-search`

No parameters.

Response: `JSONResult`
