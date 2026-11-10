import pytest
from httpx2 import Request, Response

from pypricecharting.error import APIError, ParameterError
from pypricecharting.pricecharting import PriceCharting
from pypricecharting.responses import ProductResponse
from tests.mocks.json import PRODUCT_BASIC_JSON
from tests.mocks.mock_pricecharting import TOKEN, mocked_client

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.


@pytest.mark.parametrize(
    ("kwargs", "param"),
    [({"id": "6910"}, "id"), ({"upc": "045496830434"}, "upc"), ({"q": "earthbound"}, "q")],
)
def test_product(kwargs, param):
    requests: list[Request] = []
    with mocked_client(TOKEN, Response(200, json=PRODUCT_BASIC_JSON), requests) as client:
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
        mocked_client(TOKEN, Response(200, json=PRODUCT_BASIC_JSON), requests) as client,
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
