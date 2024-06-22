from .app import CarAPI


def create_app() -> CarAPI:
    """creates app 

    Returns:
        CarAPI: child class of Flask.App 
    """
    app: CarAPI = CarAPI(__name__)
    return app
