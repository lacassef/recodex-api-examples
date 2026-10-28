# Best practices

Send the parameters the operation lists in the OpenAPI. The rest of this page is what to leave out.

## Omit the usual values

Do not send a parameter whose omitted value is already the one you want.

- `version` is `2`.
- `lang` is `en`.
- `projectId` is `2`. `projectTypeId` is `1`. `layoutTypeId` is `2`.
- `page` is `1`. `perPage` is `10`. `tab` is `1`.
- `dayOffset` is `0`, today.
- `flag` is `y`. `variant` is `ran`. `segment` is `1`. `group` on results is `1`.
- Featured `scope` is `0`. Updates, last matches, and system status use `1`.

Send the parameter when you want a different value. Do not send an empty value.

## One id, from the previous response

Do not hardcode an id outside the example that uses it. Read `sharedindexes_event_id`, `tournament_template_id`, `tournament_id`, `sharedindexes_tournament_stage_id`, `rankingId`, and `sections[].categories[].id` from the call that returned them.

`providerId` comes from the snapshot for that block. Do not reuse a lineup `providerId` on player statistics.

## News section

On `/news`, send `sectionId` or `categoryId`, not a second name for a different concept. `categoryId` anywhere else is the sport category.

## Page path

Send `path` with no host. A team path has three parts and starts with `team`. A player path starts with `player`. The last part equals the id in the route path.

Tournament resolve takes `path`, or `sport`, `country`, and `slug` together. Ranking resolve takes `path`, or `sport` and `slug`.

## Named route before a raw feed

Call `/matches/{eventId}/stats` rather than building `df_st_1_{eventId}` yourself. Use `/feed/{version}/{feed}` when you already have the feed name and there is no named route.

## Odds region

Omit `geoIpCode` and `geoIpSubdivisionCode` to use the default region. Send them only for a hash that lists them, and only when you want a region.

## Pages

Ask for the next `page` when you need it. The first page is omitted or `page=1`. Fixtures, results, transfers, and entity news are the routes that list `page`.

## Images

Put the asset path after `/images/static/` or `/images/ott/`, including any slashes inside it.

## Cache and empty results

Read `Cache-Control` before repeating the same URL. A `204` means there is no data for those parameters.

A `400` does not name the field. Check the OpenAPI.

Do not send an account cookie or token.

## What is left out

There is no route outside the OpenAPI list. There is no body on these routes.
