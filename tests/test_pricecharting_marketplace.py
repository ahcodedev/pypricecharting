from pypricecharting.pricecharting import PriceCharting
from tests.mocks.mock_pricecharting import TOKEN

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.


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
