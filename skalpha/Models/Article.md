# Article

An **Article** is a [Resource](Resource.md) from `/articles` or `/articles/{id}`.

**Where you'll see it:** the article list, trending, and the article page. `4938289` is the article id in the [examples](../docs/guides/examples.md).

**Related models:** [Author](Author.md), [Ticker](Ticker.md), [Comment](Comment.md).

`fields_article` selects a smaller object. The trending example asks for `title`, `links`, and `author`. A page `include` asks for `author`, `primaryTickers`, `secondaryTickers`, `otherTags`, `presentations`, `presentations.slides`, `author.authorResearch`, and `author.userBio`. The list example uses `author`, `primaryTickers`, `secondaryTickers`, and `sentiments`.

This page does not name keys inside `presentations` or `sentiments`.

## Properties

- **id** (`value`):
    - Article id. See [Resource](Resource.md).

- **links** (`object`):
    - Holds `self`. The trending field list asks for `links`.

- **links.self** (`string`):
    - Path for `sa_page_url`.

- **title** (`string`):
    - Present when you ask for it in `fields_article`, and on a full article.

- **author** (`Author`):
    - Present when `fields_article` or `include` asks for `author`.
