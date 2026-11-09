import pytest
from httpx2 import Client, MockTransport, Request, Response

from pypricecharting.error import APIError, ParameterError
from pypricecharting.pricecharting import PriceCharting
from pypricecharting.responses import ProductResponse
from pypricecharting.route import BASE_URL
from tests.mocks.mock_pricecharting import mocked_client

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.

TOKEN = "test-token-12345678901234567890123456789"


def test_token_constant():
    assert PriceCharting.TOKEN_KEY == "PRICECHARTING_TOKEN"


def test_init_stores_credential():
    client = PriceCharting(TOKEN)
    assert client._token.get_secret_value() == TOKEN
    client.close()


def test_init_raises_on_empty_token():
    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        PriceCharting("")


def test_init_raises_on_incorrect_length_token():
    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        PriceCharting("a")


def test_init_raises_on_missing_token():
    with pytest.raises(ValueError, match="PriceCharting API token not found"):
        PriceCharting()


def test_init_reads_env_variable(monkeypatch):
    monkeypatch.setenv(PriceCharting.TOKEN_KEY, TOKEN)

    client = PriceCharting()
    assert client._token.get_secret_value() == TOKEN
    client.close()


def test_init_raises_on_incorrect_env_variable(monkeypatch):
    monkeypatch.setenv(PriceCharting.TOKEN_KEY, "test")

    with pytest.raises(ValueError, match="PriceCharting API token is not 40 characters"):
        PriceCharting()


def test_init_creates_http_client():
    client = PriceCharting(TOKEN)
    assert isinstance(client._client, Client)
    assert not client._client.is_closed
    client.close()


def test_init_uses_transport():
    requests: list[Request] = []

    def handler(request: Request) -> Response:
        requests.append(request)
        return Response(200, json={"status": "success"})

    with PriceCharting(TOKEN, transport=MockTransport(handler)) as client:
        response = client._client.get("/api/product")

    assert response.status_code == 200
    assert len(requests) == 1
    assert requests[0].url == f"{BASE_URL}/api/product?t={TOKEN}"


def test_init_sets_base_url():
    with PriceCharting(TOKEN) as client:
        assert client._client.base_url == BASE_URL


def test_init_uses_base_url():
    requests: list[Request] = []

    def handler(request: Request) -> Response:
        requests.append(request)
        return Response(200, json={"status": "success"})

    base_url = "http://localhost:8080"
    with PriceCharting(TOKEN, base_url=base_url, transport=MockTransport(handler)) as client:
        assert client._client.base_url == base_url
        client._client.get("/api/product")

    assert len(requests) == 1
    assert requests[0].url == f"{base_url}/api/product?t={TOKEN}"


def test_close_closes_http_client():
    client = PriceCharting(TOKEN)
    client.close()
    assert client._client.is_closed


def test_with_returns_client():
    client = PriceCharting(TOKEN)
    with client as entered:
        assert entered is client
        assert not client._client.is_closed


def test_with_closes_http_client():
    with PriceCharting(TOKEN) as client:
        pass
    assert client._client.is_closed


def test_with_closes_http_client_on_error():
    client = PriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"), client:
        raise ValueError("boom")
    assert client._client.is_closed


PRODUCT_JSON = {
    "status": "success",
    "id": "6910",
    "product-name": "EarthBound",
    "console-name": "Super Nintendo",
    "loose-price": 17244,
    "cib-price": 42995,
    "new-price": 53000,
    "release-date": "1995-06-05",
}


@pytest.mark.parametrize(
    ("kwargs", "param"),
    [({"id": "6910"}, "id"), ({"upc": "045496830434"}, "upc"), ({"q": "earthbound"}, "q")],
)
def test_product(kwargs, param):
    requests: list[Request] = []
    with mocked_client(TOKEN, Response(200, json=PRODUCT_JSON), requests) as client:
        product = client.product(**kwargs)

    assert isinstance(product, ProductResponse)
    assert product.id == "6910"
    assert product.product_name == "EarthBound"
    assert product.cib_price == 42995

    assert len(requests) == 1
    request = requests[0]
    assert request.method == "GET"
    assert request.url.path == "/api/product"
    assert dict(request.url.params) == {param: kwargs[param], "t": TOKEN}


def test_product_raises_api_error():
    body = {"status": "error", "error-message": "No such product"}
    requests: list[Request] = []
    with (
        mocked_client(TOKEN, Response(404, json=body), requests) as client,
        pytest.raises(APIError, match="404: No such product"),
    ):
        client.product(id="0")


def test_product_raises_for_invalid_parameters():
    with (
        PriceCharting(TOKEN) as client,
        pytest.raises(
            ParameterError, match=r"Invalid parameters. Either id, upc, or q are required."
        ),
    ):
        client.product()


def test_product_raises_for_multiple_parameters():
    requests: list[Request] = []
    with (
        mocked_client(TOKEN, Response(200, json=PRODUCT_JSON), requests) as client,
        pytest.raises(
            ParameterError, match=r"Invalid parameters. Only one of id, upc, or q is allowed."
        ),
    ):
        client.product(id="6910", upc="045496830434")

    assert requests == []


def test_products():
    client = PriceCharting(TOKEN)
    assert client.products() is None
    client.close()


def test_offers():
    client = PriceCharting(TOKEN)
    assert client.offers() is None
    client.close()


def test_offer_details():
    client = PriceCharting(TOKEN)
    assert client.offer_details() is None
    client.close()


def test_offer_publish():
    client = PriceCharting(TOKEN)
    assert client.offer_publish() is None
    client.close()


def test_offer_feedback():
    client = PriceCharting(TOKEN)
    assert client.offer_feedback() is None
    client.close()


def test_offer_ship():
    client = PriceCharting(TOKEN)
    assert client.offer_ship() is None
    client.close()


def test_offer_end():
    client = PriceCharting(TOKEN)
    assert client.offer_end() is None
    client.close()


def test_offer_refund():
    client = PriceCharting(TOKEN)
    assert client.offer_refund() is None
    client.close()
