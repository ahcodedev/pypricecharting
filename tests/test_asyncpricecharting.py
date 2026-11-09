import pytest
from httpx2 import AsyncClient

from pypricecharting.asyncpricecharting import AsyncPriceCharting

# Template tests: the API methods are placeholders, so these only check they can be called.
# Replace the `is None` assertions once each method is implemented.

TOKEN = "test-token-12345678901234567890123456789"


def test_token_constant():
    assert AsyncPriceCharting.TOKEN_KEY == "PRICECHARTING_TOKEN"


async def test_init_stores_credential():
    client = AsyncPriceCharting(TOKEN)
    assert client._token.get_secret_value() == TOKEN
    await client.aclose()


async def test_init_raises_on_empty_token():
    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        AsyncPriceCharting("")


async def test_init_raises_on_incorrect_length_token():
    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        AsyncPriceCharting("a")


async def test_init_raises_on_missing_token():
    with pytest.raises(ValueError, match="PriceCharting API token not found"):
        AsyncPriceCharting()


async def test_init_reads_env_variable(monkeypatch):
    monkeypatch.setenv(AsyncPriceCharting.TOKEN_KEY, TOKEN)

    client = AsyncPriceCharting()
    assert client._token.get_secret_value() == TOKEN
    await client.aclose()


async def test_init_raises_on_incorrect_env_variable(monkeypatch):
    monkeypatch.setenv(AsyncPriceCharting.TOKEN_KEY, "test")

    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        AsyncPriceCharting()


async def test_init_creates_http_client():
    client = AsyncPriceCharting(TOKEN)
    assert isinstance(client.client, AsyncClient)
    assert not client.client.is_closed
    await client.aclose()


async def test_aclose_closes_http_client():
    client = AsyncPriceCharting(TOKEN)
    await client.aclose()
    assert client.client.is_closed


async def test_async_with_returns_client():
    client = AsyncPriceCharting(TOKEN)
    async with client as entered:
        assert entered is client
        assert not client.client.is_closed


async def test_async_with_closes_http_client():
    async with AsyncPriceCharting(TOKEN) as client:
        pass
    assert client.client.is_closed


async def test_async_with_closes_http_client_on_error():
    client = AsyncPriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"):
        async with client:
            raise ValueError("boom")
    assert client.client.is_closed


async def test_product():
    client = AsyncPriceCharting(TOKEN)
    assert await client.product() is None
    await client.aclose()


async def test_products():
    client = AsyncPriceCharting(TOKEN)
    assert await client.products() is None
    await client.aclose()


async def test_offers():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offers() is None
    await client.aclose()


async def test_offer_details():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_details() is None
    await client.aclose()


async def test_offer_publish():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_publish() is None
    await client.aclose()


async def test_offer_feedback():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_feedback() is None
    await client.aclose()


async def test_offer_ship():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_ship() is None
    await client.aclose()


async def test_offer_end():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_end() is None
    await client.aclose()


async def test_offer_refund():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_refund() is None
    await client.aclose()
