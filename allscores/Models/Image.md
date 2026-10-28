# Image

An **Image** response is `image/png`. There is no JSON body.

**Where you'll see it:** the `/img/...` routes. Path parameters are required. `imageVersion` comes from the [Country](Country.md), [Sport](Sport.md), [Competitor](Competitor.md), or [Athlete](Athlete.md) you already loaded.

The flag and the trophy have no image version. On a competition image, `countryId` is the fallback flag. The light routes are the logo used in lists.

| Route | Size |
| --- | --- |
| Athlete, small | 40x40 |
| Athlete, large | 84x84 |
| Competitor, small | 34x34 |
| Competitor, large | 64x64 |
| Competition, small | 20x20 |
| Competition, large | 68x68 |
| Competition logo, small | 24x24 |
| Competition logo, large | 40x40 |
| Flag | 20x20 |
| Trophy | 40x40 |

`48583` with `imageVersion` `3` is the athlete photo in the [examples](../guides/examples.md). `5930` with country `54` and `imageVersion` `19` is the competition logo there. The trophy id in the examples is `5069`.
