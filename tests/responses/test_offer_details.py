import json
from datetime import date

from pypricecharting.models import Buyer
from pypricecharting.responses import OfferDetailsResponse
from pypricecharting.types import OfferStatus, Status
from tests.mocks.json import OFFER_DETAILS_JSON


def test_offer_details_json_to_model():
    details = OfferDetailsResponse.model_validate_json(json.dumps(OFFER_DETAILS_JSON))

    assert details.status is Status.SUCCESS
    assert details.buyer == Buyer(
        buyer_email="buyer@example.com",
        shipping_name="Jane Doe",
        shipping_line1="123 Main St",
        shipping_city="Springfield",
        shipping_state="IL",
        shipping_zip="62701",
        shipping_country="US",
    )
    assert details.buyer_left_feedback is False
    assert details.seller_left_feedback is True
    assert details.id == 9307
    assert details.product_name == "M.C. Kids"
    assert details.console_name == "NES"
    assert details.condition == "Normal wear"
    assert details.includes == "Game only"
    assert details.cost_basis == 500
    assert details.price == 1473
    assert details.price_max == 2000
    assert details.price_min == 1000
    assert details.shipping_premium == 0
    assert details.best_competing_price == 1299
    assert details.value == 1473
    assert details.has_pictures is True
    assert details.is_best_priced_offer is False
    assert details.is_collection is False
    assert details.is_ended is True
    assert details.is_price_descending is True
    assert details.is_refunded is False
    assert details.is_shipped is True
    assert details.is_sold is True
    assert details.offer_id == "testofferid"
    assert details.offer_status is OfferStatus.SOLD
    assert details.pending_reason == ""
    assert details.offer_url == "/offer/testofferid"
    assert details.image_url == "/images/offers/testofferid.jpg"
    assert details.seller_id == "3mxwhfh46xj3f47cgdyu5ynzos"
    assert details.sku == "ABC-123"
    assert details.tracking_number == "901234567890000"
    assert details.start_time == date(2017, 10, 1)
    assert details.sale_time == date(2017, 10, 31)
    assert details.shipped_time == date(2017, 11, 1)
    assert details.ended_time == date(2017, 10, 31)
    assert details.refunded_time == date(1, 1, 1)


def test_offer_details_model_to_json():
    details = OfferDetailsResponse.model_validate_json(json.dumps(OFFER_DETAILS_JSON))

    dumped = details.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFER_DETAILS_JSON


def test_offer_details_without_buyer():
    details = OfferDetailsResponse.model_validate_json('{"status": "success"}')

    assert details.buyer is None


def test_offer_details_pending_reason():
    details = OfferDetailsResponse.model_validate_json(
        '{"status": "success", "offer-status": "pending", "pending-reason": "Vacation hold"}'
    )

    assert details.offer_status is OfferStatus.PENDING
    assert details.pending_reason == "Vacation hold"
