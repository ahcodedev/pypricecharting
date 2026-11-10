import pytest
from httpx2 import Request, Response

from pypricecharting.error import APIError
from pypricecharting.pricecharting import PriceCharting
from pypricecharting.requests import OffersRequestParams, OffersStatus
from pypricecharting.responses import OffersResponse
from pypricecharting.types import Status
from tests.mocks.json import OFFERS_JSON, OFFERS_REQUEST_JSON
from tests.mocks.mock_pricecharting import TOKEN, error_body, mocked_client

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.


def test_offers():
    requests: list[Request] = []
    params = OffersRequestParams.model_validate(OFFERS_REQUEST_JSON)

    with mocked_client(TOKEN, Response(200, json=OFFERS_JSON), requests) as client:
        response = client.offers(params)

    assert isinstance(response, OffersResponse)
    assert response.status == Status.SUCCESS
    assert len(response.offers) == 2
    assert response.offers[0].offer_id == "testofferid"

    assert len(requests) == 1
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/offers"
    expected = {key: str(value) for key, value in OFFERS_REQUEST_JSON.items()}
    assert dict(requests[0].url.params) == {**expected, "t": TOKEN}


def test_offers_sends_only_set_parameters():
    requests: list[Request] = []
    params = OffersRequestParams(status=OffersStatus.AVAILABLE)

    with mocked_client(TOKEN, Response(200, json=OFFERS_JSON), requests) as client:
        client.offers(params)

    assert dict(requests[0].url.params) == {"status": "available", "t": TOKEN}


def test_offers_raises_api_error():
    requests: list[Request] = []
    params = OffersRequestParams(status=OffersStatus.SOLD)
    with (
        mocked_client(TOKEN, Response(400, json=error_body("Invalid status")), requests) as client,
        pytest.raises(APIError, match="400: Invalid status"),
    ):
        client.offers(params)


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
