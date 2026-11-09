class PriceChartingError(Exception):
    """Base class for all PriceCharting errors"""


class ParameterError(PriceChartingError, ValueError):
    """Raised when an API method is called with invalid parameters"""


class APIError(PriceChartingError):
    """Raised when the API returns an error response"""

    def __init__(self, message: str, status_code: int):
        """Store the API error message and HTTP status code."""
        super().__init__(f"{status_code}: {message}")
        self.message = message
        self.status_code = status_code
