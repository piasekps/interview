from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

import settings
from core.db.engine import engine


Session = sessionmaker(
    bind=engine,
    **settings.SQLALCHEMY['sessionmaker']
)


@contextmanager
def session_manager():
    """Provide a transactional scope around a series of operations."""
    db_session = Session()

    try:
        yield db_session
        db_session.commit()
    except:  # noqa
        db_session.rollback()
        raise
    finally:
        db_session.close()

