"""mohtawaist — عميل Arabic Content Intelligence API (بايثون، بلا تبعيات خارجية)."""
from .client import Client, analyze  # noqa: F401
__version__ = "1.0.0"
__all__ = ["Client", "analyze"]
