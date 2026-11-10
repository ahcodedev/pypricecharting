from enum import StrEnum
from typing import Self

from pydantic import PositiveInt, model_validator

from pypricecharting.models import PriceChartingModel
from pypricecharting.types import Console, Genre, State


class OfferPublishRequestParams(PriceChartingModel):
    """api/offer-publish request

    Set one of `product`, `upc`, `asin`, or `epid` to create an offer, or `offer_id` to edit one.
    Set each condition tag that applies to `State.ON`. Leave them all unset for normal wear.

    https://www.pricecharting.com/api-documentation#offer-publish
    """

    product: str | None = None
    """PriceCharting product ID of the item to list."""
    upc: str | None = None
    asin: str | None = None
    epid: str | None = None
    offer_id: str | None = None
    """ID of an existing offer to edit. The other identifiers create a new offer."""
    price_max: int
    """Price in pennies buyers pay, or the starting price when `price_min` is set."""
    condition_id: int
    """Condition ID for the product's category. See `types.Condition`."""
    add_to_collection: State | None = None
    """Set to `State.ON` to add the item to your collection instead of listing it for sale."""
    cost_basis: int | None = None
    """What you paid for the item, in pennies."""
    description: str | None = None
    """Listing description, up to 300 characters."""
    broken: State | None = None
    pristine: State | None = None
    """No blemishes. Overrides the other condition tags."""
    scratch: State | None = None
    stickers: State | None = None
    tear: State | None = None
    writing: State | None = None
    price_min: PositiveInt | None = None
    """Lowest price in pennies.

    Makes the offer a reverse auction that drops from `price_max` over 30 days.
    """
    sku: str | None = None
    """Your internal SKU, up to 64 alphanumeric characters. Unique among active offers."""
    quantity: PositiveInt | None = None
    """Number of copies owned. Collections only. The API defaults to 1."""

    @model_validator(mode="after")
    def check_identifier(self) -> Self:
        """Check that at least one of `product`, `upc`, `asin`, `epid`, or `offer_id` is set.

        Raises:
            ValueError: If none of them is set.

        """
        ids = [self.product, self.upc, self.asin, self.epid, self.offer_id]
        for id in ids:
            if id is not None:
                return self
        raise ValueError("One of product, upc, asin, epid, or offer_id is required")


class OffersStatus(StrEnum):
    """Offer status to filter api/offers by"""

    AVAILABLE = "available"
    SOLD = "sold"
    ENDED = "ended"
    COLLECTION = "collection"
    """Tracked in the seller's collection, not listed for sale."""


class OffersSort(StrEnum):
    """Sort order for api/offers results"""

    NAME = "name"
    """Alphabetical."""
    STARTS = "starts"
    """Newest listings first."""
    LOWEST_PRICE = "lowest-price"


class OffersRequestParams(PriceChartingModel):
    """api/offers request

    Only `status` is required. The other fields narrow the results.

    https://www.pricecharting.com/api-documentation#offers
    """

    status: OffersStatus
    buyer: str | None = None
    """Buyer user ID."""
    console: Console | None = None
    condition_id: int | None = None
    """Condition ID for the product's category. See `types.Condition`."""
    genre: Genre | None = None
    id: str | None = None
    """PriceCharting product ID."""
    seller: str | None = None
    """Seller user ID."""
    sort: OffersSort | None = None
