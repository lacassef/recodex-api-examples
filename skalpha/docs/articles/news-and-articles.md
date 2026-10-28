# News and articles

How to open a list, then one item, then its comments. Filled calls are in [Examples](../guides/examples.md). The handoff from one response to the next is in [Workflows](../guides/workflows.md#article-or-news-then-comments).

On a detail call, send `sa_page_url`, `sa_referrer`, and `sa_query` when the operation lists them. Lists, trending, and comments do not use those parameters.

## List

Pick the list for the section. Article categories go on `/articles`. News categories go on `/news`. Do not put an article category on the news list. The tokens are in [Parameters](../guides/request-essentials.md#categories).

1. Call the list with `filter_category` set to that section. Set `include` for the objects you will render. Set `fields_news`, `fields_article`, or `fields_tag` when you want a smaller object.
2. For unread news, set `filter_unread` on `/news`. Omit it to include read items.
3. Short trending is `/news/trending` with a news category. Trending with a body is `/full-news/trending`. Set `fields_news` and `fields_tag` on the second when you want those fields. Article trending is `/articles/trending` with an article category, usually `latest-articles`.
4. Home with no single section is three calls: `/breaking-news`, `/leading-news-stories`, and `/feed`. On the feed, put the models in `models_list`. Set `without_list` to the blocks you want left out. Filter the feed by primary ticker with `any_primary_list`, by tag with `any_tags_list`, or by model with `all_list`. Publication time is `filter_since` and `filter_until` in seconds. Never send zero.
5. Education is `/education-top-articles` with one `education::` category. Send `lang=en` or omit `lang`. Do not send `undefined`.

Read each item's id and `links.self`. The next section uses both.

## Open a news item

Call `/news/{id}` with the id from the list. Put `links.self` in `sa_page_url`, with no host. Put the previous page path in `sa_referrer`, also with no host. Omit `sa_query` when there is no query string. Set `include` for the author and the tickers you will render.

The sidebar is a separate call to `/news-page-content-recommendations`. Put the same news id in `market_current_id` and set `variation` from that operation's enum.

## Open an article

Call `/articles/{id}` the same way. The detail `include` adds the presentation and the author bio when you will render them. `sa_page_url` is that article's `links.self`.

The author block is `/articles/{id}/author`. Set `include` for the bio. The id is the article id, not an author slug.

The sidebar is `/article-page-content-recommendations` with the article id in `article_id`.

A filing used as the previous page is still just `sa_referrer`. The filing's own detail takes `sa_page_url` in the form `/filing/{id}`.

## Comments

1. Call `comment-maps` on the article, news item, press release, or filing. Read the comment ids.
2. Call `comments` on that same item. Put those ids in `comment_ids`, comma-separated.
3. For replies to one comment, call `/comments/{id}/sub-comments` with that comment's id.

Use `include=user` and `sort=-top_parent_id` when the operation lists them.

## Press release and filing

Call `/press-releases/{id}` or `/filings/{id}` with the id in the path. A press release `include` asks for the acquire service and the primary tickers when you will render them. A filing `include` asks for the ticker. Put `sa_page_url` in the form `/pr/{id}-{slug}` or `/filing/{id}`.

Comment maps for both follow [Comments](#comments).

The PDF is `/filings/pdf/{id}`. The body is the file, not JSON. Follow redirects if you save it.

## Author

Take the author slug from `include=author` on the article list. Do not invent one.

1. Call `/authors/{slug}` for the profile. Set `include` for the articles and tickers you will render. Put `sa_page_url` in the form `/author/{slug}`.
2. Call `/authors/{slug}/article/ticker-counts` for the counts.
3. Call `/authors/{slug}/top-covered-symbols` for the symbols that author covers most.

## Search that leads to content

Call `/searches` for every type at once. Put the text in `filter_query` and the types in `filter_type`.

For one tab, call `/searches/{scope}` with that tab in the path and the same text in `filter_query`. Use `filter_period` for a quarter on headlines, news, and articles, and for all time on pages and people. Headlines can also take `filter_tags`.

The id in an article or news result goes in the path of `/articles/{id}` or `/news/{id}`. `links.self` goes in `sa_page_url`. A symbol result continues at [Symbol page](symbol-page.md).
