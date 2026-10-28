# EventStatisticsPeriod

An **EventStatisticsPeriod** holds the statistics for one slice of a match — typically
`"ALL"` (whole match) plus per‑period entries such as `"1st half"` / `"2nd half"` or
quarters. It is one element of [EventStatistics](EventStatistics.md)`.statistics` and
contains the named [groups](EventStatisticsGroup.md) of stat rows for that period.

**Related models:** [EventStatistics](EventStatistics.md) ·
[EventStatisticsGroup](EventStatisticsGroup.md) ·
[EventStatisticsItem](EventStatisticsItem.md).

## Properties

- **groups** (`array of EventStatisticsGroup`):
    - A list of statistical groups for the period, with each entry being an instance of `EventStatisticsGroup`. This list contains various statistical metrics or categories relevant to the period.

- **period** (`string`):
    - A string representing the name or identifier of the period, such as "First Half," "Quarter 1," or "Second Period."