from enum import Enum, unique


@unique
class Status(Enum):
    """PriceCharting API response status"""

    SUCCESS = "success"
    ERROR = "error"
