# BestOdds

**BestOdds** is the best available line for the requested games, or for a competition window.

**Where you'll see it:** the best-odds route. Game bet lines are a separate route and do not use this shape.

**Related models:** [Outright](Outright.md), [Trend](Trend.md), [ScoresList](ScoresList.md).

`bookmakers` can be empty on a teaser or a raffle, and the status can still be HTTP `200`. This page does not name the keys inside a bookmaker.

## Properties

- **lines** (`array`):
    - The lines.

- **lineTypes** (`array`):
    - Line types for those lines.

- **bookmakers** (`array`):
    - Bookmakers for those lines. The array can be empty.

- **games** (`array`):
    - Games those lines belong to.
