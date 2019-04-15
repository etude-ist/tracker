import uuid


def validate_payload(data):
    if data.get('external_id') is None:
        raise ValueError

    if not isinstance(data.get('external_id'), str):
        raise ValueError

    if 'value' in data and not isinstance(data.get('value'), (int, float)):
        raise ValueError

    if 'name' in data and not isinstance(data.get('name'), str):
        raise ValueError


def validate_uuid(cid):
    if isinstance(cid, uuid.UUID):
        return

    if isinstance(cid, str):
        uuid.UUID(cid)

    if not isinstance(cid, str):
        raise ValueError
