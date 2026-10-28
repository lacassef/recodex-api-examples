# Models

Shapes of the JSON you parse, and how those objects link. Paths are in [Routes](Routes.md). Parameters and operation ids are in [openapi/](../openapi/). The same field names are summarized in [Schemas](../reference/schemas.md).

A `200` body is JSON. The spec also lists `204` when the route exists and there is no data. That body is empty: do not parse it as JSON. Some routes still return `200` with an empty object or an empty list. Outrights with no market, and team of the week with no selection, return an empty object. A teaser or a raffle can return `bookmakers` empty. A suggestions call that only sends `sport` can return an empty list. A trends call for a quiet date can return only `lastUpdateId` and `ttl`. Parse those `200` bodies.

Image routes return `image/png`. They have no JSON model. Sizes are in [Image](Image.md).

Error bodies are in [ErrorResponse](ErrorResponse.md). A `400` has `title` `Bad Request` and does not name the parameter.

A listed field is a key that appears. It is not a promise that every response includes it. A missing key means that fact is not in this response. Extra keys can appear. Ignore the ones you do not use.

## The data model

```
Sport
└── Country
    └── Competition
        └── Game
            ├── Competitor
            │   └── Athlete
            ├── News card
            └── Trend / Outright line
```

- [Sport](Sport.md) and [Country](Country.md) are the catalogs. `id` on a sport is `sport`, `sportId`, or `sportType` on the next call, whichever that operation lists.
- [Competition](Competition.md) `id` is `competition`, `competitionId`, or `competitions`. `currentSeasonNum` and `currentStageNum` are `seasonNum` and `stageNum` on standings.
- A scores list is a [ScoresList](ScoresList.md). Read the game id from `games` and send it as `gameId`, `game`, `games`, or `sportifiergameid`, whichever the next operation lists.
- [Competitor](Competitor.md) `id` is `competitorId`, `competitor`, `competitors`, or `competitorIds`.
- [Athlete](Athlete.md) `id` is `athleteId` or `athletes`.

Which call comes next is in [Workflows](../guides/workflows.md).

## Keys at the top of a 200 body

| What you asked for | Key |
| --- | --- |
| Sports catalog | each sport's `id`, `name`, `nameForURL`, `imageVersion`, plus `lastUpdateId`, `requestedUpdateId`, `ttl` |
| Countries | `countries`, plus `sports`, `lastUpdateId`, `requestedUpdateId`, `ttl` |
| A scores list | `games`, `summary`, and the sports, countries, competitions, and competitors that label the rows |
| Fixtures or results | `games`, `summary`, `competitionFilters`, `paging` |
| One competition | the competition fields on [Competition](Competition.md) |
| A table | `standings` |
| One competitor | the competitor fields on [Competitor](Competitor.md) |
| Athletes | the athlete fields on [Athlete](Athlete.md) |
| News | the cards, plus `newsSources` |
| Search | competitions, competitors, and athletes, plus sports and countries |
| Trends | each trend, plus `lastUpdateId` and `ttl` |
| Best odds | `lines`, `lineTypes`, `bookmakers`, and the games |
| Play-by-play | `Messages`, `UpdateURL`, `TTL` |

## Entity pages

| Model | What it represents |
| --- | --- |
| [ScoresList](ScoresList.md) | Games plus the catalogs that label them. |
| [Paging](Paging.md) | `nextPage` and `previousPage`. |
| [Sport](Sport.md) | One sport in the catalog. |
| [Country](Country.md) | One country in the catalog. |
| [Competition](Competition.md) | One competition. |
| [Competitor](Competitor.md) | One team or side. |
| [Athlete](Athlete.md) | One person. |
| [Standings](Standings.md) | The table for a season and stage. |
| [NewsCard](NewsCard.md) | One news card. |
| [Trend](Trend.md) | One betting trend. |
| [Outright](Outright.md) | One futures line. |
| [BestOdds](BestOdds.md) | Lines, line types, and bookmakers. |
| [PlayByPlay](PlayByPlay.md) | Commentary. |
| [GameStats](GameStats.md) | Team statistics for a game. |
| [Lineup](Lineup.md) | Players on the pitch. |
| [HeadToHead](HeadToHead.md) | Previous meetings. |
| [Transfer](Transfer.md) | One player move. |
| [Related](Related.md) | A linked competition, competitor, or athlete. |
| [SeasonStats](SeasonStats.md) | Leader tables for a competition. |
| [Career](Career.md) | Career tables and trophy stats. |
| [Bracket](Bracket.md) | A knockout draw. |
| [History](History.md) | Past winners. |
| [Search](Search.md) | The three result lists. |
| [Image](Image.md) | PNG sizes. There is no JSON body. |
| [ErrorResponse](ErrorResponse.md) | `error.status`, `error.title`, `error.request_id`. |
