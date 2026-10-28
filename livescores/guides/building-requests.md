# Building a request

Every route is `GET /api/livescores/...`. There is no body.

Filled calls are in [Examples](examples.md). The order of calls is in [Workflows](workflows.md).

## Steps

1. Open the operation in the [OpenAPI](../openapi/livescoresapi_openapi.yaml) or in the [map](../README.md).
2. Copy that operation's parameter names. Do not invent a name and do not reuse another route's query.
3. Fill in the required ones. An optional parameter goes in only when you want that value.
4. Take the value shape from [Parameters](request-essentials.md).
5. Omit `version`, `lang`, and `projectId` when `2`, `en`, and `2` are the values you want.

## Choosing the id

`sportId` comes from the [sport list](../reference/sport-ids.md). `1` is soccer.

`eventId` comes from `records[].fields.sharedindexes_event_id` on a scoreboard, a tournament match list, or a participant match list.

`categoryId` on a tournament or participant route comes from `/sports/{sportId}/categories`, in `sections[].categories[].id`.

`templateId` comes from `tournament_template_id` on a tournament list, or from `templateId` on `/tournaments/resolve`.

`tournamentId` and `stageId` come from `/tournaments/resolve`, or from `tournament_id` and `sharedindexes_tournament_stage_id` on a match list.

`rankingId` comes from `/rankings/resolve` or from `/rankings/{sport}/{slug}/id`.

`participantId` and `playerId` come from search or from the match you already opened. A team page path is `team/{slug}/{participantId}`. A player page path is `player/{slug}/{playerId}`.

## One form of the page path

Send `path`, or send the slug parts. Do not send both a path and a different slug.

Tournament resolve and archive: `path=football/england/premier-league`, or `sport`, `country`, and `slug` together.

Ranking resolve: `path=tennis/rankings/atp`, or `sport` and `slug`.

Squad: `path=team/liverpool/lId4TMwf`, or `slug` when you omit `path`. The player tables use `player/{slug}/{playerId}`.

Sport categories take `path` only when you need to override the sport page, such as `motorsport/auto-racing`. Otherwise omit it.

## News

On `/news`, `sectionId` is the section. `categoryId` on that route is the same section id when `sectionId` is omitted. On other routes, `categoryId` is the sport category.

## Match updates

Lineup changes, missing-player changes, momentum stats, and player-statistics detail take `providerId`. Read it from the snapshot for that block, then send it on the update route. The snapshot routes are in [Matches](../matches/overview.md).

## Odds

`/sports/{sportId}/odds` is the odds list for a day. `/matches/{eventId}/odds-detail` is one match. `/odds` is a persisted query: send `_hash` and the parameters that hash requires. Omit `geoIpCode` and `geoIpSubdivisionCode` to use the default region. The hashes are in [Persisted queries](../graphql/overview.md).

## Feed by name

`/feed/{version}/{feed}` takes the feed name in the path. Patterns are in [Feed names](../feeds/feed-patterns.md). When a named route exists, call that route.
