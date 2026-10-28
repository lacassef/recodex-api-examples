# Examples

Replace `{api-host}`. The names are the OpenAPI names. Ids in these curls (`08W6fzLP`, `COuk57Ci`, `lId4TMwf`, `UkhgIFEq`, `4KeVObqb`, `v3LmzFnC`) belong to these examples. Another event has another id.

## Scoreboard and lists

Soccer today. Omit `dayOffset` for the same day.

```sh
curl "https://{api-host}/api/livescores/sports/1/scoreboard?dayOffset=0&lang=en"
curl "https://{api-host}/api/livescores/sports/1/refresh"
curl "https://{api-host}/api/livescores/sports/1/odds?dayOffset=0&lang=en"
curl "https://{api-host}/api/livescores/sports/31/featured?scope=0&lang=en"
```

A feed by name. Prefer the scoreboard route when that is the data you want.

```sh
curl "https://{api-host}/api/livescores/feed/2/f_1_0_2_en_1"
```

## Navigation and categories

```sh
curl "https://{api-host}/api/livescores/navigation/1/17"
curl "https://{api-host}/api/livescores/req/m_1_17"
curl "https://{api-host}/api/livescores/sports/3/categories"
curl "https://{api-host}/api/livescores/sports/32/categories?path=motorsport/auto-racing"
curl "https://{api-host}/api/livescores/sports/1/categories/98/tournaments?lang=en&flag=y"
```

## Tournament

Template `COuk57Ci` is category `98` in these examples. `round` comes from the tournament you opened.

```sh
curl "https://{api-host}/api/livescores/tournaments/resolve?path=football/england/premier-league"
curl "https://{api-host}/api/livescores/tournaments/archive?path=football/england/premier-league"
curl "https://{api-host}/api/livescores/tournaments/1/98/COuk57Ci/matches?lang=en"
curl "https://{api-host}/api/livescores/tournaments/1/98/COuk57Ci/fixtures?round=187&page=1&lang=en"
curl "https://{api-host}/api/livescores/tournaments/2/182/GrsQDFC0/results?segment=1&lang=en"
curl "https://{api-host}/api/livescores/tournaments/M1c7lv64/tables/tKE3WZmL"
curl "https://{api-host}/api/livescores/tournaments/8recE9FQ/overview/dK0Jjau7?tab=1"
curl "https://{api-host}/api/livescores/tournaments/UFxNEUzj/draw/vFA41USe?groupId=QRiI3vYF"
curl "https://{api-host}/api/livescores/tournaments/UFxNEUzj/seasons/vFA41USe"
curl "https://{api-host}/api/livescores/sports/2/season-calendar"
```

## Match

`08W6fzLP` is the event id in these examples. Read the next one from `sharedindexes_event_id`.

```sh
curl "https://{api-host}/api/livescores/matches/08W6fzLP/stats"
curl "https://{api-host}/api/livescores/matches/08W6fzLP/commentary"
curl "https://{api-host}/api/livescores/matches/08W6fzLP/h2h"
curl "https://{api-host}/api/livescores/matches/08W6fzLP/odds-detail"
curl "https://{api-host}/api/livescores/matches/08W6fzLP/timeline"
curl "https://{api-host}/api/livescores/matches/Us8CuWaN/box-score"
curl "https://{api-host}/api/livescores/matches/ragg03vI/lineups"
curl "https://{api-host}/api/livescores/matches/ragg03vI/lineups/updates?providerId=PROVIDER"
curl "https://{api-host}/api/livescores/matches/ragg03vI/missing-players"
curl "https://{api-host}/api/livescores/matches/ragg03vI/player-statistics"
curl "https://{api-host}/api/livescores/matches/ragg03vI/stage"
curl "https://{api-host}/api/livescores/matches/08W6fzLP/highlights"
curl "https://{api-host}/api/livescores/matches/vH0563UN/highlights/videos"
curl "https://{api-host}/api/livescores/matches/vH0563UN/report/html"
```

`PROVIDER` stands for `providerId` from the snapshot you just called.

## Participants and players

```sh
curl "https://{api-host}/api/livescores/participants/69Dxbc61/matches?sportId=1&categoryId=98&lang=en"
curl "https://{api-host}/api/livescores/participants/lId4TMwf/squad?path=team/liverpool/lId4TMwf"
curl "https://{api-host}/api/livescores/participants/69Dxbc61/transfers?tab=1&page=1"
curl "https://{api-host}/api/livescores/participants/zNO51Dz3/events/IBdwmTR0/detail"
curl "https://{api-host}/api/livescores/players/UkhgIFEq/profile"
curl "https://{api-host}/api/livescores/players/UkhgIFEq/match-record?slug=alcaraz-garfia-carlos"
curl "https://{api-host}/api/livescores/players/UkhgIFEq/injuries?path=player/alcaraz-garfia-carlos/UkhgIFEq"
```

## Rankings, news, search

```sh
curl "https://{api-host}/api/livescores/rankings/resolve?path=tennis/rankings/atp"
curl "https://{api-host}/api/livescores/rankings/tennis/atp/id"
curl "https://{api-host}/api/livescores/rankings/4KeVObqb?variant=ran&tab=1"
curl "https://{api-host}/api/livescores/news?sportId=1&sectionId=59"
curl "https://{api-host}/api/livescores/news/articles/v3LmzFnC"
curl "https://{api-host}/api/livescores/news/entities/41/MP4jLdJh?page=1&perPage=10"
curl "https://{api-host}/api/livescores/search?q=arsenal"
curl "https://{api-host}/api/livescores/top-search"
```

On the news list, `categoryId=59` is the same section when `sectionId` is omitted.

## Persisted queries, updates, images

Omit the geo parameters to use the default region.

```sh
curl "https://{api-host}/api/livescores/graphql?_hash=dmpe2&eventId=08W6fzLP&projectId=2"
curl "https://{api-host}/api/livescores/odds?_hash=oce&eventId=08W6fzLP&projectId=2"
curl "https://{api-host}/api/livescores/updates?sportId=1"
curl "https://{api-host}/api/livescores/updates/list?sportId=2"
curl "https://{api-host}/api/livescores/system/status"
curl "https://{api-host}/api/livescores/images/static/res/image/data/bookmakers/80-915.png"
curl "https://{api-host}/api/livescores/images/ott/r300xfq60/26bb49b4-4e3b-4899-9055-dc456da25e10.avif"
```

`ope2` also takes `bookmakerId`, `betType`, and `betScope` from the odds row you are opening. Those names are in [Persisted queries](../graphql/overview.md).
