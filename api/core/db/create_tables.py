from os.path import dirname, realpath, join

from alembic import command
from alembic.config import Config

from settings import POSTGRESQL

# import models here
from organisations.models import Organisation
from users.models import User


def create_all_tables(configure_logger=True):
    path = join(dirname(dirname(dirname(realpath(__file__)))), 'alembic.ini')
    config = Config(path)
    config.attributes['configure_logger'] = configure_logger
    config.set_main_option(
        'sqlalchemy.url',
        '{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(**POSTGRESQL)
    )

    command.upgrade(config, 'head')


if __name__ == "__main__":
    create_all_tables()
