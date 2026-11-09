# PyPriceCharting

Python client for the [PriceCharting API](https://www.pricecharting.com/api-documentation).

The package provides a synchronous client, `PriceCharting`, and an asynchronous client,
`AsyncPriceCharting`. Both authenticate with a 40-character PriceCharting API token.

The client is under development: the clients can be created and used as context managers, but
their API methods are not implemented yet.

## Authentication

Set your token in the `PRICECHARTING_TOKEN` environment variable and create a client without
arguments:

```python
from pypricecharting import PriceCharting

with PriceCharting() as client:
    ...
```

You can also pass the token directly:

```python
with PriceCharting("your-40-character-token") as client:
    ...
```

The environment variable is recommended, because it keeps the token out of your code. Both
clients raise `ValueError` if no token is found or the token is not 40 characters.

## Security

The PriceCharting API requires the token in the query string of `GET` requests, so it is part of
the request URL. The clients redact it from the `httpx2` request log, which shows `t=REDACTED`
instead. Anything outside this library that records URLs can still see the token, such as
proxies or your own logging of requests.

See the [API Reference](api/clients.md) for the classes and types in the package.
