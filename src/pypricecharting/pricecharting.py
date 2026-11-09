import logging
import os
from types import TracebackType
from typing import Self

from httpx2 import Client
from pydantic import SecretStr

from pypricecharting._auth import _REDACT_FILTER, _TokenAuth


class PriceCharting:
    """Synchronous PriceCharting API client."""

    TOKEN_KEY = "PRICECHARTING_TOKEN"

    def __init__(self, token: str | None = None):
        """Create a client authenticated with a PriceCharting API token.

        The client adds a logging filter to the `httpx2` logger that replaces the token in
        request URLs with `REDACTED`.

        Args:
            token: The 40-character PriceCharting API token. If omitted, it is read from the
                `PRICECHARTING_TOKEN` environment variable.

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
        self.client = Client(auth=_TokenAuth(self._token))
        logging.getLogger("httpx2").addFilter(_REDACT_FILTER)

    def close(self):
        """Close the underlying HTTP client."""
        self.client.close()

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

    def product(self):
        """Get a single product."""
        pass

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
