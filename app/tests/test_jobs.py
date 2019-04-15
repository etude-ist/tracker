import uuid

import ujson

from jobs.analytics import write_db
from models.trackers import Cart
from tests.utils import fake_after_return, make_item


def test_write_db_job(
        monkeypatch, api_test_client, session
):
    monkeypatch.setattr(write_db, '_session', session)
    monkeypatch.setattr(write_db, 'after_return', fake_after_return)

    cart_id = uuid.uuid4()
    payload = ujson.dumps(make_item())
    task = write_db.s(cart_id=cart_id, payload=payload).apply()
    assert task.status == "SUCCESS"
    cart = session.query(Cart).filter(Cart.id == cart_id).one()
    assert cart
    assert len(cart.items) == 1

    payload = ujson.dumps(make_item())
    task = write_db.s(cart_id=cart_id, payload=payload).apply()
    assert task.status == "SUCCESS"
    cart = session.query(Cart).filter(Cart.id == cart_id).one()
    assert cart
    assert len(cart.items) == 2
