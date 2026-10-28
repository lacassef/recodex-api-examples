# Examples

Replace `{api-host}`. The names are the OpenAPI names. Ids in these curls belong to these examples. Another game, competition, or athlete has another id.

## Catalog and scores

```sh
curl "https://{api-host}/api/allscores/sports"
curl "https://{api-host}/api/allscores/sports?withCount=true&langId=31"
curl "https://{api-host}/api/allscores/countries?sportId=1&langId=31&timezone=Africa/Maputo"
curl "https://{api-host}/api/allscores/games-scores?sport=1&startDate=30/09/2026&endDate=30/09/2026&langId=31&timezone=Africa/Maputo"
curl "https://{api-host}/api/allscores/featured-games?sport=1&context=1&numberOfGames=4&showOdds=true"
curl "https://{api-host}/api/allscores/games-top?sport=1&context=1&showOdds=true&numberOfGames=4"
```

## One game

`4669892` is the game id. `2378-5050-5930` is a `matchupId`.

```sh
curl "https://{api-host}/api/allscores/game-details?gameId=4669892&langId=31"
curl "https://{api-host}/api/allscores/game-details?matchupId=2378-5050-5930"
curl "https://{api-host}/api/allscores/game-stats?games=4669892&onlyIsMajor=true"
curl "https://{api-host}/api/allscores/stats-pregame?game=4669892&onlyMajor=true"
curl "https://{api-host}/api/allscores/game-lineups?gameId=4669892"
curl "https://{api-host}/api/allscores/h2h?gameId=4669892&addMainOdds=true"
curl "https://{api-host}/api/allscores/h2h?matchupId=1266-1773-116"
curl "https://{api-host}/api/allscores/point-by-point?gameId=4669892"
curl "https://{api-host}/api/allscores/playbyplay-comments?lang=31&fixtureid=57dotnff3xaafnxfltzt4czdg&sportifiergameid=4669892"
```

## Competition and competitor

```sh
curl "https://{api-host}/api/allscores/featured-competitions?sport=1&type=stats&withSeasons=true"
curl "https://{api-host}/api/allscores/competition-details?competition=5930&withSeasons=true&type=stats"
curl "https://{api-host}/api/allscores/competition-standings?competition=7016&type=1"
curl "https://{api-host}/api/allscores/competition-brackets?competition=232"
curl "https://{api-host}/api/allscores/fixtures?competitorIds=2379"
curl "https://{api-host}/api/allscores/results?competitions=5930"
curl "https://{api-host}/api/allscores/competitor-details?competitorId=2379&withSeasons=true"
curl "https://{api-host}/api/allscores/competitor-squads?competitorId=1357"
curl "https://{api-host}/api/allscores/competitor-recent-form?competitor=2379&numOfGames=5"
curl "https://{api-host}/api/allscores/transfers?competitions=215&onlyConfirmed=true&limit=4"
```

The next page is `/paging`. Put `paging.nextPage` or `paging.previousPage` from that response in `paging`.

## Athletes, news, search

```sh
curl "https://{api-host}/api/allscores/search?query=raphinha&filter=all&sport=1"
curl "https://{api-host}/api/allscores/athlete-details?athleteId=817&competitionId=116&fullDetails=true"
curl "https://{api-host}/api/allscores/athlete-details?athleteId=817,45579"
curl "https://{api-host}/api/allscores/athlete-career?athleteId=40557&seasonKey=-1"
curl "https://{api-host}/api/allscores/athlete-trophy-stats?athleteId=817&competitionId=7016"
curl "https://{api-host}/api/allscores/athlete-next-game?athletes=817"
curl "https://{api-host}/api/allscores/news?sport=1&isPreview=true"
curl "https://{api-host}/api/allscores/top-athletes?sportType=1&limit=10"
```

## Odds

```sh
curl "https://{api-host}/api/allscores/game-bet-line?games=4669892"
curl "https://{api-host}/api/allscores/best-odds?competition=232&sport=1&minGames=3&maxGames=4"
curl "https://{api-host}/api/allscores/best-odds?games=4669892"
curl "https://{api-host}/api/allscores/bets-outrights?competitions=5930"
curl "https://{api-host}/api/allscores/bets-proposition?gameId=4669892&athleteId=40557"
curl "https://{api-host}/api/allscores/bets-teaser?gameId=4669892"
curl "https://{api-host}/api/allscores/game-predictions?sport=1&competitors=131,132"
curl "https://{api-host}/api/allscores/trends?games=4669892"
```

Send `lineId` from the outrights response to `/bets-outright-details`. Send `trend.id` to `/trend-details` as `trendId`.

## Images

```sh
curl "https://{api-host}/api/allscores/img/small/athlete/48583/version/3"
curl "https://{api-host}/api/allscores/img/large/athlete/48583/version/3"
curl "https://{api-host}/api/allscores/img/small/competitor/131/version/3"
curl "https://{api-host}/api/allscores/img/small/light/country/54/competition/570/version/4"
curl "https://{api-host}/api/allscores/img/large/light/country/54/competition/5930/version/19"
curl "https://{api-host}/api/allscores/img/small/country/1/competition/572/version/3"
curl "https://{api-host}/api/allscores/img/flag/country/21"
curl "https://{api-host}/api/allscores/img/trophy/5069"
```
