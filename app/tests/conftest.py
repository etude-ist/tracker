import os
import uuid

import pytest

from falcon import testing
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from resources.api import create


engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker()


@pytest.fixture()
def api_test_client():
    return testing.TestClient(create())


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()


@pytest.fixture(scope='function')
def fixed_uuid():
    return uuid.UUID('50b2cc9b-2fc9-4b05-bf48-4e0190f3cd6a')
