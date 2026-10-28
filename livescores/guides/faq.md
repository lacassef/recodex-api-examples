# FAQ

Parameter names and required flags are in the [OpenAPI](../openapi/livescoresapi_openapi.yaml). Sequences of calls are in [Workflows](workflows.md).

## Where do the parameters come from?

From the operation you are calling. Send only names that operation lists. Do not reuse another route's query.

## Are there POST routes?

No. Every route is `GET /api/livescores/...`.

## What does an empty 204 mean?

The route exists and there is no data for those parameters. The body is empty. Do not repeat the same request.

## The 400 does not name the bad field

A `400` has `title: Bad Request` and a `request_id`. It does not name the parameter. Check the name and the value in the OpenAPI.

## What are 502, 503, and 504?

The response could not be obtained. The body is `{"error":{"status","title","request_id"}}`.

## How do I find an event id?

On a scoreboard or a match list, read `records[].fields.sharedindexes_event_id`. Put that value in `{eventId}`.

## Which sportId?

The integers are in [Sport ids](../reference/sport-ids.md). `1` is soccer. `20` and `27` are not in that list.

## Slug, path, or id?

`eventId`, `participantId`, `playerId`, `templateId`, `tournamentId`, `stageId`, and `rankingId` identify the path of the data routes.

`path` is a page path with no host. A team path is `team/{slug}/{participantId}`. A player path is `player/{slug}/{playerId}`. A tournament path is `{sport}/{country}/{slug}`. A ranking path is `{sport}/rankings/{slug}`.

Squad and the player table routes need `path`, or `slug` when `path` is omitted. The id inside `path` has to match the path parameter.

## Which categoryId?

On `/news`, `categoryId` is the news section id, and only when `sectionId` is omitted. Send `sectionId`, or send `categoryId` with that same section id.

On `/sports/{sportId}/categories/{categoryId}/tournaments`, on the tournament match routes, and on `/participants/{participantId}/matches`, `categoryId` is the sport category. Read it from `sections[].categories[].id`.

## Do I send sectionId and categoryId on the news list?

Send one. `sectionId` is the section. `categoryId` is that same id when `sectionId` is omitted.

## What is providerId?

The update routes name the snapshot it comes from. Lineup updates use the lineups response. Missing-player updates use the missing-players response. Momentum stats use the momentum response. Player-statistics detail and updates use the player-statistics response. Omit `providerId` on the snapshot call.

## Which variant?

On `/rankings/{rankingId}`, `ran` or `ral`. Omit it to use `ran`.

## Should I send geoIpCode?

On `/odds`, and on `lobtm`, omit `geoIpCode` and `geoIpSubdivisionCode` to use the default region. `lwto`, `lwo`, `twto`, and `two` follow the same rule. Send the geo parameters when you want a region.

## Should I send version, lang, and projectId?

Omit `version` to use `2`. Omit `lang` to use `en`. Omit `projectId` to use `2`. Send one of them when you want another value.

## Can I call /feed with a feed name?

Yes. The name goes in the path. Patterns are in [Feed names](../feeds/feed-patterns.md). When a named route exists for that data, call the named route.

## Which hash goes on which route?

`/graphql` and `/odds` each require `_hash`. The parameters that hash requires are in [Persisted queries](../graphql/overview.md). Match, news, and tournament routes that already exist do not take `_hash`.

## How do image paths work?

`/images/static/*` returns PNG. `/images/ott/*` returns AVIF. The `*` can contain slashes. It is the rest of the URL path.

## Do I send an account cookie or token?

No.

## Should I repeat the same URL?

Read `Cache-Control` on the response before you repeat it. A `204` will not gain a body by repeating the same parameters.
