
from collections.abc import Callable     #imported for typing, typing.Callable is deprecated since 3.9
from werkzeug import Response            # Imported for typing 
from flask import request, make_response

class EndpointHandler():
    """ Wrapper around function that gets invoked by the Endpoint
    """
    def __init__(self, action:Callable) -> None:
        self.action = action

    def __call__(self, *args, **kwargs) -> Response:
        """ calls the function 

        Returns:
            Response: return value of invoked function wrapped in JSON response with HTTP Status Code 
        """
        response = self.action(*args, **request.view_args)
        return make_response(response)
