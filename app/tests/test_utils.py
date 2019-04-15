import uuid

import pytest

from tests.utils import make_item
from jobs.utils import validate_uuid, validate_payload


@pytest.mark.parametrize(
    "identifier",
    [
        "aaaaa",
        "123aaaa",
        "123",
        123,
        None,
        [],
        {},
        123.4
    ]
)
def test_validate_uuid_exceptions(identifier):

    with pytest.raises(ValueError):
        validate_uuid(identifier)


@pytest.mark.parametrize(
    "identifier",
    [
        uuid.uuid4(),
        str(uuid.uuid4())
    ]
)
def test_validate_uuid(identifier):
    assert validate_uuid(identifier) is None


@pytest.mark.parametrize(
    "data",
    [
        {},
        {"external_id": 123},
        {"external_id": "123", "value": "123"},
        {"external_id": "123", "name": 123},
        {"external_id": "123", "value": "123", "name": 123}
    ]
)
def test_validate_payload_exceptions(data):

    with pytest.raises(ValueError):
        validate_payload(data)


@pytest.mark.parametrize(
    "data",
    [
        {"external_id": "123"},
        {"external_id": "123", "value": 12},
        {"external_id": "123", "name": "apple"},
        {"external_id": "123", "name": "apple", "value": 12},
        make_item()
    ]
)
def test_validate_payload(data):

    assert validate_payload(data) is None
