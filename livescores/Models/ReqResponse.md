# ReqResponse

A **ReqResponse** is a navigation payload. The records use the same `fields` object as a [FeedResponse](FeedResponse.md).

**Where you'll see it:** `/req/{req}`.

### Example

```json
{
  "req": "m_1_17",
  "header": {},
  "records": [
    { "fields": { "sharedindexes_event_id": "08W6fzLP" } }
  ]
}
```

## Properties

- **req** (`string`):
    - The `req` id you sent.

- **header** (`object`):
    - Decoded header fields.

- **records** (`array of FeedRecord`):
    - Rows. See [FeedResponse](FeedResponse.md) for `fields`.
