# Images

`GET` routes. The response is `image/png`. Path parameters are required. `imageVersion` comes from the country, sport, competitor, or athlete you already loaded. Filled calls are in [Examples](../guides/examples.md).

| Route | Size | Path |
| --- | --- | --- |
| Athlete, small | 40x40 | `/api/allscores/img/small/athlete/{athleteId}/version/{imageVersion}` |
| Athlete, large | 84x84 | `/api/allscores/img/large/athlete/{athleteId}/version/{imageVersion}` |
| Competitor, small | 34x34 | `/api/allscores/img/small/competitor/{competitorId}/version/{imageVersion}` |
| Competitor, large | 64x64 | `/api/allscores/img/large/competitor/{competitorId}/version/{imageVersion}` |
| Competition, small | 20x20 | `/api/allscores/img/small/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |
| Competition, large | 68x68 | `/api/allscores/img/large/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |
| Competition logo, small | 24x24 | `/api/allscores/img/small/light/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |
| Competition logo, large | 40x40 | `/api/allscores/img/large/light/country/{countryId}/competition/{competitionId}/version/{imageVersion}` |
| Flag | 20x20 | `/api/allscores/img/flag/country/{countryId}` |
| Trophy | 40x40 | `/api/allscores/img/trophy/{trophyId}` |

The flag and the trophy have no image version. On a competition image, `countryId` is the fallback flag. The light routes are the logo used in lists.
