# Routes

Every published AllScores API route, one row per path. A `*` after a query name means that parameter is required. Omit an optional one you are not using.

Most JSON routes also take `langId`, `timezone`, `publisherId`, `campaign`, and `userCountryId`. Those five are left off this table. Images do not take them. Play-by-play uses `lang` and does not take that set. Paging takes `publisherId`, `campaign`, and `userCountryId`, and does not take `langId` or `timezone`.

A `200` body is JSON. Image routes return `image/png`. The spec also lists `204` when the route exists and there is no data. Some routes still return `200` with an empty object or an empty list. The objects callers parse are in [README](README.md). Machine-readable parameters are in [openapi/](../openapi/).

## athlete-career

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-career` | athleteId, seasonKey | Get athlete career |

## athlete-chart-events

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-chart-events` | athletes | Get athlete chart events |

## athlete-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-details` | athleteId, competitionId, competition, fullDetails, topBookmaker | Get athlete details |

## athlete-games

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-games` | athleteId, competitionId, statType, lastMatchLimit | Get athlete games |

## athlete-next-game

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-next-game` | athletes, fullDetails, lastUpdateId, topBookmaker | Get athlete next game |

## athlete-trophy-stats

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/athlete-trophy-stats` | athleteId, competitionId | Get athlete trophy stats |

## best-odds

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/best-odds` | games, competition, sport, minGames, maxGames, lastUpdateId, lineType, bookmakerId, context, withCompetitionFilter, topBookmaker | Get best odds |

## bets-outright-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/bets-outright-details` | lineId, lastUpdateId | Get outright bet details |

## bets-outrights

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/bets-outrights` | competitors, athletes, competitions, lastUpdateId, lineTypeId, withProbabilityText, context, topBookmaker | Get bets outrights |

## bets-proposition

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/bets-proposition` | gameId, athleteId, topBookmakerId, fullData, topBookmaker | Get bets proposition |

## bets-raffle-bookmaker

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/bets-raffle-bookmaker` |  | Get bets raffle bookmaker |

## bets-teaser

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/bets-teaser` | gameId, topBookmaker | Get bets teaser |

## competition-brackets

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competition-brackets` | competition, competitor, live, lastUpdateId, type, topBookmaker | Get competition brackets |

## competition-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competition-details` | competition, withSeasons, withBestOdds, isDashboard, type, lastUpdateId, sport, countries, limit | Get competition details |

## competition-history

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competition-history` | competitions | Get competition history |

## competition-standings

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competition-standings` | competition, competitor, withSeasonsFilter, live, isPreview, stageNum, groupCategory, type, seasonNum, lastUpdateId, context | Get competition standings |

## competition-team-of-the-week

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competition-team-of-the-week` | competitions, weekKey | Get competition team of the week |

## competitor-current-games

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competitor-current-games` | competitorId, competitions, includeTopBettingOpportunity, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get competitor current games |

## competitor-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competitor-details` | competitorId, withSeasons, isDashboard, lastUpdateId | Get competitor details |

## competitor-recent-form

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competitor-recent-form` | competitor, numOfGames | Get competitor recent form |

## competitor-squads

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/competitor-squads` | competitorId | Get competitor squads |

## countries

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/countries` | sportId, lastUpdateId, countries | Get countries |

## custom-scores

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/custom-scores` | competitions, competitorIds, startDate, endDate, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get custom scores |

## featured-competitions

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/featured-competitions` | sport, competitions, withSeasons, type, countries, limit | Get featured competitions |

## featured-games

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/featured-games` | sport, competitions, competitors, numberOfGames, context, showOdds, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get featured games |

## fixtures

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/fixtures` | competitions, competitorIds, includeTopBettingOpportunity, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get fixtures |

## game-bet-line

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-bet-line` | games, lastUpdateId | Get game bet lines |

## game-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-details` | gameId, matchupId, lastUpdateId, topBookmaker | Get game details |

## game-highlights

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-highlights` | competitors, competitions, numberOfGames, roundKey | Get game highlights |

## game-lineups

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-lineups` | gameId, athleteId, matchWeekKey | Get game lineups |

## game-predictions

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-predictions` | sport, competitors, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get game predictions |

## game-predictions-contextual

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-predictions-contextual` | sport, games, competitions, competitors, countries, startDate, endDate, showOdds, onlyMajorGames, onlyLiveGames, numberOfGames, withLive, withTop, withSuggested, favoriteCompetitions, competitionsLimit, blackListGames, context, includeTopBettingOpportunity, topBookmaker, feedBy, onlyOnTv, roundKey, matchupId, relation, lastUpdateId | Get contextual game predictions |

