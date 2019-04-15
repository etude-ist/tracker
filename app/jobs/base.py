import os
import celery
import sqlalchemy as sq

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class Task(celery.Task):

    _engine = None
    _session = None

    @property
    def engine(self):
        if self._engine is None:
            self._engine = sq.create_engine(os.getenv('DATABASE_URL'))
        return sessionmaker(bind=self._engine)

    @property
    def session(self):
        if self._session is None:
            session_factory = self.engine
            self._session = scoped_session(session_factory)
        return self._session

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if hasattr(self, '_session'):
            self._session.remove()
        if hasattr(self, '_engine'):
            self._engine.engine.dispose()
