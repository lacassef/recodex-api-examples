# ErrorResponse

The error body on `400`, `500`, `502`, `503`, and `504`. A `400` has `title` `Bad Request` and does not name the parameter.

**Where you'll see it:** any route that rejects the query or cannot return a payload.

**Related models:** none. A `204` and a `200` with an empty object are not this shape. See [README](README.md).

### Example

`request_id` here is shape, not a captured id.

```json
{
  "error": {
    "status": 400,
    "title": "Bad Request",
    "request_id": "req_example"
  }
}
```

## Properties

- **error** (`object`):
    - The error object.

- **error.status** (`number`):
    - The HTTP status.

- **error.title** (`string`):
    - A short title, such as `Bad Request`.

- **error.request_id** (`string`):
    - The id for this request.
