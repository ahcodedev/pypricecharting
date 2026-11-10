import pytest
from httpx2 import Client, MockTransport, Request, Response

from pypricecharting.pricecharting import PriceCharting
from pypricecharting.route import BASE_URL
from tests.mocks.mock_pricecharting import TOKEN


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
