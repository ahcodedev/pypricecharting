import pytest
from httpx2 import Request, Response

from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.error import APIError
from pypricecharting.requests import OffersRequestParams, OffersStatus
from pypricecharting.responses import OffersResponse
from pypricecharting.types import Status
from tests.mocks.json import OFFERS_JSON, OFFERS_REQUEST_JSON
from tests.mocks.mock_pricecharting import TOKEN, error_body, mocked_async_client

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.


async def test_offers():
    requests: list[Request] = []
    params = OffersRequestParams.model_validate(OFFERS_REQUEST_JSON)

    async with mocked_async_client(TOKEN, Response(200, json=OFFERS_JSON), requests) as client:
        response = await client.offers(params)

    assert isinstance(response, OffersResponse)
    assert response.status == Status.SUCCESS
    assert len(response.offers) == 2
    assert response.offers[0].offer_id == "testofferid"

    assert len(requests) == 1
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/offers"
    expected = {key: str(value) for key, value in OFFERS_REQUEST_JSON.items()}
    assert dict(requests[0].url.params) == {**expected, "t": TOKEN}


async def test_offers_sends_only_set_parameters():
    requests: list[Request] = []
    params = OffersRequestParams(status=OffersStatus.AVAILABLE)

    async with mocked_async_client(TOKEN, Response(200, json=OFFERS_JSON), requests) as client:
        await client.offers(params)

    assert dict(requests[0].url.params) == {"status": "available", "t": TOKEN}


async def test_offers_raises_api_error():
    requests: list[Request] = []
    params = OffersRequestParams(status=OffersStatus.SOLD)
    async with mocked_async_client(
        TOKEN, Response(400, json=error_body("Invalid status")), requests
    ) as client:
        with pytest.raises(APIError, match="400: Invalid status"):
            await client.offers(params)


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
