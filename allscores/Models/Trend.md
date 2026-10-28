# Trend

A **Trend** is one betting trend card.

**Where you'll see it:** the trends list and the single-trend route.

**Related models:** [ScoresList](ScoresList.md), [BestOdds](BestOdds.md). Send `id` as `trendId`.

The list names `text`, `outcome`, `percentage`, `confidenceTrendIds`, `lineTypeId`, and `betCTA`. The single trend adds `id`, `divId`, `lineTypeTitle`, and `gameId`. A quiet date can return only `lastUpdateId` and `ttl`.

### Example

`4669892` is the game id in the [examples](../guides/examples.md). The other strings are shape. The guides do not publish a `trendId`.

```json
{
  "gameId": 4669892,
  "text": "",
  "lineTypeTitle": ""
}
```

## Properties

- **id** (`number`):
    - Trend id on the single-trend route. Send it as `trendId`.

- **text** (`string`):
    - The card text.

- **outcome** (`value`):
    - Outcome on a list card.

- **percentage** (`value`):
    - Percentage on a list card.

- **confidenceTrendIds** (`array`):
    - Related trend ids on a list card.

- **lineTypeId** (`number`):
    - Line type on a list card.

- **betCTA** (`value`):
    - Call to action on the card.

- **divId** (`string`):
    - Present on the single trend.

- **lineTypeTitle** (`string`):
    - Present on the single trend.

- **gameId** (`number`):
    - Game id on the single trend.
