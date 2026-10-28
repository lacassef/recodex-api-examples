# PlayByPlay

**PlayByPlay** is the commentary body.

**Where you'll see it:** `/playbyplay-comments`.

**Related models:** none on this page. The route does not take `langId`, `timezone`, `publisherId`, `campaign`, or `userCountryId`. `lang` is the numeric language id. `fixtureid` is the provider fixture key. `sportifiergameid` is the game id. `4669892` is that game id in the [examples](../guides/examples.md). `IsFinished` keeps that capitalization.

This page does not name the keys inside `Messages`.

### Example

`UpdateURL` and `TTL` are shape. Do not call a URL from this example.

```json
{
  "Messages": [],
  "UpdateURL": "",
  "TTL": 0
}
```

## Properties

- **Messages** (`array`):
    - Commentary messages.

- **UpdateURL** (`string`):
    - URL the body returns for the next update.

- **TTL** (`number`):
    - How long this body stays current.
