from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class LanguageMiddleware(BaseHTTPMiddleware):
    """Middleware to set the language based on the 'accept-language' header."""

    async def dispatch(self, request: Request, call_next):
        """Middleware to set the language based on the 'accept-language' header.
        Defaults to 'en' if the language is not recognized."""
        lang = request.headers.get("accept-language", "en").split(",")[0].lower()
        request.state.lang = lang if lang in ["fr", "en"] else "en"
        response = await call_next(request)
        return response
