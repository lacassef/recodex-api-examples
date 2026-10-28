# Persisted queries

`/graphql` and `/odds` run a query identified by `_hash`. Send the parameters that hash requires. Those extra names are not a fixed list on the operation, because they depend on the hash.

Prefer the match, news, and tournament routes when one of them already returns that data. Those routes do not take `_hash`. Filled calls are in [Examples](../guides/examples.md).

An unknown `_hash` returns an error from that query. Check the hash and the parameter names.

## GraphQL

GET `/api/livescores/graphql`

- `_hash` (query, required)

| `_hash` | Parameters |
| --- | --- |
| `dlie2` | `eventId`, `projectId` |
| `dmpe2` | `eventId`, `projectId` |
| `dsos2` | `eventId`, `projectId` |
| `epmsd` | `eventId`, `providerId` |
| `epmsdp` | `eventId`, `playerId`, `providerId` |
| `epmsse` | `eventId`, `projectId` |
| `epmsspe` | `eventId`, `projectId`, `playerId` |
| `fsa` | `articleId`, `projectId` |
| `fsned` | `entityId`, `layoutTypeId`, `projectId`. On a match, `entityId` is the event id. |
| `lobtm` | `eventId`, `projectId`. Omit `geoIpCode` and `geoIpSubdivisionCode` for the default region. |

Response: `JSONResult`

## Odds

GET `/api/livescores/odds`

- `_hash` (query, required)

| `_hash` | Parameters |
| --- | --- |
| `oce` | `eventId`, `projectId`. Omit `geoIpCode` and `geoIpSubdivisionCode` for the default region. |
| `ope2` | `eventId`, `bookmakerId`, `betType`, `betScope` |
| `pobtm` | `eventId`, `projectId`. Omit `geoIpCode` and `geoIpSubdivisionCode` for the default region. |

`lwto`, `lwo`, `twto`, and `two` also take the default region when `geoIpCode` and `geoIpSubdivisionCode` are omitted. Send the other parameters that hash requires.

Response: `JSONResult`

Entity news is `/news/entities/{entityTypeId}/{entityId}`, not an odds hash. The article is `/news/articles/{articleId}`.
