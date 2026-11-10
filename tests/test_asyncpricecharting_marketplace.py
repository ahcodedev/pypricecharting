from pypricecharting.asyncpricecharting import AsyncPriceCharting
from tests.mocks.mock_pricecharting import TOKEN

# Template tests: methods that are still placeholders only check they can be called.
# Replace their `is None` assertions once each method is implemented.


async def test_offers():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offers() is None
    await client.aclose()


async def test_offer_details():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_details() is None
    await client.aclose()


async def test_offer_publish():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_publish() is None
    await client.aclose()


async def test_offer_feedback():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_feedback() is None
    await client.aclose()


async def test_offer_ship():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_ship() is None
    await client.aclose()


async def test_offer_end():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_end() is None
    await client.aclose()


async def test_offer_refund():
    client = AsyncPriceCharting(TOKEN)
    assert await client.offer_refund() is None
    await client.aclose()
