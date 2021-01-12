from pytest import fixture
from sqlalchemy_utils import database_exists, create_database, drop_database

from core.db.create_tables import create_all_tables
from core.db.engine import engine
from core.db.session import Session


@fixture(scope='session', autouse=True)
def create_test_database():
    """
    Prepare database for tests.

    This fixture creates all tables and extensions in PostgreSQL database at
    the beginning of all tests and delete everything at the end of all tests.
    """

    def delete_test_database():
        """
        Delete database if exists.
        """
        if database_exists(engine.url):
            drop_database(engine.url)

    delete_test_database()

    # Create database
    create_database(engine.url)

    connection = engine.connect()
    connection.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    connection.close()

    # Create all tables
    create_all_tables()

    yield

    delete_test_database()


@fixture(scope='function', autouse=True)
def db_transaction():
    """
    Create transaction before every single test and rollback everything
    at the end of test.
    """
    connection = engine.connect()
    transaction = connection.begin()
    Session.configure(bind=connection)

    yield

    transaction.rollback()
    connection.close()
