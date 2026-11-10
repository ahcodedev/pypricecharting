import logging
import os
from types import TracebackType
from typing import Self

from httpx2 import AsyncBaseTransport, AsyncClient
from pydantic import SecretStr

from pypricecharting._auth import _REDACT_FILTER, _TokenAuth
from pypricecharting.error import ParameterError
from pypricecharting.responses import ProductResponse, ProductsResponse, _parse
from pypricecharting.route import BASE_URL, Route


class AsyncPriceCharting:
    """Asynchronous PriceCharting API client.

    Reuse one client for all requests and close it when done (`async with` or `aclose()`). The Marketplace API
    methods are not implemented yet and return `None`.
    """

    TOKEN_KEY = "PRICECHARTING_TOKEN"
    """Environment variable the token is read from when none is passed."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = BASE_URL,
        transport: AsyncBaseTransport | None = None,
    ):
        """Create a client authenticated with a PriceCharting API token.

        The token is redacted from `httpx2` request logs.

        Args:
            token: The 40-character PriceCharting API token. If omitted, it is read from the
                `PRICECHARTING_TOKEN` environment variable.
            base_url: API base URL. Override it to use a mock server.
            transport: Custom `httpx2` async transport, such as `httpx2.MockTransport` in tests.

        Raises:
            ValueError: If the token is missing or not 40 characters.

        """
        if token is not None and len(token) != 40:
            raise ValueError("PriceCharting API token is not 40 characters")
        token = token or os.environ.get(self.TOKEN_KEY)

        if token is None:
            raise ValueError("PriceCharting API token not found")
        if len(token) != 40:
            raise ValueError("PriceCharting API token is not 40 characters")

        self._token = SecretStr(token)
        self._client = AsyncClient(
            base_url=base_url, auth=_TokenAuth(self._token), transport=transport
        )
        logging.getLogger("httpx2").addFilter(_REDACT_FILTER)

    async def aclose(self):
        """Close the underlying HTTP client."""
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        """Enter the async context and return the client."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Close the underlying HTTP client on exit."""
        await self.aclose()

    async def product(
        self, id: str | None = None, upc: str | None = None, q: str | None = None
    ) -> ProductResponse:
        """Get a single product by exactly one of `id`, `upc`, or `q`.

        Args:
            id: PriceCharting product ID.
            upc: UPC barcode.
            q: Full text search on title and/or console. Only the best match is returned.

        Returns:
            The matching product.

        Raises:
            ParameterError: If not exactly one of `id`, `upc`, or `q` is given.
            APIError: If the API returns an error.

        """
        params = {
            key: value for key, value in {"id": id, "upc": upc, "q": q}.items() if value is not None
        }

        if len(params) == 0:
            raise ParameterError("Invalid parameters. Either id, upc, or q are required.")
        if len(params) > 1:
            raise ParameterError("Invalid parameters. Only one of id, upc, or q is allowed.")

        response = await self._client.get(Route.Prices.PRODUCT, params=params)
        return _parse(response, ProductResponse)

    async def products(self, q: str) -> ProductsResponse:
        """Search for products by title and/or console.

        Args:
            q: Full text search on title and/or console. Surrounding whitespace is stripped.

        Returns:
            Up to 20 matching products.

        Raises:
            ParameterError: If `q` is empty or only whitespace.
            APIError: If the API returns an error.

        """
        q = q.strip()

        if len(q) == 0:
            raise ParameterError("Invalid parameter; Query string q was empty.")

        response = await self._client.get(Route.Prices.PRODUCTS, params={"q": q})
        return _parse(response, ProductsResponse)

    async def offers(self):
        """List marketplace offers."""
        pass

    async def offer_details(self):
        """Get the details of a marketplace offer."""
        pass

    async def offer_publish(self):
        """Publish a new marketplace offer."""
        pass

    async def offer_feedback(self):
        """Leave feedback on a marketplace offer."""
        pass

    async def offer_ship(self):
        """Mark a marketplace offer as shipped."""
        pass

    async def offer_end(self):
        """End a marketplace offer."""
        pass

    async def offer_refund(self):
        """Refund a marketplace offer."""
        pass
