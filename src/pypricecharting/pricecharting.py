from types import TracebackType
from typing import Self

from httpx2 import Client


class PriceCharting:
    """Synchronous PriceCharting API client."""

    def __init__(self, credential: str):
        """Create a client authenticated with a PriceCharting API token."""
        self.credential = credential
        self.client = Client()

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
