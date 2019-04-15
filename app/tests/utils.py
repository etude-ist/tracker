import uuid

from random import randint


def make_item():
    base_item = {
        "external_id": str(randint(1, 10**6))
    }
    if randint(0, 1):
        base_item['value'] = randint(1, 10**3)
    if randint(0, 1):
        base_item['name'] = str(uuid.uuid4())
    return base_item


def fake_after_return(status, retval, task_id, args, kwargs, einfo):
    pass
