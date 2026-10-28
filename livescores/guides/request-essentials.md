# Parameters

Each parameter name is the one in the [OpenAPI](../openapi/livescoresapi_openapi.yaml). Send only the ones the operation lists. Required, type, and example are in the spec.

## Value shape

`sportId`, `countryId`, `categoryId` on a category or participant route, `sectionId`, `round`, `segment`, `page`, `perPage`, `tab`, `scope`, `projectId`, `projectTypeId`, `layoutTypeId`, `entityTypeId`, and `dayOffset` are integers when the operation types them as integers.

`group` on tournament results is a token. Omit it to use `1`. `flag` is `y` or `n`. Omit it to use `y`. `variant` on a ranking is `ran` or `ral`. Omit it to use `ran`.

`eventId`, `participantId`, `playerId`, `templateId`, `tournamentId`, `stageId`, `rankingId`, `articleId`, `entityId`, `providerId`, `req`, and `feed` are strings. A path id uses letters and digits.

`lang` is a short token, such as `en`. Omit it to use `en`. `version` is an integer. Omit it to use `2`.

Omit `projectId` to use `2`. Omit `layoutTypeId` to use `2`. Omit `page` to use `1`. Omit `perPage` to use `10`. Omit `tab` to use `1`. Omit `projectTypeId` to use `1`.

`scope` depends on the operation. Omit it on featured to use `0`. Omit it on updates, last matches, and system status to use `1`.

`dayOffset` is a day relative to today. Omit it to use `0`, which is today. A negative value is an earlier day. A positive value is a later day.

`path` has no host and no leading slash.

- Tournament: `football/england/premier-league`.
- Team: `team/{slug}/{participantId}`.
- Player: `player/{slug}/{playerId}`.
- Ranking: `tennis/rankings/atp`.
- Sport category override: `motorsport/auto-racing`.

The id at the end of a team or player path is the same id as the path parameter.

## What you can omit

| Parameter | Used when omitted |
| --- | --- |
| `version` | `2` |
| `lang` | `en` |
| `projectId` | `2` |
| `projectTypeId` | `1` |
| `layoutTypeId` | `2` |
| `page` | `1` |
| `perPage` | `10` |
| `tab` | `1` |
| `dayOffset` | `0` |
| `flag` | `y` |
| `variant` | `ran` |
| `segment` | `1` |
| `group` on results | `1` |

Send a parameter when you want a different value.

## News section and sport category

On `/news`, send `sectionId`. `categoryId` on that route is the same section id when `sectionId` is omitted. Send one of the two.

On category, tournament, and participant-match routes, `categoryId` is the sport category id. It is not a news section.

## Odds region

On `/odds`, omit `geoIpCode` and `geoIpSubdivisionCode` to use the default region. Send them when you want a region.

## Page paths

Squad needs `path`, or `slug` when `path` is omitted. The player match record, titles, and injuries routes are the same, with a player path.

Tournament resolve and archive need `path`, or `sport`, `country`, and `slug` together.

Ranking resolve needs `path`, or `sport` and `slug`. `/rankings/{sport}/{slug}/id` takes those two in the path.

## Responses

Feed routes return `FeedResponse`: `version`, `feed`, `header`, and `records`. Each record has `fields`. A field value is a string or an array of strings. Known field names are decoded. Unknown codes stay as they are. A feed that is already JSON is returned as that JSON.

`sharedindexes_event_id` in `records[].fields` is the `eventId` for match routes. `tournament_template_id` is `templateId`. `tournament_id` and `sharedindexes_tournament_stage_id` are `tournamentId` and `stageId`.

Navigation with a `req` that starts with `m_` returns `ReqResponse`. Any other `req` is returned as received.

The other objects are in [Schemas](../reference/schemas.md). `JSONResult` is the JSON body of that route.

## Content types

- `application/json` for most routes.
- `text/html` for `/matches/{eventId}/report/html`.
- `image/png` for `/images/static/{path}`.
- `image/avif` for `/images/ott/{path}`.

`{path}` on an image route can contain slashes. It is the rest of the path.

## Errors

`400` is an invalid parameter. The body is `{"error":{"status","title","request_id"}}`. `title` is `Bad Request`. The field name is not in the JSON. Check the name and the value in the OpenAPI.

An empty `204` means the route exists and there is no data for those parameters. The body is empty.

`502`, `503`, and `504` mean the response could not be obtained. The body is the same error object.
