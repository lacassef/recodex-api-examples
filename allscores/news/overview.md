# News

GET `/api/allscores/news`

Filter with one of these, and the shared parameters:

- `sport`
- `games`, `competitions`, `competitors`, `athletes`
- `countries`, `userCompetitions`, `userCompetitors`
- `isPreview` — short list. Omit it for the full list.

Each card has `id`, `title`, `publishDate`, `image`, `url`, `sourceId`, and `isMagazine`. The body also includes `newsSources`.

There is no article route. The card's `url` is the link the response already carries. A filled call is in [Examples](../guides/examples.md).
