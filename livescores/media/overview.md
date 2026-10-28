# Media and assets

Filled calls are in [Examples](../guides/examples.md).

## Banners

GET `/api/livescores/banners`

Response: `JSONResult`

## Content media

GET `/api/livescores/content/media`

Response: `JSONResult`

## Remote stats

GET `/api/livescores/remote-stats`

Response: `JSONResult`

## Static images

GET `/api/livescores/images/static/{path}`

Parameters:

- `path` (path, required). It can contain slashes.

Response: `image/png`

## Media images

GET `/api/livescores/images/ott/{path}`

Parameters:

- `path` (path, required). It can contain slashes. A news cover or a photo uses this route.

Response: `image/avif`
