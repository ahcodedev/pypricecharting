import pytest
from httpx2 import Client

from pypricecharting.pricecharting import PriceCharting

# Template tests: the API methods are placeholders, so these only check they can be called.
# Replace the `is None` assertions once each method is implemented.

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
    assert isinstance(client.client, Client)
    assert not client.client.is_closed
    client.close()


def test_close_closes_http_client():
    client = PriceCharting(TOKEN)
    client.close()
    assert client.client.is_closed


def test_with_returns_client():
    client = PriceCharting(TOKEN)
    with client as entered:
        assert entered is client
        assert not client.client.is_closed


def test_with_closes_http_client():
    with PriceCharting(TOKEN) as client:
        pass
    assert client.client.is_closed


def test_with_closes_http_client_on_error():
    client = PriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"), client:
        raise ValueError("boom")
    assert client.client.is_closed


def test_product():
    client = PriceCharting(TOKEN)
    assert client.product() is None
    client.close()


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
