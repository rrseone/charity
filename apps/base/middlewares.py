import threading

_requests = threading.local()


class RequestMiddleware:
    """Middleware to store the request object globally."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _requests.request = request  # Store the request globally
        response = self.get_response(request)
        return response


def get_current_user():
    """Helper function to get the currently logged-in users."""
    return getattr(_requests, "request", None) and getattr(_requests.request, "users", None)