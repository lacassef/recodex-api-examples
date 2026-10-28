# Resource

A **Resource** is one item the list and detail routes return: an article, a news item, a press release, a filing, or an author. The two keys the guides name on that item are `id` and `links.self`.

**Where you'll see it:** `/articles`, `/news`, `/press-releases`, `/filings`, `/authors`, the symbol sub-resources that return those items, and `/feed`.

**Related models:** [Article](Article.md), [NewsItem](NewsItem.md), [Author](Author.md), [Ticker](Ticker.md), [Filing](Filing.md), [Comment](Comment.md).

`links.self` is a path with no host. On a detail call that lists `sa_page_url`, send that path. Examples from the guides: `/article/4938289-target-corporation-tgt-q2-2026-earnings-call-transcript`, `/news/4635195-target-projects-around-5-percent-fy2026-net-sales-growth`, `/pr/20666771-headline-slug`, `/filing/310003947`, `/author/{slug}`.

`include` names related objects. It does not add keys by itself beyond the objects you asked for. Names the guides use:

- Articles and news: `author`, `primaryTickers`, `secondaryTickers`, `sentiments`, `otherTags`
- An article page also uses `presentations`, `presentations.slides`, `author.authorResearch`, `author.userBio`
- A press release uses `acquireService` and `primaryTickers`
- A filing uses `formType` or `ticker`
- Comments use `user`
- A discussion uses `subject`, `subject.author`, `comments`, `comments.user`
- Indices use `tickers`
- People also follow uses `sector` and `sub_industry`

The feed asks for models with `models_list`: `Article`, `MarketCurrent`, `Research`. Those are request values. The items in the feed are still resources.

### Example

`4938289` and the path are the article in the [examples](../docs/guides/examples.md). Other keys depend on `include` and on the fields parameters.

```json
{
  "id": "4938289",
  "links": {
    "self": "/article/4938289-target-corporation-tgt-q2-2026-earnings-call-transcript"
  }
}
```

## Properties

- **id** (`value`):
    - The item id. Article, news, press-release, filing, and comment ids in the examples are numeric. The guides do not pick a JSON type. Put it in the next path.

- **links.self** (`string`):
    - Path of this item, with no host. `links` is the object that holds `self`.
