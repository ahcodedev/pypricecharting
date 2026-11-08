import pytest
from httpx2 import AsyncClient

from pypricecharting.asyncpricecharting import AsyncPyPriceCharting

# Template tests: the API methods are placeholders, so these only check they can be called.
# Replace the `is None` assertions once each method is implemented.

TOKEN = "test-token"


async def test_init_stores_credential():
    client = AsyncPyPriceCharting(TOKEN)
    assert client.credential == TOKEN
    await client.aclose()


async def test_init_creates_http_client():
    client = AsyncPyPriceCharting(TOKEN)
    assert isinstance(client.client, AsyncClient)
    assert not client.client.is_closed
    await client.aclose()


async def test_aclose_closes_http_client():
    client = AsyncPyPriceCharting(TOKEN)
    await client.aclose()
    assert client.client.is_closed


async def test_async_with_returns_client():
    client = AsyncPyPriceCharting(TOKEN)
    async with client as entered:
        assert entered is client
        assert not client.client.is_closed


async def test_async_with_closes_http_client():
    async with AsyncPyPriceCharting(TOKEN) as client:
        pass
    assert client.client.is_closed


async def test_async_with_closes_http_client_on_error():
    client = AsyncPyPriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"):
        async with client:
            raise ValueError("boom")
    assert client.client.is_closed


async def test_product():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.product() is None
    await client.aclose()


async def test_products():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.products() is None
    await client.aclose()


async def test_offers():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offers() is None
    await client.aclose()


async def test_offer_details():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_details() is None
    await client.aclose()


async def test_offer_publish():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_publish() is None
    await client.aclose()


async def test_offer_feedback():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_feedback() is None
    await client.aclose()


async def test_offer_ship():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_ship() is None
    await client.aclose()


async def test_offer_end():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_end() is None
    await client.aclose()


async def test_offer_refund():
    client = AsyncPyPriceCharting(TOKEN)
    assert await client.offer_refund() is None
    await client.aclose()
