import datetime
from enum import Enum, unique


@unique
class RateLimit(Enum):
    """Minimum wait between PriceCharting API calls."""

    API = datetime.timedelta(seconds=1)
    CSV = datetime.timedelta(minutes=10)

    # Offers requests rate limited to 5 minutes for the SAME query
    OFFERS_POLLING = datetime.timedelta(minutes=5)
