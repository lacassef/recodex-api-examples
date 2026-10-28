# NewsCard

A **NewsCard** is one item in the news list.

**Where you'll see it:** the news route. The body also includes `newsSources`.

**Related models:** [ScoresList](ScoresList.md) for the games, competitions, competitors, and athletes you filter by.

There is no article route. `url` is the link the card already carries.

### Example

The strings are shape. The guides do not publish a news card id.

```json
{
  "title": "",
  "publishDate": "",
  "image": "",
  "url": ""
}
```

## Properties

- **id** (`number`):
    - Card id.

- **title** (`string`):
    - Headline.

- **publishDate** (`string`):
    - When the card was published.

- **image** (`string`):
    - Image on the card.

- **url** (`string`):
    - Link the response already carries.

- **sourceId** (`number`):
    - Source of the card.

- **isMagazine** (`value`):
    - Whether the card is a magazine item. The description does not pick a JSON type.

- **newsSources** (`array`):
    - Sources for the cards in this body. This key sits beside the cards, not inside one card.
