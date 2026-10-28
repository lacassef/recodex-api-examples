# Languages and enums

Send the parameter name the operation lists. `lang` on play-by-play is the numeric language id. The other JSON routes use `langId`.

## langId

| Id | Language |
| --- | --- |
| 1 | English |
| 2 | Hebrew |
| 9 | English (US) |
| 10 | English (UK) |
| 12 | Italian |
| 14 | Spanish |
| 15 | French |
| 16 | German |
| 21 | Russian |
| 27 | Arabic |
| 29 | Spanish (Latin America) |
| 30 | Portuguese (Portugal) |
| 31 | Portuguese (Brazil) |
| 33 | Turkish |
| 34 | Indonesian |
| 35 | Polish |
| 37 | Dutch |
| 42 | Danish |
| 57 | Japanese |
| 88 | Thai |
| 141 | Chinese (simplified) |
| 158 | Persian |
| 193 | German (Austria) |
| 194 | Finnish |
| 195 | Norwegian |
| 196 | Malay |
| 197 | Dutch (Belgium) |
| 198 | Swedish |
| 199 | Chinese (Taiwan) |
| 209 | Filipino |
| 210 | Vietnamese |
| 216 | Hindi |
| 217 | Lao |
| 219 | Burmese |

Omit `langId` for the default language.

## Dates

Send the date string in the locale short pattern. An example value is `30/09/2026`.

| Locale | Pattern |
| --- | --- |
| pt-br | dd/MM/yyyy |
| pt-pt | dd-MM-yyyy |
| en-us | M/d/yyyy |
| en-gb | dd/MM/yyyy |
| ar | dd/MM/yy |

`startDate`, `endDate`, and `date` take that string.

## context

`1` home, `2` my scores, `3` competition page, `4` team page. Omit `context` when you do not want a placement.

## statusGroup

`1` anticipated, `2` scheduled, `3` started, `4` ended. Football postponed is `5`. Football cancelled is `119`.

## gameTimeAndStatusDisplayType

`0` none, `1` status text, `2` game time, `3` both.

## Competitor kind

`1` team, `2` national team, `4` athlete, `8` double.

## Odds

Trend: `1` down, `2` even, `3` up. Bet result: `1` win, `2` lose, `3` void.

Analytics entity type: `1` competition, `2` competitor, `3` sport, `4` game, `5` athlete.

Betting entity type: `2` competition, `4` competitor, `6` athlete. On outright details, `entityType` `4` is the competitor.

## Events

`1` goal, `2` yellow card, `3` red card, `6` penalty miss, `1000` substitution.

## relation

`or` or `and`. Send it when you want that combination.

## Catalog type

On featured competitions and competition details, `type` is empty, `stats`, or `standings`.

On competition standings, `type` is the table layout. Example values are `1` and `6`.
