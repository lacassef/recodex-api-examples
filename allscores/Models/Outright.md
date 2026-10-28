# Outright

An **Outright** is one futures line.

**Where you'll see it:** outright details. The list route returns an empty object and HTTP `200` when the entity has no market.

**Related models:** [Competitor](Competitor.md), [Competition](Competition.md), [Athlete](Athlete.md). Send `lineId` to the details route.

`entityType` `4` on the details route is the competitor. An unknown `lineId` returns those ids as `0` and empty sports and countries.

### Example

The guides do not publish a `lineId`. `4` is the competitor entity type.

```json
{
  "entityType": 4,
  "name": "",
  "marketTitle": ""
}
```

## Properties

- **name** (`string`):
    - Line name.

- **marketTitle** (`string`):
    - Market title.

- **entityType** (`number`):
    - Kind of entity. `4` is the competitor.

- **entityId** (`number`):
    - Id of that entity.

- **lineTypeId** (`number`):
    - Line type.

- **lineId** (`number`):
    - Line id. Send it to outright details.

- **bookmakerId** (`number`):
    - Bookmaker for this price.

- **odds** (`value`):
    - The price. The description does not pick a JSON type.

- **winningChancesText** (`string`):
    - Present when the market has it.
