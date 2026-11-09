import json

from pypricecharting.models import Buyer

BUYER_JSON = {
    "buyer-email": "buyer@example.com",
    "shipping-name": "Jane Doe",
    "shipping-line1": "123 Main St",
    "shipping-line2": "Apt 4",
    "shipping-city": "Springfield",
    "shipping-state": "IL",
    "shipping-zip": "62701",
    "shipping-country": "US",
}


def test_buyer_json_to_model():
    buyer = Buyer.model_validate_json(json.dumps(BUYER_JSON))

    assert buyer.buyer_email == "buyer@example.com"
    assert buyer.shipping_name == "Jane Doe"
    assert buyer.shipping_line1 == "123 Main St"
    assert buyer.shipping_line2 == "Apt 4"
    assert buyer.shipping_city == "Springfield"
    assert buyer.shipping_state == "IL"
    assert buyer.shipping_zip == "62701"
    assert buyer.shipping_country == "US"


def test_buyer_model_to_json():
    buyer = Buyer(
        buyer_email="buyer@example.com",
        shipping_name="Jane Doe",
        shipping_line1="123 Main St",
        shipping_line2="Apt 4",
        shipping_city="Springfield",
        shipping_state="IL",
        shipping_zip="62701",
        shipping_country="US",
    )

    dumped = buyer.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == BUYER_JSON
