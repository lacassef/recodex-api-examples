# Workflows

A workflow is the order of calls and what you carry from one response into the next request. Each call is `GET /api/livescores/...`. Take the parameter names from that operation in the [OpenAPI](../openapi/livescoresapi_openapi.yaml). Value shape is in [Parameters](request-essentials.md). Filled requests are in [Examples](examples.md).

Send only the parameters that step needs. Omit a value you are not changing.

## Scoreboard, then a match

1. Pick `sportId` from the [sport list](../reference/sport-ids.md).
2. Call `/sports/{sportId}/scoreboard`. Put the day in `dayOffset`. Omit it for today. Omit `lang` and `version` when you want `en` and `2`.
3. Read `records[].fields.sharedindexes_event_id`. That value is `eventId`.
4. Call the match route for the block you are rendering. Put `eventId` in the path. The routes are in [Matches](../matches/overview.md).

Keep `sharedindexes_sport_id`, `tournament_id`, `sharedindexes_tournament_stage_id`, and `tournament_template_id` when the next page is a tournament or a participant.

## Match page

You already have `eventId`. Pick the block. Do not call every match route up front.

1. Stats, commentary, commentary only, point by point, head to head, news, report, odds detail, top scorers, detail config, box score, and box-score names are feed routes. Omit `version` to use `2`.
2. The live table is `/matches/{eventId}/timeline`. The tournament table tab is `/matches/{eventId}/overview`, with `tab` when you want a tab other than `1`.
3. The vertical summary is `/matches/{eventId}/tv/long`. The horizontal summary is `/matches/{eventId}/tv/short`.
4. The current tennis game is `/matches/{eventId}/highlights`. Highlight videos are `/matches/{eventId}/highlights/videos`.
5. Lineups: `/matches/{eventId}/lineups`. Omit `projectId` to use `2`. Read `providerId` from that response.
6. Lineup changes: `/matches/{eventId}/lineups/updates`. Put that `providerId` in the query.
7. Missing players, momentum, and player statistics use the same two steps. The snapshot is the route without `updates`. The next call is the update route, with `providerId` from the snapshot. Momentum updates take only `eventId`. Player-statistics detail takes `providerId` from the player-statistics snapshot.
8. The summary odds form is `/matches/{eventId}/stage`.
9. News layout is `/matches/{eventId}/news-layout`. Omit `layoutTypeId` and `projectId` to use `2` and `2`.
10. The HTML report is `/matches/{eventId}/report/html`. The body is HTML.

A `204` means that match has no data for that route. Do not repeat the same request.

A participant row inside one event is `/matches/{eventId}/participants/{participantId}/detail`. `participantId` comes from that match.

## Tournament

1. Call `/sports/{sportId}/categories`. Send `path` only when the sport page is not the usual one, such as `motorsport/auto-racing`.
2. Read `sections[].categories[].id`. Call `/sports/{sportId}/categories/{categoryId}/tournaments`. Omit `flag` to use `y`.
3. Read `tournament_template_id`. That is `templateId` for matches, fixtures, and results.
4. Matches: `/tournaments/{sportId}/{categoryId}/{templateId}/matches`.
5. Fixtures need `round` as well: `/tournaments/{sportId}/{categoryId}/{templateId}/fixtures`.
6. Results: `/tournaments/{sportId}/{categoryId}/{templateId}/results`. Omit `segment`, `page`, and `group` to use `1`, `1`, and `1`.
7. Call `/tournaments/resolve` with `path`, or with `sport`, `country`, and `slug` together. Read `tournamentId`, `stageId`, and `templateId`.
8. Tables, overview, list, draw, top scorers, and seasons take `tournamentId` and `stageId`. Draw takes `groupId` when you want one group. Overview takes `tab`.
9. Archive uses the same path form as resolve, on `/tournaments/archive`.
10. The season calendar for a sport is `/sports/{sportId}/season-calendar`.

If you already have a match, `tournament_id` and `sharedindexes_tournament_stage_id` are `tournamentId` and `stageId`. You can skip resolve.

## Team

1. Take `participantId` from search or from the match.
2. Call `/participants/{participantId}/matches`. This route also requires `sportId` and `categoryId` in the query. `categoryId` here is the sport category.
3. Squad: send `path` as `team/{slug}/{participantId}`, or send `slug` and omit `path`. The id in `path` has to be that `participantId`.
4. News, transfers, and events use the participant id. Transfers take `tab` and `page`. Events take `projectTypeId`. Omit it to use `1`.
5. One event for that participant is `/participants/{participantId}/events/{eventId}/detail`.
6. Recent matches as JSON are `/participants/{participantId}/last-matches`. Omit `scope` to use `1`.

## Player

1. Call `/players/{playerId}/profile`. Omit `projectId` to use `2`.
2. Match record, tournaments won, and injuries need `path` or `slug`. `path` is `player/{slug}/{playerId}`. The id in the path has to be that `playerId`.

## Rankings

1. Call `/rankings/resolve` with `path`, or with `sport` and `slug`. The path form is `{sport}/rankings/{slug}`. `/rankings/{sport}/{slug}/id` is the same resolution with those values in the path.
2. Read `rankingId`.
3. Call `/rankings/{rankingId}`. `variant` is `ran` or `ral`. Omit it to use `ran`. Omit `tab` to use `1`.

## News, then the article

1. Call `/news` with `sportId` and `sectionId`. If you omit `sectionId`, send the same section id in `categoryId`.
2. Read the article id from that list. Call `/news/articles/{articleId}`.
3. News for a team, a tournament, or a player is `/news/entities/{entityTypeId}/{entityId}`. Omit `page` and `perPage` for the first page of `10`. Send `page` when you need the next page.

`categoryId` on this list is the news section. It is not the sport category used by tournaments.

## Search, then open the result

1. Call `/search` with the text in `q`.
2. A team result continues at [Team](#team) with `participantId`. A player result continues at [Player](#player) with `playerId`. A tournament result continues at [Tournament](#tournament) with the path or the ids the result gives you.
3. `/top-search` has no parameters. It is the suggestion list, not a query.

## Odds

1. The day list is `/sports/{sportId}/odds`, with the same `dayOffset` as the scoreboard.
2. One match is `/matches/{eventId}/odds-detail`, using `eventId` from the scoreboard.
3. A persisted odds query is `/odds`. Put the hash in `_hash` and the parameters that hash requires. Omit `geoIpCode` and `geoIpSubdivisionCode` to use the default region. Hashes are in [Persisted queries](../graphql/overview.md).

The summary odds form on a match page is `/matches/{eventId}/stage`, not `/odds`.

## Refresh

1. `/sports/{sportId}/refresh` is the light scoreboard update for that sport.
2. `/updates` takes `sportId`. Omit `scope` to use `1`.
3. `/updates/list` takes `sportId`. Omit `projectId` to use `2`. This route does not take `scope`.
4. `/updates/counts` is the count feed. Omit `projectId` to use `2`.
5. `/matches/{eventId}/hashes` is the hash feed for one match, before you repeat a detail call.
6. `/system/status` takes `scope`. Omit it to use `1`.

Read `Cache-Control` on the response before you repeat the same URL.
