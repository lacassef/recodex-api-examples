# Models

Shapes of the JSON you parse, and how those objects link. Paths are in [Routes](Routes.md). Parameters and operation ids are in [openapi/](../openapi/).

A `200` body is the payload for that route. A `204` body is empty: the route is valid and there is nothing for those parameters. Do not parse it as JSON. Error bodies are in [ErrorResponse](ErrorResponse.md).

`/images/static/{path}` returns `image/png`. `/images/ott/{path}` returns `image/avif`. `/matches/{eventId}/report/html` returns HTML. Those three have no JSON model.

## The data model

```
Sport
└── CategoryItem          a country or tour inside a section
    └── Tournament        templateId, then tournamentId and stageId
        └── Event         one match, id in sharedindexes_event_id
            ├── Participant
            └── Player
```

- A scoreboard or a match list is a [FeedResponse](FeedResponse.md). Read `records[].fields.sharedindexes_event_id`. That value is `eventId`.
- [CategoriesResponse](CategoriesResponse.md) lists the categories of a sport. `sections[].categories[].id` is `categoryId` on tournament and participant routes.
- [TournamentResolveResponse](TournamentResolveResponse.md) turns a path into `tournamentId`, `stageId`, and `templateId`.
- A [ParticipantSquadResponse](ParticipantSquadResponse.md) is one team sheet. Player tables are [PlayerMatchRecordResponse](PlayerMatchRecordResponse.md), [PlayerTournamentsWonResponse](PlayerTournamentsWonResponse.md), and [PlayerInjuriesResponse](PlayerInjuriesResponse.md).

Which call comes next is in [Workflows](../guides/workflows.md).

## Keys at the top of a 200 body

| What you asked for | Key |
| --- | --- |
| A feed or a scoreboard | `records`, plus `version`, `feed`, and `header` |
| A navigation `req` | `req`, `header`, `records` |
| Categories | `sections` |
| A ranking id | `rankingId` |
| A resolved tournament | `tournamentId`, `stageId`, `templateId` |
| An archive | `seasons` |
| A squad | `sections` |
| Match record, titles, injuries | `tables` or `injuries` |
| GraphQL or odds | the JSON object for that `_hash`. There is no fixed key on this page |
| Banners, content media, remote stats | a [JSON object](JSONResult.md) with no fixed key |

A missing key and `null` mean that fact is not in this response. Feed field values are strings, or arrays when the value is a list. Extra keys can appear. Ignore the ones you do not use.

## Entity pages

| Model | What it represents |
| --- | --- |
| [FeedResponse](FeedResponse.md) | A normalized feed: header plus records. |
| [ReqResponse](ReqResponse.md) | The same records, keyed by a `req` id. |
| [CategoriesResponse](CategoriesResponse.md) | Sections and categories for one sport. |
| [RankingIDResponse](RankingIDResponse.md) | The id that opens a ranking table. |
| [TournamentResolveResponse](TournamentResolveResponse.md) | Ids for one tournament path. |
| [TournamentArchiveResponse](TournamentArchiveResponse.md) | Past seasons and the winner of each. |
| [ParticipantSquadResponse](ParticipantSquadResponse.md) | Squad sections, rows, and players. |
| [PlayerMatchRecordResponse](PlayerMatchRecordResponse.md) | Season rows for one player. |
| [PlayerTournamentsWonResponse](PlayerTournamentsWonResponse.md) | Titles grouped by year. |
| [PlayerInjuriesResponse](PlayerInjuriesResponse.md) | Injury rows. |
| [JSONResult](JSONResult.md) | A JSON object with no fixed keys. |
| [ErrorResponse](ErrorResponse.md) | `error.status`, `error.title`, `error.request_id`. |
