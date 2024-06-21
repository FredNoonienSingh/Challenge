from .app import CarAPI


def create_app() -> CarAPI:
    app:CarAPI = CarAPI(__name__)
    return app