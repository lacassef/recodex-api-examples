# Paging

A **Paging** object is the cursor pair on fixtures and results.

**Where you'll see it:** `paging` on a [ScoresList](ScoresList.md) from fixtures or results. The next call is `GET /api/allscores/paging`.

**Related models:** [ScoresList](ScoresList.md).

Pass `nextPage` or `previousPage` unchanged as the `paging` parameter. Do not rebuild the string. That route does not take `langId` or `timezone`. It still accepts `publisherId`, `campaign`, and `userCountryId`.

### Example

The strings below are shape. A real cursor is the value you just received.

```json
{
  "nextPage": "",
  "previousPage": ""
}
```

## Properties

- **nextPage** (`string`):
    - Cursor for the next page.

- **previousPage** (`string`):
    - Cursor for the previous page.
