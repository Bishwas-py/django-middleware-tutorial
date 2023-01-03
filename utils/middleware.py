
from django.http import HttpResponse


class CustomRequestMiddleware:
    """
    Middleware to check if the request body contains 
    127.0.0.1 [Internal IP address] or not. Also, it bans the user if the user
    sends more than 7 requests with Internal IP address, for 5 minutes.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # upper code executes before the view function
        response = self.get_response(request) # this triggers the view function
        # lower code executes after the view function

        # return HttpResponse("I'm the bestest. Overriding the response, not giving it sh*t.")
        return response