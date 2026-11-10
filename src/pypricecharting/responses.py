from contextlib import suppress
from datetime import date

from httpx2 import Response
from pydantic import Field, ValidationError

from pypricecharting.error import APIError
from pypricecharting.models import Buyer, Offer, PriceChartingModel, ProductSummary
from pypricecharting.types import OfferStatus, Rating, Status


class ErrorResponse(PriceChartingModel):
    """Error response from any endpoint

    Returned with a 4xx or 5xx status code. The clients raise `error.APIError` instead of
    returning it.

    https://www.pricecharting.com/api-documentation
    """

    status: Status
    error_message: str | None = None
    """Why the request failed."""


class ProductResponse(ProductSummary):
    """api/product response

    Prices are in pennies. Price keys mean different conditions for video games, cards and
    comics, noted below as video games / cards / comics.

    https://www.pricecharting.com/api-documentation#api-product
    """

    status: Status
    genre: str | None = None
    """Product genre, such as "RPG". See `types.Genre` for video game genres."""
    release_date: date | None = None
    upc: str | None = None
    asin: str | None = None
    """Amazon ASIN."""
    epid: str | None = None
    """eBay ePID."""
    tcg_id: str | None = None
    """TCGplayer ID. Trading cards only."""
    sales_volume: int | None = None
    """Units sold per year."""

    loose_price: int | None = None
    """Video games: item only, no box or manual. Cards: ungraded. Comics: ungraded."""
    cib_price: int | None = None
    """Video games: item with box and manual. Cards: grade 7 or 7.5. Comics: 4.0 or 4.5."""
    new_price: int | None = None
    """Video games: new and sealed. Cards: grade 8 or 8.5. Comics: 6.0 or 6.5."""
    graded_price: int | None = None
    """Video games: new, graded by WATA or VGA. Cards: grade 9. Comics: 8.0 or 8.5."""
    box_only_price: int | None = None
    """Video games: original box only. Cards: grade 9.5. Comics: 9.2."""
    manual_only_price: int | None = None
    """Video games: original manual only. Cards: PSA 10. Comics: 9.8."""
    bgs_10_price: int | None = None
    """Cards: BGS 10. Comics: 10.0."""
    condition_9_price: int | None = None
    """Cards: grade 1. Comics: 2.0 (Good)."""
    condition_10_price: int | None = None
    """Cards: grade 2. Comics: 9.6 (Near Mint+)."""
    condition_13_price: int | None = None
    """Cards: grade 3. Comics: 3.0."""
    condition_14_price: int | None = None
    """Cards: grade 4. Comics: 5.0."""
    condition_15_price: int | None = None
    """Cards: grade 5. Comics: 7.0."""
    condition_16_price: int | None = None
    """Cards: grade 6. Comics: 9.0."""
    condition_17_price: int | None = None
    """Cards: CGC 10. Comics: 9.4."""
    condition_18_price: int | None = None
    """Cards: SGC 10."""
    condition_19_price: int | None = None
    """Cards: CGC 10 Pristine."""
    condition_20_price: int | None = None
    """Cards: BGS 10 Black."""
    condition_21_price: int | None = None
    """Cards: TAG 10."""
    condition_22_price: int | None = None
    """Cards: ACE 10."""

    gamestop_price: int | None = None
    """GameStop pre-owned price."""
    retail_loose_buy: int | None = None
    """Recommended price for a retailer to buy a loose copy."""
    retail_loose_sell: int | None = None
    """Recommended price for a retailer to sell a loose copy."""
    retail_cib_buy: int | None = None
    """Recommended price for a retailer to buy a complete-in-box copy."""
    retail_cib_sell: int | None = None
    """Recommended price for a retailer to sell a complete-in-box copy."""
    retail_new_buy: int | None = None
    """Recommended price for a retailer to buy a new copy."""
    retail_new_sell: int | None = None
    """Recommended price for a retailer to sell a new copy."""


class ProductsResponse(PriceChartingModel):
    """api/products response

    https://www.pricecharting.com/api-documentation#api-products
    """

    status: Status
    products: list[ProductSummary] = Field(default_factory=list)
    """Up to 20 best matches for the search."""


class OffersResponse(PriceChartingModel):
    """api/offers response

    https://www.pricecharting.com/api-documentation#offers
    """

    status: Status
    offers: list[Offer] = Field(default_factory=list)


