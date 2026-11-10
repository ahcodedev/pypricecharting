import pytest
from httpx2 import AsyncClient, MockTransport, Request, Response

from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.error import APIError, ParameterError
from pypricecharting.responses import ProductResponse
from pypricecharting.route import BASE_URL
from tests.mocks.json import PRODUCT_BASIC_JSON
from tests.mocks.mock_pricecharting import mocked_async_client

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.

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


@pytest.mark.parametrize(
    ("kwargs", "param"),
    [({"id": "6910"}, "id"), ({"upc": "045496830434"}, "upc"), ({"q": "earthbound"}, "q")],
)
async def test_product(kwargs, param):
    requests: list[Request] = []
    async with mocked_async_client(
        TOKEN, Response(200, json=PRODUCT_BASIC_JSON), requests
    ) as client:
        product = await client.product(**kwargs)

    assert isinstance(product, ProductResponse)
    assert product.id == "6910"
    assert product.product_name == "EarthBound"
    assert product.cib_price == 42995

    assert len(requests) == 1
    request = requests[0]
    assert request.method == "GET"
    assert request.url.path == "/api/product"
    assert dict(request.url.params) == {param: kwargs[param], "t": TOKEN}


async def test_product_raises_api_error():
    body = {"status": "error", "error-message": "No such product"}
    requests: list[Request] = []
    async with mocked_async_client(TOKEN, Response(404, json=body), requests) as client:
        with pytest.raises(APIError, match="404: No such product"):
            await client.product(id="0")


async def test_product_raises_for_invalid_parameters():
    async with AsyncPriceCharting(TOKEN) as client:
        with pytest.raises(
            ParameterError, match=r"Invalid parameters. Either id, upc, or q are required."
        ):
            await client.product()


async def test_product_raises_for_multiple_parameters():
    requests: list[Request] = []
    async with mocked_async_client(
        TOKEN, Response(200, json=PRODUCT_BASIC_JSON), requests
    ) as client:
        with pytest.raises(
            ParameterError, match=r"Invalid parameters. Only one of id, upc, or q is allowed."
        ):
            await client.product(id="6910", upc="045496830434")

    assert requests == []


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
