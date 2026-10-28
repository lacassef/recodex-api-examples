# FAQ

Parameter names and required flags are in the [OpenAPI](../openapi/allscores_openapi.yaml). Sequences of calls are in [Workflows](workflows.md).

## Where do the parameters come from?

From the operation you are calling. Send only names that operation lists. `sport`, `sportId`, and `sportType` are three names for the sport number. `competitorId`, `competitor`, `competitors`, and `competitorIds` are four names. The map is in [Parameters](request-essentials.md).

## Are there POST routes?

No. Every route is `GET /api/allscores/...`.

## What does 204 mean?

The spec lists `204` when the route exists and there is no data for those parameters. The body is empty.

Some routes still return `200` with an empty object or an empty list. Outrights with no market return an empty object. Team of the week with no selection returns an empty object. A teaser or a raffle can return `bookmakers` empty. A suggestions call that only sends `sport` can return an empty list. A trends call for a quiet date can return only `lastUpdateId` and `ttl`.

## The 400 does not name the bad field

A `400` has `title: Bad Request` and a `request_id`. It does not name the parameter. Check the name and the value in the OpenAPI. The error body is `{"error":{"status","title","request_id"}}`.

## Which type do I send?

On featured competitions and competition details, `type` is empty, `stats`, or `standings`. On competition standings, `type` is the table layout. Example values are `1` and `6`.

## Do I send showOdds=false?

Omit `showOdds` when you do not want odds. Send it when you want odds on a route that lists `showOdds`. `/games-scores` does not take `showOdds`.

## What is matchupId?

`homeId-awayId-competitionId`. Use it on game details and head to head when you do not have `gameId`. Games-top, the slider, suggestions, and contextual predictions also accept `matchupId`.

## Does paging take langId?

No. Send `paging` from `paging.nextPage` or `paging.previousPage`. The cursor already carries the list. You can still send `publisherId`, `campaign`, and `userCountryId` on that request.

## Why are there two competition parameters on athlete details?

The operation lists `competitionId` and `competition`. Send the one you are using. `competitionId` is the one to use for a player profile.
