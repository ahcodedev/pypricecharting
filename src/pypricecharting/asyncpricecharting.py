from types import TracebackType
from typing import Self

from httpx2 import AsyncClient


class AsyncPriceCharting:
    """Asynchronous PriceCharting API client."""

    def __init__(self, credential: str):
        """Create a client authenticated with a PriceCharting API token."""
        self.credential = credential
        self.client = AsyncClient()

    async def aclose(self):
        """Close the underlying HTTP client."""
        await self.client.aclose()

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

    async def product(self):
        """Get a single product."""
        pass

    async def products(self):
        """Search for products."""
        pass

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
