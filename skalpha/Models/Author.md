# Author

An **Author** is the person attached to an article or a news item, or the body of `/authors/{slug}`.

**Where you'll see it:** `include=author`, `/articles/{id}/author`, and `/authors/{slug}`.

**Related models:** [Article](Article.md), [Resource](Resource.md).

`fields_author` on article trending asks for `nick` and `image`. The author route's `include` asks for `authorResearch` and `userBioTags`. An article page also asks for `author.authorResearch` and `author.userBio`.

Take the author slug from `include=author` on the article list. The guides do not name the key that holds that slug. Send the slug you read on `/authors/{slug}`.

## Properties

- **nick** (`string`):
    - Present when `fields_author` asks for `nick`.

- **image** (`value`):
    - Present when `fields_author` asks for `image`. The description does not pick a JSON type.

- **authorResearch** (`value`):
    - Present when `include` asks for `authorResearch` or `author.authorResearch`.

- **userBioTags** (`value`):
    - Present when the author route's `include` asks for `userBioTags`.

- **userBio** (`value`):
    - Present when an article page asks for `author.userBio`.
