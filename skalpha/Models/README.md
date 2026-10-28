# Models

Shapes of the JSON you parse, and how those objects link. Paths are in [Routes](Routes.md). Parameters and operation ids are in [openapi/](../openapi/).

A `200` body is JSON. A `204` body is empty: the route exists and there is no data for those parameters. Do not parse a `204` as JSON. `/charts/lua` is not a JSON:API document. `/filings/pdf/{id}` is the file, not JSON.

These pages name keys the guides already name: `id`, `links.self`, the sparse field names, and `marketOpen`. They do not add an envelope. `include` asks for related objects. `fields_news`, `fields_article`, `fields_author`, and `fields_tag` ask for a smaller object. A listed field is a key that appears when that response has it. It is not a promise that every response includes it.

Error bodies are in [ErrorResponse](ErrorResponse.md).

## The data model

```
Resource                 one article, news item, press release, filing, or author
├── id
├── links.self           path, no host, for sa_page_url
├── author               include
├── primaryTickers       include
└── secondaryTickers     include
```

- A list returns items. Read each item's `id` and `links.self`.
- The next detail call puts `id` in the path. When that operation lists `sa_page_url`, put the `links.self` path there, with no host.
- Comment maps return the ids. The next call puts those ids in `comment_ids`. This page does not name the key inside the map.
- `marketOpen` is the named key on the session route. Chart series keys are not named.

Which call comes next is in [Workflows](../docs/guides/workflows.md).

## Keys at the top of a 200 body

| What you asked for | Key |
| --- | --- |
| An article, news item, press release, filing, or author | `id`, and `links.self` when the item has a path |
| A smaller article | the names in `fields_article`: `title`, `links`, `author` |
| A smaller author | the names in `fields_author`: `nick`, `image` |
| A smaller news item | the names in `fields_news`, such as `title`, `publish_on`, `date`, `comment_count` |
| A smaller tag | the names in `fields_tag`: `slug`, `name` |
| Symbol data or fundamental metrics | the names you sent in `fields_list` |
| US session | `marketOpen` |
| A chart | not JSON:API. No key is named here |
| A filing PDF | the file, not JSON |

## Entity pages

| Model | What it represents |
| --- | --- |
| [Resource](Resource.md) | The shared item: `id` and `links.self`. |
| [Article](Article.md) | Sparse article fields and the includes for a page. |
| [NewsItem](NewsItem.md) | Sparse news fields. |
| [Author](Author.md) | `nick` and `image`, and the author slug you send next. |
| [Tag](Tag.md) | `slug` and `name`. |
| [Ticker](Ticker.md) | The include. The slug and the numeric id are what later routes ask for. |
| [Comment](Comment.md) | Ids from comment maps, then the bodies. |
| [SymbolData](SymbolData.md) | Keys you named in `fields_list`. |
| [MarketSession](MarketSession.md) | `marketOpen`. |
| [Chart](Chart.md) | The chart body. No series keys are named. |
| [Filing](Filing.md) | JSON detail versus the PDF file. |
| [ErrorResponse](ErrorResponse.md) | `error.status`, `error.title`, `error.request_id`. |
