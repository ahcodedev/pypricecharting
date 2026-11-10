import pytest
from httpx2 import Request, Response

from pypricecharting.asyncpricecharting import AsyncPriceCharting
from pypricecharting.error import APIError, ParameterError
from pypricecharting.responses import ProductResponse, ProductsResponse
from pypricecharting.types import Status
from tests.mocks.json import PRODUCT_BASIC_JSON, PRODUCTS_JSON
from tests.mocks.mock_pricecharting import TOKEN, error_body, mocked_async_client


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
    body = error_body("No such product")
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
    requests: list[Request] = []

    async with mocked_async_client(TOKEN, Response(200, json=PRODUCTS_JSON), requests) as client:
        response = await client.products("Tactics Ogre")

    assert isinstance(response, ProductsResponse)
    assert response.status == Status.SUCCESS
    assert len(response.products) == 2
    assert response.products[0].product_name == "Tactics Ogre"
    assert response.products[1].product_name == "Tactics Ogre"

    assert len(requests) == 1
    assert requests[0].method == "GET"
    assert requests[0].url.path == "/api/products"
    assert dict(requests[0].url.params) == {"q": "Tactics Ogre", "t": TOKEN}


async def test_products_raises_for_invalid_parameter():
    async with AsyncPriceCharting(TOKEN) as client:
        with pytest.raises(ParameterError, match=r"Invalid parameter; Query string q was empty"):
            await client.products("")