class OfferDetailsResponse(PriceChartingModel):
    """api/offer-details response

    https://www.pricecharting.com/api-documentation#offer-details
    """

    status: Status
    buyer: Buyer | None = None
    """Buyer contact and shipping details. Set once the offer sells."""
    buyer_left_feedback: bool | None = None
    seller_left_feedback: bool | None = None
    id: int | None = None
    """PriceCharting product ID, not the offer ID."""
    product_name: str | None = None
    console_name: str | None = None
    condition: str | None = None
    includes: str | None = None
    cost_basis: int | None = None
    """What the seller paid for the item, in pennies."""
    price: int | None = None
    """Current price in pennies, or the sale price if sold. Includes any shipping premium."""
    max_price: int | None = None
    """Listing price in pennies, or the starting price of a reverse auction."""
    min_price: int | None = None
    """Lowest price in pennies of a reverse auction. Not set for standard listings."""
    shipping_premium: int | None = None
    """Extra the buyer paid for international shipping, in pennies."""
    has_pictures: bool | None = None
    is_collection: bool | None = None
    """Whether the item is in the seller's collection instead of listed for sale."""
    is_ended: bool | None = None
    is_price_descending: bool | None = None
    """Whether the offer is a reverse auction, dropping toward `min_price`."""
    is_refunded: bool | None = None
    is_shipped: bool | None = None
    is_sold: bool | None = None
    offer_id: str | None = None
    offer_status: OfferStatus | None = None
    offer_url: str | None = None
    """Relative URL of the offer page. Prepend `route.BASE_URL` for a full link."""
    sku: str | None = None
    """Seller's internal SKU. Only returned to the seller."""
    tracking_number: str | None = None
    start_time: date | None = None
    """Date the offer was published. Resets when the offer is revised."""
    sale_time: date | None = None
    """Date the offer sold. `0001-01-01` if it hasn't happened."""
    shipped_time: date | None = None
    """Date the seller told PriceCharting the offer shipped. `0001-01-01` if it hasn't happened."""
    ended_time: date | None = None
    """Date the offer ended, by sale or by the seller. `0001-01-01` if it hasn't happened."""
    refunded_time: date | None = None
    """Date the offer was refunded. `0001-01-01` if it hasn't happened."""


class OfferPublishResponse(PriceChartingModel):
    """api/offer-publish response

    https://www.pricecharting.com/api-documentation#offer-publish
    """

    status: Status
    offer_id: str | None = None
    offer_url: str | None = None
    """Relative URL of the offer page. Prepend `route.BASE_URL` for a full link."""
    offer_status: OfferStatus | None = None
    product_name: str | None = None
    console_name: str | None = None
    condition_string: str | None = None
    """Condition shown to buyers, such as "Normal Wear"."""
    include_string: str | None = None
    """What comes with the item, such as game only or game and box."""
    has_pictures: bool | None = None
    price: int | None = None
    """Listing price in pennies."""
    cost_basis: int | None = None
    """What the seller paid for the item, in pennies."""
    sku: str | None = None
    """Seller's internal SKU."""
    is_collection: bool | None = None
    """Whether the item is in the seller's collection instead of listed for sale."""
    quantity: int | None = None
    """Number of copies owned. Collections only."""
    start_time: date | None = None
    """Date the offer was published."""


class OfferFeedbackResponse(PriceChartingModel):
    """api/offer-feedback response

    https://www.pricecharting.com/api-documentation#offer-feedback
    """

    status: Status
    offer_id: str | None = None
    rating: Rating | None = None
    comment: str | None = None


class OfferShipResponse(PriceChartingModel):
    """api/offer-ship response

    https://www.pricecharting.com/api-documentation#offer-ship
    """

    status: Status
    offer_id: str | None = None
    is_shipped: bool | None = None
    shipped_time: date | None = None
    """Date PriceCharting was notified, not when the carrier received the item."""
    tracking_number: str | None = None


class OfferEndResponse(PriceChartingModel):
    """api/offer-end response

    https://www.pricecharting.com/api-documentation#offer-end
    """

    status: Status
    offer_id: str | None = None
    is_ended: bool | None = None
    ended_time: date | None = None


class OfferRefundResponse(PriceChartingModel):
    """api/offer-refund response

    https://www.pricecharting.com/api-documentation#offer-refund
    """

    status: Status
    offer_id: str | None = None
    is_refunded: bool | None = None
    refunded_time: date | None = None


def _parse[M: PriceChartingModel](response: Response, model: type[M]) -> M:
    """Validate an HTTP response into a response model.

    Args:
        response: The HTTP response from the PriceCharting API.
        model: The response model to validate the JSON body into.

    Returns:
        The validated response model.

    Raises:
        APIError: If the response is not JSON or has a non-2xx status code. The message is
            the body's `error-message`, or the HTTP reason phrase.

    """
    try:
        data = response.json()
    except ValueError:
        raise APIError(
            response.reason_phrase or "Invalid JSON response", response.status_code
        ) from None

    if not response.is_success:
        message = None
        with suppress(ValidationError):
            message = ErrorResponse.model_validate(data).error_message
        raise APIError(message or response.reason_phrase or "Unknown error", response.status_code)

    return model.model_validate(data)
