# Search

**Search** returns three lists plus the sports and countries that label them.

**Where you'll see it:** the search route. `filter=all` returns every result type. `raphinha` with `sport` `1` is the query in the [examples](../guides/examples.md).

**Related models:** [Competition](Competition.md), [Competitor](Competitor.md), [Athlete](Athlete.md), [Sport](Sport.md), [Country](Country.md).

Read `id` from the list you open next. Which parameter name that id uses is in [Parameters](../guides/request-essentials.md). This page does not add keys beyond those objects.

## Properties

- **competitions** (`array of Competition`):
    - Matching competitions.

- **competitors** (`array of Competitor`):
    - Matching competitors.

- **athletes** (`array of Athlete`):
    - Matching athletes.

- **sports** (`array of Sport`):
    - Sports for those rows.

- **countries** (`array of Country`):
    - Countries for those rows.
