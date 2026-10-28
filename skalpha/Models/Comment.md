# Comment

A **Comment** is one comment on an article, a news item, a press release, or a filing.

**Where you'll see it:** `comment-maps`, then `comments`, then `/comments/{id}/sub-comments`.

**Related models:** [Article](Article.md), [NewsItem](NewsItem.md).

`comment-maps` returns the ids. The next call sends those ids in `comment_ids`, comma-separated. The guides do not name the key inside the map. Use `include=user` and `sort=-top_parent_id` when the operation lists them.

The comments route returns the bodies for those ids. This page does not name the keys inside a body. Replies to one comment use that comment's id in `/comments/{id}/sub-comments`.

`103525208` and `103517498` are comment ids in the [examples](../docs/guides/examples.md). `103368775` and `103339973` are the ids in the FAQ list.