## game-stats

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/game-stats` | games, onlyIsMajor, filterId, lastUpdateId | Get game statistics |

## games-scores

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/games-scores` | sport, competitions, startDate, endDate, onlyMajorGames, onlyLiveGames, withTop, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, competitors, games, relation | Get games scores |

## games-slider

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/games-slider` | sport, games, competitions, competitors, countries, startDate, endDate, showOdds, onlyMajorGames, onlyLiveGames, numberOfGames, withLive, withTop, withSuggested, favoriteCompetitions, competitionsLimit, blackListGames, context, includeTopBettingOpportunity, topBookmaker, feedBy, onlyOnTv, roundKey, matchupId, relation, lastUpdateId | Get slider games |

## games-suggestions

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/games-suggestions` | sport, games, competitions, competitors, countries, startDate, endDate, showOdds, onlyMajorGames, onlyLiveGames, numberOfGames, withLive, withTop, withSuggested, favoriteCompetitions, competitionsLimit, blackListGames, context, includeTopBettingOpportunity, topBookmaker, feedBy, onlyOnTv, roundKey, matchupId, relation, lastUpdateId | Get suggested games |

## games-top

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/games-top` | sport, games, competitions, competitors, countries, startDate, endDate, showOdds, onlyMajorGames, onlyLiveGames, numberOfGames, withLive, withTop, withSuggested, favoriteCompetitions, competitionsLimit, blackListGames, context, includeTopBettingOpportunity, topBookmaker, feedBy, onlyOnTv, roundKey, matchupId, relation, lastUpdateId | Get top games |

## h2h

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/h2h` | gameId, matchupId, addMainOdds, lastUpdateId, topBookmaker | Get head-to-head matches |

## img

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/img/flag/country/{countryId}` |  | Get country flag |
| `GET /api/allscores/img/large/athlete/{athleteId}/version/{imageVersion}` |  | Get athlete large image |
| `GET /api/allscores/img/large/competitor/{competitorId}/version/{imageVersion}` |  | Get competitor large image |
| `GET /api/allscores/img/large/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |  | Get competition large image |
| `GET /api/allscores/img/large/light/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |  | Get competition light large image |
| `GET /api/allscores/img/small/athlete/{athleteId}/version/{imageVersion}` |  | Get athlete small image |
| `GET /api/allscores/img/small/competitor/{competitorId}/version/{imageVersion}` |  | Get competitor small image |
| `GET /api/allscores/img/small/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |  | Get competition small image |
| `GET /api/allscores/img/small/light/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |  | Get competition light small image |
| `GET /api/allscores/img/trophy/{trophyId}` |  | Get trophy image |

## news

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/news` | sport, games, competitions, competitors, athletes, isPreview, countries, userCompetitions, userCompetitors | Get news |

## paging

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/paging` | paging*, publisherId, campaign, userCountryId | Get games (paging) |

## playbyplay-comments

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/playbyplay-comments` | lang, appType, fixtureid, sportifiergameid, isLive, IsFinished, onlyPreview | Get play-by-play comments |

## point-by-point

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/point-by-point` | gameId | Get point by point |

## related-entities

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/related-entities` | competitors, competitions, athletes | Get related entities |

## results

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/results` | competitions, competitorIds, includeTopBettingOpportunity, lastUpdateId, countries, favoriteCompetitions, competitionsLimit, withLive, withSuggested, blackListGames, topBookmaker, feedBy, onlyOnTv, roundKey, games, relation | Get results |

## search

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/search` | query, filter, sport | Search |

## sports

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/sports` | withCount, lastUpdateId | Get sports |

## stats

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/stats` | competitorId, competition, phaseNum, withSeasons | Get stats |

## stats-pregame

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/stats-pregame` | game, onlyMajor | Get pre-game stats |

## top-athletes

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/top-athletes` | sportType, limit | Get top athletes |

## top-competitions

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/top-competitions` | sport, limit, countries | Get top competitions |

## top-competitors

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/top-competitors` | sport, withSeasons, limit, isDashboard, promoteNational | Get top competitors |

## transfers

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/transfers` | competitions, competitors, onlyConfirmed, lastUpdateId, limit, lastTransferId | Get transfers |

## trend-details

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/trend-details` | trendId, topBookmaker, lastUpdateId | Get trend details |

## trends

| Path | Query | Comment |
|------|-------|---------|
| `GET /api/allscores/trends` | games, competition, sportType, date, isTop, lastUpdateId, competitor, matchupId, numOfGames, context, topBookmaker | Get trends |
