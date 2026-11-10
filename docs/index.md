# PyPriceCharting

Python client for the [PriceCharting API](https://www.pricecharting.com/api-documentation).

It provides a synchronous client, `PriceCharting`, and an asynchronous client,
`AsyncPriceCharting`, both authenticated with a 40-character API token.

Under development: the Prices API methods (`product`, `products`) and the Marketplace `offers`
method are implemented; the other Marketplace API methods are not yet.

## Authentication

Set the token in the `PRICECHARTING_TOKEN` environment variable and create a client without
arguments:

```python
from pypricecharting import PriceCharting

with PriceCharting() as client:
    ...
```

Or pass the token directly:

```python
with PriceCharting("your-40-character-token") as client:
    ...
```

Prefer the environment variable, which keeps the token out of your code. Both clients raise
`ValueError` if the token is missing or not 40 characters.

Reuse one client for all requests, and close it when done: with a `with` block, or by calling
`close()` (`aclose()` for the async client).

## Getting a product

`product` looks up a product by exactly one of `id` (PriceCharting product ID), `upc` (UPC
barcode), or `q` (full text search, best match only):

```python
from pypricecharting import AsyncPriceCharting, PriceCharting

with PriceCharting() as client:
    game = client.product(id="6910")
    print(game.product_name, game.cib_price)  # EarthBound 42995

async with AsyncPriceCharting() as client:
    game = await client.product(upc="045496830434")
```

Prices are integer pennies: `42995` is $429.95.

## Searching products

`products` runs a full text search on title and/or console and returns up to 20 matches as
`ProductSummary` objects. Pass a result's `id` to `product` for prices:

```python
with PriceCharting() as client:
    results = client.products("chrono trigger super nintendo")
    for summary in results.products:
        print(summary.id, summary.product_name, summary.console_name)
```

An empty or whitespace-only query raises `ParameterError`.

## Listing offers

`offers` lists marketplace offers. It takes an `OffersRequestParams`; only `status` is required,
and the other fields narrow the results:

```python
from pypricecharting import Console, OffersRequestParams, OffersSort, OffersStatus, PriceCharting

with PriceCharting() as client:
    params = OffersRequestParams(
        status=OffersStatus.AVAILABLE, console=Console.NES, sort=OffersSort.LOWEST_PRICE
    )
    for offer in client.offers(params).offers:
        print(offer.offer_id, offer.product_name, offer.price)
```

The API allows the same `offers` request at most once every 5 minutes.

## Errors

All errors subclass `PriceChartingError`:

- `ParameterError` (also a `ValueError`): invalid method arguments, raised before any request is
  sent.
- `APIError`: the API returned an error. Has `message` and `status_code`.

```python
from pypricecharting import APIError

try:
    game = client.product(id="0")
except APIError as error:
    print(error.status_code, error.message)
```

## Client options

Both clients take two optional arguments, mainly for testing:

- `base_url`: send requests to another server, such as a local mock server.
- `transport`: a custom `httpx2` transport, such as `httpx2.MockTransport`.

```python
from httpx2 import MockTransport, Response

client = PriceCharting(
    base_url="http://localhost:8080",
    transport=MockTransport(lambda request: Response(200, json={"status": "success"})),
)
```

## Imports

Everything public, including the clients, errors, models, and enums, can be imported from
`pypricecharting` or from its own module (such as `pypricecharting.responses`):

```python
from pypricecharting import Condition, PriceCharting, ProductResponse
```

## Security

The API requires the token in the query string of `GET` requests. The clients redact it from the
`httpx2` request log (`t=REDACTED`), but anything else that records URLs, such as proxies or your
own request logging, can still see it.

See the [API Reference](api/clients.md) for all classes and types.
