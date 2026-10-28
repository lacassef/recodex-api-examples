# NewsItem

A **NewsItem** is a [Resource](Resource.md) from `/news` or `/news/{id}`.

**Where you'll see it:** the news list, trending, full-news trending, and the news page. `4635195` is the news id in the [examples](../docs/guides/examples.md).

**Related models:** [Tag](Tag.md), [Ticker](Ticker.md), [Author](Author.md), [Comment](Comment.md).

`fields_news` selects a smaller object. The examples ask for `title` and `publish_on`, and for `title`, `date`, and `comment_count`. `fields_tag` selects `slug` and `name` on the tags. A detail `include` asks for `author`, `primaryTickers`, `secondaryTickers`, and `otherTags`.

## Properties

- **id** (`value`):
    - News id. See [Resource](Resource.md).

- **links.self** (`string`):
    - Path for `sa_page_url`.

- **title** (`string`):
    - Present when `fields_news` asks for `title`, and on a full item.

- **publish_on** (`value`):
    - Present when `fields_news` asks for `publish_on`. The guides do not pick a JSON type.

- **date** (`value`):
    - Present when `fields_news` asks for `date`. The guides do not pick a JSON type.

- **comment_count** (`value`):
    - Present when `fields_news` asks for `comment_count`. The guides do not pick a JSON type.
