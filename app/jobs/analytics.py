import ujson
import uuid

from celery.exceptions import InvalidTaskError

from jobs.base import Task
from jobs.utils import validate_payload, validate_uuid
from models import Cart, Item
from worker import app


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


@app.task(bind=True, base=Task, name='write_db')
def write_db(self, cart_id, payload):
    try:
        data = ujson.loads(payload)
        validate_payload(data)
        validate_uuid(cart_id)
    except ValueError:
        raise InvalidTaskError

    cart = get_or_create(self.session, Cart, **{'id': cart_id})
    item = Item(
        id=uuid.uuid4(),
        cart_id=cart_id,
        external_id=data.get('external_id'),
        value=data.get('value'),
        name=data.get('name')
    )
    cart.items.append(item)
    self.session.commit()
