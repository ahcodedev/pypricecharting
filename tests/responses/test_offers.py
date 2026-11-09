import json

from pypricecharting.models import Offer
from pypricecharting.responses import OffersResponse
from pypricecharting.types import OfferStatus, Status

OFFERS_JSON = {
    "status": "success",
    "offers": [
        {"offer-id": "smzksacsy5i2dsrddxsrlzsp6i", "offer-status": "sold", "price": 1473},
        {"offer-id": "vtdsww72uyslgooawzyyijsllm", "offer-status": "available", "price": 2500},
    ],
}


def test_offers_json_to_model():
    response = OffersResponse.model_validate_json(json.dumps(OFFERS_JSON))

    assert response.status is Status.SUCCESS
    assert response.offers == [
        Offer(offer_id="smzksacsy5i2dsrddxsrlzsp6i", offer_status=OfferStatus.SOLD, price=1473),
        Offer(
            offer_id="vtdsww72uyslgooawzyyijsllm", offer_status=OfferStatus.AVAILABLE, price=2500
        ),
    ]


def test_offers_model_to_json():
    response = OffersResponse(
        status=Status.SUCCESS,
        offers=[
            Offer(offer_id="smzksacsy5i2dsrddxsrlzsp6i", offer_status=OfferStatus.SOLD, price=1473),
            Offer(
                offer_id="vtdsww72uyslgooawzyyijsllm",
                offer_status=OfferStatus.AVAILABLE,
                price=2500,
            ),
        ],
    )

    dumped = response.model_dump_json(by_alias=True, exclude_none=True)

    assert json.loads(dumped) == OFFERS_JSON


def test_offers_defaults_to_empty_list():
    response = OffersResponse.model_validate_json('{"status": "success"}')

    assert response.offers == []
