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
        use_attribute_docstrings=True,
    )


class ProductSummary(PriceChartingModel):
    """A product as listed in /api/products search results.

    https://www.pricecharting.com/api-documentation#api-products
    """

    id: str | None = None
    """PriceCharting product ID."""
    product_name: str | None = None
    console_name: str | None = None


class Offer(PriceChartingModel):
    """An offer as listed in /api/offers results.

    https://www.pricecharting.com/api-documentation#offers
    """

    offer_id: str | None = None
    """Unique offer ID, also shown in the offer URL."""
    offer_status: OfferStatus | None = None
    offer_url: str | None = None
    """Relative URL of the offer page. Prepend `route.BASE_URL` for a full link."""
    id: int | None = None
    """PriceCharting product ID, not the offer ID."""
    product_name: str | None = None
    console_name: str | None = None
    condition_string: str | None = None
    """Condition shown to buyers, such as "Normal Wear"."""
    include_string: str | None = None
    """What comes with the item, such as game only or game and box."""
    price: int | None = None
    """Current price in pennies, or the sale price if sold. Includes any shipping premium."""
    is_available: bool | None = None
    is_sold: bool | None = None
    is_ended: bool | None = None
    is_shipped: bool | None = None
    sale_time: date | None = None
    """Date the offer sold. `0001-01-01` if it hasn't happened."""
    shipped_time: date | None = None
    """Date the seller told PriceCharting the offer shipped. `0001-01-01` if it hasn't happened."""
    ended_time: date | None = None
    """Date the offer ended, by sale or by the seller. `0001-01-01` if it hasn't happened."""
    cert_id: str | None = None
    """Grading company certificate number. Graded offers only."""
    grade_co_id: int | None = None
    """ID of the grading company. Graded offers only."""


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
