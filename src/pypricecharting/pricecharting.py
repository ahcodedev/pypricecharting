import logging
import os
from types import TracebackType
from typing import Self

from httpx2 import BaseTransport, Client
from pydantic import SecretStr

from pypricecharting._auth import _REDACT_FILTER, _TokenAuth
from pypricecharting.error import ParameterError
from pypricecharting.responses import ProductResponse, _parse
from pypricecharting.route import BASE_URL, Prices


class PriceCharting:
    """Synchronous PriceCharting API client."""

    TOKEN_KEY = "PRICECHARTING_TOKEN"

    def __init__(
        self,
        token: str | None = None,
        base_url: str = BASE_URL,
        transport: BaseTransport | None = None,
    ):
        """Create a client authenticated with a PriceCharting API token.

        The client adds a logging filter to the `httpx2` logger that replaces the token in
        request URLs with `REDACTED`.

        Args:
            token: The 40-character PriceCharting API token. If omitted, it is read from the
                `PRICECHARTING_TOKEN` environment variable.
            base_url: The API base URL. Defaults to `route.BASE_URL`. Override it to send
                requests to another server, such as a mock server in tests.
            transport: The `httpx2` transport that sends requests, such as
                `httpx2.MockTransport` in tests. If omitted, the default `httpx2` transport is
                used.

        Raises:
            ValueError: If no token is passed or set in the environment, or the token is not
                40 characters.

        """
        if token is not None and len(token) != 40:
            raise ValueError("PriceCharting API token is not 40 characters")

        token = token or os.environ.get(self.TOKEN_KEY)

        if token is None:
            raise ValueError("PriceCharting API token not found")
        elif len(token) != 40:
            raise ValueError("PriceCharting API token is not 40 characters")

        self._token = SecretStr(token)
        self._client = Client(base_url=base_url, auth=_TokenAuth(self._token), transport=transport)
        logging.getLogger("httpx2").addFilter(_REDACT_FILTER)

    def close(self):
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> Self:
        """Enter the context and return the client."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Close the underlying HTTP client on exit."""
        self.close()

    def product(
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

        response = self._client.get(Prices.PRODUCT.value, params=params)
        return _parse(response, ProductResponse)

    def products(self):
        """Search for products."""
        pass

    def offers(self):
        """List marketplace offers."""
        pass

    def offer_details(self):
        """Get the details of a marketplace offer."""
        pass

    def offer_publish(self):
        """Publish a new marketplace offer."""
        pass

    def offer_feedback(self):
        """Leave feedback on a marketplace offer."""
        pass

    def offer_ship(self):
        """Mark a marketplace offer as shipped."""
        pass

    def offer_end(self):
        """End a marketplace offer."""
        pass

    def offer_refund(self):
        """Refund a marketplace offer."""
        pass
