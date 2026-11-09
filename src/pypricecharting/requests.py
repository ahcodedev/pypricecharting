from typing import Self

from pydantic import PositiveInt, model_validator

from pypricecharting.models import PriceChartingModel
from pypricecharting.types import State


class OfferPublishRequest(PriceChartingModel):
    """api/offer-publish request

    https://www.pricecharting.com/api-documentation#offer-publish
    """

    product: str | None = None
    upc: str | None = None
    asin: str | None = None
    epid: str | None = None
    offer_id: str | None = None
    price_max: int
    condition_id: str
    add_to_collection: str | None = None
    cost_basis: int | None = None
    description: str | None = None
    broken: State | None = None
    pristine: State | None = None
    scratch: State | None = None
    stickers: State | None = None
    tear: State | None = None
    writing: State | None = None
    price_min: PositiveInt | None = None
    sku: str | None = None
    quantity: PositiveInt | None = None

    @model_validator(mode="after")
    def check_identifier(self) -> Self:
        """Validate at least one identifier provided"""
        ids = [self.product, self.upc, self.asin, self.epid, self.offer_id]
        for id in ids:
            if id is not None:
                return self
        raise ValueError("One of product, upc, asin, epid, or offer_id not provided")
