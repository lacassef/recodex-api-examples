# ErrorResponse

The error body on `400`, `502`, `503`, and `504`. A `400` has `title` `Bad Request` and does not name the parameter.

A `400` whose body is the string `invalid parameters` is not this object. That string names `filter_since=0`, `filter_until=0`, or `page_number=0`. Omit those parameters instead of sending `0`.

**Where you'll see it:** any route that rejects the query or cannot return a payload.

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
