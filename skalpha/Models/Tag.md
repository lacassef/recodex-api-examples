# Tag

A **Tag** is the smaller tag object `fields_tag` selects.

**Where you'll see it:** full-news trending and other news routes that list `fields_tag`. The example asks for `slug` and `name`.

**Related models:** [NewsItem](NewsItem.md). `otherTags` on a detail `include` is the related list. This page does not name further keys on that list.

## Properties

- **slug** (`string`):
    - Present when `fields_tag` asks for `slug`.

- **name** (`string`):
    - Present when `fields_tag` asks for `name`.
