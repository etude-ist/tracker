import uuid

import falcon

from jobs.analytics import write_db
from models.trackers import Cart
from resources.settings import PATH
from resources.trackers import CartTrackerResource
from tests.utils import fake_after_return, make_item


def sync_write(self, cart_id, payload):
    write_db.s(cart_id=cart_id, payload=payload).apply()


def test_pipline(
        monkeypatch, api_test_client, session
):
    monkeypatch.setattr(write_db, '_session', session)
    monkeypatch.setattr(write_db, 'after_return', fake_after_return)
    monkeypatch.setattr(CartTrackerResource, 'async_write', sync_write)

    result = api_test_client.simulate_post(
        PATH,
        json=make_item()
    )
    cookies = result.cookies
    assert 'cart_id' in cookies
    first_cart_id = cookies.get('cart_id').value
    assert result.status == falcon.HTTP_204

    result = api_test_client.simulate_post(
        PATH,
        json=make_item()
    )
    assert 'cart_id' in result.cookies
    second_cart_id = result.cookies.get('cart_id').value
    assert result.status == falcon.HTTP_204

    result = api_test_client.simulate_post(
        PATH,
        json=make_item(),
        headers={'Cookie': f"cart_id={first_cart_id}"}
    )
    assert result.status == falcon.HTTP_204

    cart = session.query(Cart).filter(
        Cart.id == uuid.UUID(first_cart_id)
    ).one()
    assert cart
    assert len(cart.items) == 2

    cart = session.query(Cart).filter(
        Cart.id == uuid.UUID(second_cart_id)
    ).one()
    assert cart
    assert len(cart.items) == 1
