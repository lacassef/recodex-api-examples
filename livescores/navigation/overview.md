# Navigation and categories

Filled calls are in [Examples](../guides/examples.md).

## Req

GET `/api/livescores/req/{req}`

Parameters:

- `req` (path, required)

Response: `ReqResponse` when `req` starts with `m_`. Any other value is returned as received.

## Navigation by sport and country

GET `/api/livescores/navigation/{sportId}/{countryId}`

Parameters:

- `sportId` (path, required)
- `countryId` (path, required)

Response: `ReqResponse`

## Sport categories

GET `/api/livescores/sports/{sportId}/categories`

Parameters:

- `sportId` (path, required)
- `path` (query). Send it only to override the sport page, such as `motorsport/auto-racing`.

Response: `CategoriesResponse`

Read `sections[].categories[].id` for the next tournament list. That id is `categoryId`.

## Category tournaments

GET `/api/livescores/sports/{sportId}/categories/{categoryId}/tournaments`

Parameters:

- `sportId` (path, required)
- `categoryId` (path, required). This is the sport category, not a news section.
- `projectId` (query, omit for `2`)
- `lang` (query, omit for `en`)
- `flag` (query, `y` or `n`, omit for `y`)
- `group` (query, omit for `1`)
- `version` (query, omit for `2`)

Response: `FeedResponse`

`tournament_template_id` in the feed is `templateId` for the tournament match routes.
