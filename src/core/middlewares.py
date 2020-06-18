import copy
from urllib.parse import urlencode


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):


        response = get_response(request)

        with open('logger.txt', 'a') as f:
            f.write(f'processing request: {request.path} {request.method}\n')


        return response

    return middleware


class QueryParamsInjectorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.


        query_params = copy.deepcopy(request.GET)
        if 'page' in query_params:
            del query_params['page']
        request.query_params = urlencode(query_params)


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response