import pytest
from httpx2 import Client

from pypricecharting.pypricecharting import PyPriceCharting

# Template tests: the API methods are placeholders, so these only check they can be called.
# Replace the `is None` assertions once each method is implemented.

TOKEN = "test-token"


def test_init_stores_credential():
    client = PyPriceCharting(TOKEN)
    assert client.credential == TOKEN
    client.close()


def test_init_creates_http_client():
    client = PyPriceCharting(TOKEN)
    assert isinstance(client.client, Client)
    assert not client.client.is_closed
    client.close()


def test_close_closes_http_client():
    client = PyPriceCharting(TOKEN)
    client.close()
    assert client.client.is_closed


def test_with_returns_client():
    client = PyPriceCharting(TOKEN)
    with client as entered:
        assert entered is client
        assert not client.client.is_closed


def test_with_closes_http_client():
    with PyPriceCharting(TOKEN) as client:
        pass
    assert client.client.is_closed


def test_with_closes_http_client_on_error():
    client = PyPriceCharting(TOKEN)
    with pytest.raises(ValueError, match="boom"), client:
        raise ValueError("boom")
    assert client.client.is_closed


def test_product():
    client = PyPriceCharting(TOKEN)
    assert client.product() is None
    client.close()


def test_products():
    client = PyPriceCharting(TOKEN)
    assert client.products() is None
    client.close()


def test_offers():
    client = PyPriceCharting(TOKEN)
    assert client.offers() is None
    client.close()


def test_offer_details():
    client = PyPriceCharting(TOKEN)
    assert client.offer_details() is None
    client.close()


def test_offer_publish():
    client = PyPriceCharting(TOKEN)
    assert client.offer_publish() is None
    client.close()


def test_offer_feedback():
    client = PyPriceCharting(TOKEN)
    assert client.offer_feedback() is None
    client.close()


def test_offer_ship():
    client = PyPriceCharting(TOKEN)
    assert client.offer_ship() is None
    client.close()


def test_offer_end():
    client = PyPriceCharting(TOKEN)
    assert client.offer_end() is None
    client.close()


def test_offer_refund():
    client = PyPriceCharting(TOKEN)
    assert client.offer_refund() is None
    client.close()
