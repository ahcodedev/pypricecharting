from httpx2 import MockTransport, Request, Response

from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.pricecharting import PriceCharting

TOKEN = "test-token-12345678901234567890123456789"
"""A fake 40-character API token for tests."""


def mocked_client(token: str | None, response: Response, requests: list[Request]) -> PriceCharting:
    """Create a `PriceCharting` client that records requests and returns `response`."""

    def handler(request: Request) -> Response:
        requests.append(request)
        return response

    return PriceCharting(token=token, transport=MockTransport(handler))


def mocked_async_client(
    token: str | None, response: Response, requests: list[Request]
) -> AsyncPriceCharting:
    """Create an `AsyncPriceCharting` client that records requests and returns `response`."""

    def handler(request: Request) -> Response:
        requests.append(request)
        return response

    return AsyncPriceCharting(token=token, transport=MockTransport(handler))
