from datetime import date

from pydantic import BaseModel, ConfigDict

from pypricecharting.types import OfferStatus


def to_kebab(name: str) -> str:
    """Convert a snake_case field name to the API's kebab-case key."""
    return name.replace("_", "-")


class PriceChartingModel(BaseModel):
    """Base model that maps snake_case fields to the API's kebab-case keys."""

    model_config = ConfigDict(
        alias_generator=to_kebab,
        populate_by_name=True,
    )


class ProductSummary(PriceChartingModel):
    """A product as listed in /api/products search results.

    https://www.pricecharting.com/api-documentation#api-products
    """

    id: str | None = None
    product_name: str | None = None
    console_name: str | None = None


class Offer(PriceChartingModel):
    """An offer as listed in /api/offers results.

    https://www.pricecharting.com/api-documentation#offers
    """

    offer_id: str | None = None
    offer_status: OfferStatus | None = None
    offer_url: str | None = None  # relative URL, prepend https://www.pricecharting.com
    id: int | None = None  # PriceCharting product ID
    product_name: str | None = None
    console_name: str | None = None
    condition_string: str | None = None
    include_string: str | None = None
    price: int | None = None  # current price, or sale price with shipping premium if sold
    is_available: bool | None = None
    is_sold: bool | None = None
    is_ended: bool | None = None
    is_shipped: bool | None = None
    sale_time: date | None = None
    shipped_time: date | None = None
    ended_time: date | None = None
    cert_id: str | None = None  # grading company certificate number, graded offers only
    grade_co_id: int | None = None  # grading company ID, graded offers only


class Buyer(PriceChartingModel):
    """The buyer of a sold offer, as returned by /api/offer-details."""

    buyer_email: str | None = None
    shipping_name: str | None = None
    shipping_line1: str | None = None
    shipping_line2: str | None = None
    shipping_city: str | None = None
    shipping_state: str | None = None
    shipping_zip: str | None = None
    shipping_country: str | None = None
