# Requirements

- [PostgreSQL 10.10](https://www.postgresql.org)
- [Python 3.7.4](https://www.python.org)

# Libraries

- [Falcon](https://falcon.readthedocs.io)
- [Marshmallow](https://marshmallow.readthedocs.io)
- [SQLAlchemy](http://www.sqlalchemy.org)
- [Alembic](http://alembic.zzzcomputing.com)
- [Marshmallow SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.io)
- [pytest](http://doc.pytest.org)

# Docker

    ./docker.sh up
    ./docker.sh --help

***


## Alembic migrations

1. Create up to date database from scratch

        python core/db/create_tables.py

2. Update database to most recent migration

        alembic upgrade head

3. Autogenerate migration

        alembic revision --autogenerate -m "Migration message"
