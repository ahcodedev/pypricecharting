import logging
import os
from types import TracebackType
from typing import Self

from httpx2 import BaseTransport, Client
from pydantic import SecretStr

from pypricecharting._auth import _REDACT_FILTER, _TokenAuth
from pypricecharting.error import ParameterError
from pypricecharting.requests import OffersRequestParams
from pypricecharting.responses import (
    OfferDetailsResponse,
    OffersResponse,
    ProductResponse,
    ProductsResponse,
    _parse,
)
from pypricecharting.route import BASE_URL, Route


class PriceCharting:
    """Synchronous PriceCharting API client.

    Reuse one client for all requests and close it when done (`with` or `close()`). The Marketplace
    methods other than `offers` and `offer_details` are not implemented yet and return `None`.
    """

    TOKEN_KEY = "PRICECHARTING_TOKEN"
    """Environment variable the token is read from when none is passed."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = BASE_URL,
        transport: BaseTransport | None = None,
    ):
        """Create a client authenticated with a PriceCharting API token.

        The token is redacted from `httpx2` request logs.

        Args:
            token: The 40-character PriceCharting API token. If omitted, it is read from the
                `PRICECHARTING_TOKEN` environment variable.
            base_url: API base URL. Override it to use a mock server.
            transport: Custom `httpx2` transport, such as `httpx2.MockTransport` in tests.

        Raises:
            ValueError: If the token is missing or not 40 characters.

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

        response = self._client.get(Route.Prices.PRODUCT, params=params)
        return _parse(response, ProductResponse)

    def products(self, q: str) -> ProductsResponse:
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

        response = self._client.get(Route.Prices.PRODUCTS, params={"q": q})
        return _parse(response, ProductsResponse)

    def offers(self, params: OffersRequestParams) -> OffersResponse:
        """List marketplace offers matching the given filters.

        The same request can be made at most once every 5 minutes.

        Args:
            params: Offer filters. Only `status` is required.

        Returns:
            The matching offers.

        Raises:
            APIError: If the API returns an error.

        """
        response = self._client.get(
            Route.Marketplace.OFFERS,
            params=params.model_dump(mode="json", by_alias=True, exclude_none=True),
        )
        return _parse(response, OffersResponse)

    def offer_details(self, offer_id: str) -> OfferDetailsResponse:
        """Get the full details of one marketplace offer.

        Args:
            offer_id: The offer ID. Surrounding whitespace is stripped.

        Returns:
            The offer, including the buyer's shipping details once it has sold.

        Raises:
            ParameterError: If `offer_id` is empty or only whitespace.
            APIError: If the API returns an error.

        """
        offer_id = offer_id.strip()

        if len(offer_id) == 0:
            raise ParameterError("Invalid parameter; offer_id was empty.")

        response = self._client.get(Route.Marketplace.OFFER_DETAILS, params={"offer-id": offer_id})
        return _parse(response, OfferDetailsResponse)

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
