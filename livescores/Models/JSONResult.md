# JSONResult

A JSON object whose keys depend on the route. This page does not list them.

**Where you'll see it:** `/banners`, `/content/media`, `/remote-stats`, `/graphql`, and `/odds`.

GraphQL and odds take `_hash` plus the query parameters that hash lists. The body is the JSON for that hash. Banners, content media, and remote stats are the same kind of object: read the keys the response actually contains.

A `204` has no body.
