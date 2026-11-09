import json
from datetime import date

from pypricecharting.models import ProductSummary
from pypricecharting.responses import ProductResponse, ProductsResponse
from pypricecharting.types import Status

PRODUCT_JSON = {
    "status": "success",
    "id": "6910",
    "product-name": "EarthBound",
    "console-name": "Super Nintendo",
    "release-date": "1995-06-05",
    "sales-volume": 120,
    "loose-price": 17244,
    "cib-price": 42995,
    "new-price": 53000,
    "bgs-10-price": 60000,
    "condition-9-price": 9000,
    "retail-loose-buy": 12000,
}

PRODUCTS_JSON = {
    "status": "success",
    "products": [
        {"console-name": "Playstation", "id": "4801", "product-name": "Tactics Ogre"},
        {"console-name": "GameBoy Advance", "id": "2611", "product-name": "Tactics Ogre"},
    ],
}


def test_product_json_to_model():
    product = ProductResponse.model_validate_json(json.dumps(PRODUCT_JSON))

    assert product.status is Status.SUCCESS
    assert product.id == "6910"
    assert product.product_name == "EarthBound"
    assert product.console_name == "Super Nintendo"
    assert product.release_date == date(1995, 6, 5)
    assert product.sales_volume == 120
    assert product.loose_price == 17244
    assert product.cib_price == 42995
    assert product.new_price == 53000
    assert product.bgs_10_price == 60000
    assert product.condition_9_price == 9000
    assert product.retail_loose_buy == 12000
    assert product.upc is None


def test_product_model_to_json():
    product = ProductResponse(
        status=Status.SUCCESS,
        id="6910",
        product_name="EarthBound",
        console_name="Super Nintendo",
        release_date=date(1995, 6, 5),
        sales_volume=120,
        loose_price=17244,
        cib_price=42995,
        new_price=53000,
        bgs_10_price=60000,
        condition_9_price=9000,
        retail_loose_buy=12000,
    )

    dumped = product.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == PRODUCT_JSON


def test_products_json_to_model():
    response = ProductsResponse.model_validate_json(json.dumps(PRODUCTS_JSON))

    assert response.status is Status.SUCCESS
    assert response.products == [
        ProductSummary(id="4801", product_name="Tactics Ogre", console_name="Playstation"),
        ProductSummary(id="2611", product_name="Tactics Ogre", console_name="GameBoy Advance"),
    ]


def test_products_model_to_json():
    response = ProductsResponse(
        status=Status.SUCCESS,
        products=[
            ProductSummary(id="4801", product_name="Tactics Ogre", console_name="Playstation"),
            ProductSummary(id="2611", product_name="Tactics Ogre", console_name="GameBoy Advance"),
        ],
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == PRODUCTS_JSON


def test_products_defaults_to_empty_list():
    response = ProductsResponse.model_validate_json('{"status": "success"}')

    assert response.products == []
