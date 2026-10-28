# Career

**Career** is the career tables for one athlete, and the trophy table is the same family of object.

**Where you'll see it:** `stats` on athlete career and on athlete trophy stats. `40557` is the career athlete id in the [examples](../guides/examples.md). `seasonKey` `-1` is every season. Trophy stats in the examples use athlete `817` and competition `7016`.

**Related models:** [Athlete](Athlete.md), [SeasonStats](SeasonStats.md).

Career `stats` has categories, tables, and a legend. Rows are competitions. `summary` is the career total.

Trophy `stats` is a table with columns, rows, and the competitor that row belongs to. This page does not name a key for that competitor.

## Properties

- **stats.categories** (`array`):
    - Category groups on a career. The key path is `categories` on `stats`.

- **stats.tables** (`array`):
    - Tables on a career.

- **stats.legend** (`value`):
    - Legend for the career tables.

- **summary** (`value`):
    - Career total.

- **columns** (`array`):
    - Columns on a trophy table.

- **rows** (`array`):
    - Rows on a trophy table.
