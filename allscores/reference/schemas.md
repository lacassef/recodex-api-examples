# Schemas

The body is JSON except the image routes, which are `image/png`. Field names below are the ones the route descriptions name. A list route also returns the sports, countries, competitions, and competitors needed to label the rows.

## Polling

`lastUpdateId`, `requestedUpdateId`, and `ttl` come back on the catalog and score routes. The next call sends the `lastUpdateId` you just received. Omit it for a full response.

## Paging

Fixtures and results include `paging.nextPage` and `paging.previousPage`. Pass that string unchanged as `paging` on `/paging`.

## Games

A scores list has `games` with status, start time, and home and away scores, plus `summary`. Odds are present when the route accepts `showOdds` and you set it. Read the game id from `games` and send it as `gameId`, or as `games` when the next route asks for a list.

`matchupId` is `homeId-awayId-competitionId` on the routes that list that parameter.

## Competitions and competitors

A competition has `id`, `name`, `countryId`, `sportId`, `currentSeasonNum`, `currentStageNum`, and flags such as `hasStandings`, `hasBrackets`, `hasStats`, `hasTransfers`, and `hasBets`. `withSeasons` adds `seasons`.

A competitor has `id`, `name`, `longName`, `symbolicName`, `countryId`, `sportId`, `imageVersion`, and `mainCompetitionId`.

Standings include `displayName`, groups, columns, rows, destinations, `filterTypes`, and `competitionRules`.

## Athletes

Without `fullDetails`, an athlete has age, position, club, and nationality. `fullDetails=true` adds jersey, contract, injury, `shortBio`, `highlightStats`, `lastMatches`, transfers, trophies, and `careerStats`.

Career `stats` has categories, tables, and a legend. Trophy `stats` is a table with columns and rows.

## News and search

A news card has `id`, `title`, `publishDate`, `image`, `url`, `sourceId`, and `isMagazine`. The body also has `newsSources`.

Search returns competitions, competitors, and athletes, plus the sports and countries that label them.

## Bets

A trend has `id`, `text`, `betCTA`, `divId`, `lineTypeTitle`, and `gameId`. Send `trend.id` as `trendId`.

An outright line has `lineId`, `lineTypeId`, `bookmakerId`, and `odds`. Send `lineId` to outright details. `entityType` `4` on that details route is the competitor.

Best odds returns `lines`, `lineTypes`, `bookmakers`, and the games those lines belong to.

## Commentary

Play-by-play returns `Messages`, `UpdateURL`, and `TTL`.
