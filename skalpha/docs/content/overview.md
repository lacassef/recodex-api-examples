# Content

News, articles, press releases, filings, authors, and the feed. Parameter shape, pagination, and categories are in [Parameters](../guides/request-essentials.md). The detail step is in [News and articles](../articles/news-and-articles.md).

`page_size` is 1 to 50. `lang` is optional on every route. Do not send `isMounting`. It is not a parameter.

## News

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/breaking-news` | Short headlines. | — | `lang` | No other parameters. |
| `/api/skalpha/news` | List with a category. | — | `fields_news`, `fields_tag`, `filter_category`, `filter_since`, `filter_until`, `filter_unread`, `include`, `lang`, `page_size`, `page_number` | Example include: `primaryTickers,secondaryTickers`. `filter_unread=true` limits the list to unread items. |
| `/api/skalpha/news/trending` | Trending. | — | `filter_category`, `include`, `page_size`, `page_number` | Category `market-news::all` or `market-news::trending`. Include `author`. |
| `/api/skalpha/news/{id}` | One news item. | `id` | `include`, `lang`, `sa_page_url`, `sa_referrer`, `sa_query` | Include `author,primaryTickers,secondaryTickers,otherTags`. `sa_page_url` is the `links.self` path. |
| `/api/skalpha/news/{id}/comment-maps` | Comment ids. | `id` | `include`, `sort`, `lang` | `include=user`, `sort=-top_parent_id`. |
| `/api/skalpha/news/{id}/comments` | Bodies. | `id` | `comment_ids`, `include`, `sort`, `lang` | `comment_ids` comma-separated, ids from `comment-maps`. |
| `/api/skalpha/news-page-content-recommendations` | News sidebar. | — | `market_current_id`, `variation` | Use `variation=variation_b`. |
| `/api/skalpha/full-news/trending` | Trending with more fields. | — | `fields_news`, `fields_tag`, `filter_category`, `include`, `page_size`, `page_number` | `page_size` up to 50. A full body uses 50. |
| `/api/skalpha/leading-news-stories` | Home highlights. | — | `lang` | No pagination. |

## Articles

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/articles` | List by article category. | — | `fields_article`, `filter_category`, `filter_since`, `filter_until`, `include`, `page_size`, `page_number` | Include `author,primaryTickers,secondaryTickers,sentiments`. |
| `/api/skalpha/articles/trending` | Analysis trending. | — | `fields_article`, `fields_author`, `filter_category`, `include`, `page_size`, `page_number` | Category `latest-articles`. Fields `title,links,author` and author `nick,image`. |
| `/api/skalpha/articles/{id}` | One article. | `id` | `include`, `lang`, `sa_page_url`, `sa_referrer`, `sa_query` | Page include: `author,primaryTickers,secondaryTickers,otherTags,presentations,presentations.slides,author.authorResearch,author.userBio`. |
| `/api/skalpha/articles/{id}/author` | Author of that article. | `id` | `include` | `authorResearch,userBioTags`. |
| `/api/skalpha/articles/{id}/comment-maps` | Comment ids. | `id` | `include`, `sort` | `user` and `-top_parent_id`. |
| `/api/skalpha/articles/{id}/comments` | Bodies. | `id` | `comment_ids`, `include`, `sort`, `lang` | Same shape as news. |
| `/api/skalpha/comments/{id}/sub-comments` | Replies to one comment. | `id` | `include`, `sort`, `lang` | `include` in the spec is `user`. |
| `/api/skalpha/article-page-content-recommendations` | Article sidebar. | — | `article_id`, `variation` | Use `variation=variation_a`. |
| `/api/skalpha/education-top-articles` | Top of one education category. | — | `filter_category`, `lang`, `page_size` | Category is an `education::` token. Example: `page_size=3` and `lang=en`. |

## Press releases

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/press-releases/{id}` | One press release. | `id` | `include`, `sa_page_url`, `sa_referrer`, `sa_query` | Include `acquireService,primaryTickers`. `sa_page_url` in the form `/pr/{id}-{slug}`. |
| `/api/skalpha/press-releases/{id}/comment-maps` | Comment ids. | `id` | `include`, `sort` | `user`, `-top_parent_id`. |

## Filings

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/filings/{id}` | One filing. | `id` | `include`, `sa_page_url`, `sa_referrer`, `sa_query` | Include `ticker`. Page path: `/filing/{id}`. |
| `/api/skalpha/filings/{id}/comment-maps` | Comment ids. | `id` | `include`, `sort` | Same as the other maps. |
| `/api/skalpha/filings/pdf/{id}` | PDF. | `id` | — | The body is the PDF, not JSON. |

## Authors

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/authors/{slug}` | Profile. | `slug` | `include`, `sa_page_url`, `sa_referrer`, `sa_query` | `sa_page_url=/author/{slug}`. |
| `/api/skalpha/authors/{slug}/article/ticker-counts` | Ticker counts across articles. | `slug` | — | Aggregate. |
| `/api/skalpha/authors/{slug}/top-covered-symbols` | Most covered symbols. | `slug` | — | — |

## Feed

| Route | Purpose | Required | Optional | Notes |
| --- | --- | --- | --- | --- |
| `/api/skalpha/feed` | Home blocks. | `models_list` | `all_list`, `any_tags_list`, `any_primary_list`, `include`, `page_size`, `page_number`, `filter_since`, `filter_until`, `custom_sort`, `without_list` | Models: `Article`, `MarketCurrent`, `Research`. Example: the first two. `without_list`: `transcripts`, `earnings-slides`, `exclude-feed`. |
