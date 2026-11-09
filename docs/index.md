# PyPriceCharting

Python client for the [PriceCharting API](https://www.pricecharting.com/api-documentation).

The package provides a synchronous client, `PriceCharting`, and an asynchronous client,
`AsyncPriceCharting`. Both authenticate with a 40-character PriceCharting API token.

The client is under development: `product` is implemented on both clients, and the other API
methods are not implemented yet.

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

## Getting a product

`product` looks up a single product by exactly one of `id` (PriceCharting product ID), `upc`
(UPC barcode), or `q` (full text search, best match only):

```python
from pypricecharting import AsyncPriceCharting, PriceCharting

with PriceCharting() as client:
    game = client.product(id="6910")
    print(game.product_name, game.cib_price)  # EarthBound 42995

async with AsyncPriceCharting() as client:
    game = await client.product(upc="045496830434")
```

Prices are integer pennies, so `42995` is $429.95.

Create one client and reuse it for all your requests, so they share a connection pool. Close it
when you are done, either with a `with` block or by calling `close()` (`aclose()` for the async
client).

## Errors

All errors subclass `PriceChartingError` and can be imported from `pypricecharting`:

- `ParameterError` (also a `ValueError`) is raised before any request is sent when a method gets
  invalid parameters, such as `product()` with none or more than one of `id`, `upc`, and `q`.
- `APIError` is raised when the API returns an error. It has the API's `message` and the HTTP
  `status_code`.

```python
from pypricecharting import APIError

try:
    game = client.product(id="0")
except APIError as error:
    print(error.status_code, error.message)
```

## Client options

Both clients accept two optional arguments, mainly for testing:

- `base_url` sends requests to another server, such as a local mock server. It defaults to
  `https://www.pricecharting.com`.
- `transport` replaces the `httpx2` transport that sends requests, such as
  `httpx2.MockTransport`.

```python
from httpx2 import MockTransport, Response

client = PriceCharting(
    base_url="http://localhost:8080",
    transport=MockTransport(lambda request: Response(200, json={"status": "success"})),
)
```

## Imports

Everything public can be imported from `pypricecharting` directly: the clients, the errors, the
request and response models, the shared models (`ProductSummary`, `Offer`, `Buyer`), and the enums
in `types` (`Condition`, `Console`, `Genre`, `Status`, and others):

```python
from pypricecharting import Condition, PriceCharting, ProductResponse
```

They can also be imported from their own modules, such as `pypricecharting.responses`.

## Security

The PriceCharting API requires the token in the query string of `GET` requests, so it is part of
the request URL. The clients redact it from the `httpx2` request log, which shows `t=REDACTED`
instead. Anything outside this library that records URLs can still see the token, such as
proxies or your own logging of requests.

See the [API Reference](api/clients.md) for the classes and types in the package.
