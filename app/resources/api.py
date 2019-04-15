import falcon

from resources.settings import BASE_URL
from resources.trackers import (
    BaseResource, CartTrackerResource
)
from resources.utils import base_url


def create():
    app = falcon.API()

    compose_url = base_url(BASE_URL)

    app.add_route(compose_url("/"), BaseResource())
    app.add_route(compose_url("/item"), CartTrackerResource())

    return app
