import pytest
from httpx2 import AsyncClient, MockTransport, Request, Response

from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.route import BASE_URL
from tests.mocks.mock_pricecharting import TOKEN


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
    assert isinstance(client._client, AsyncClient)
    assert not client._client.is_closed
    await client.aclose()


async def test_init_uses_transport():
    requests: list[Request] = []

    def handler(request: Request) -> Response:
        requests.append(request)
        return Response(200, json={"status": "success"})

    async with AsyncPriceCharting(TOKEN, transport=MockTransport(handler)) as client:
        response = await client._client.get("/api/product")

    assert response.status_code == 200
    assert len(requests) == 1
    assert requests[0].url == f"{BASE_URL}/api/product?t={TOKEN}"


async def test_init_sets_base_url():
    async with AsyncPriceCharting(TOKEN) as client:
        assert client._client.base_url == BASE_URL


async def test_init_uses_base_url():
    requests: list[Request] = []

    def handler(request: Request) -> Response:
        requests.append(request)
        return Response(200, json={"status": "success"})

    base_url = "http://localhost:8080"
    async with AsyncPriceCharting(
        TOKEN, base_url=base_url, transport=MockTransport(handler)
    ) as client:
        assert client._client.base_url == base_url
        await client._client.get("/api/product")

    assert len(requests) == 1
    assert requests[0].url == f"{base_url}/api/product?t={TOKEN}"


async def test_aclose_closes_http_client():
    client = AsyncPriceCharting(TOKEN)
    await client.aclose()
    assert client._client.is_closed


async def test_async_with_returns_client():
    client = AsyncPriceCharting(TOKEN)
    async with client as entered:
        assert entered is client
        assert not client._client.is_closed


async def test_async_with_closes_http_client():
    async with AsyncPriceCharting(TOKEN) as client:
        pass
    assert client._client.is_closed


async def test_async_with_closes_http_client_on_error():
    client = AsyncPriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"):
        async with client:
            raise ValueError("boom")
    assert client._client.is_closed
