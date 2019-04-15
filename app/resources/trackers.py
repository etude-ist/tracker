import uuid

import falcon

from jobs.analytics import write_db
from resources.settings import COOKIE_MAX_AGE, DOMAIN, PATH


class BaseResource:

    def on_get(self, req, resp):
        resp.staus = falcon.HTTP_200


class CartTrackerResource:

    def async_write(self, cart_id, payload):
        write_db.s(cart_id=cart_id, payload=payload).delay()

    def on_post(self, req, resp):

        cookies = req.cookies
        if 'cart_id' in cookies:
            cart_id = cookies.get('cart_id')
        else:
            cart_id = uuid.uuid4()
            resp.set_cookie(
                'cart_id',
                str(cart_id),
                max_age=COOKIE_MAX_AGE,
                domain=DOMAIN,
                path=PATH,
                secure=False
            )

        body = req.stream.read()
        payload = body.decode('utf-8')
        self.async_write(cart_id, payload)

        resp.status = falcon.HTTP_204
