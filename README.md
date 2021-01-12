# Requirements

- [PostgreSQL 10.10](https://www.postgresql.org)
- [Python 3.7.4](https://www.python.org) (2016-11-30: It should work with Python 3.x)

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


# Virtualenv

  1. Install dependencies.

        pip install -r requirements.txt

  2. Add api/ to PYTHONPATH.

        add2virtualenv api

  3. Set environment variables (export them in `$VIRTUAL_ENV/bin/postactivate`):

        API_ENV=local
        POSTGRES_HOST=localhost

  4. Install PostgreSQL

    - create user with ```interview``` as a name and ```interview``` as a password.

            createuser --password interview # type 'interview' when asked for password
            sudo su - postgres
            psql
            alter user interview with createdb;

    - edit `pg_hba.conf` file (/etc/postgresql/{version}/main): change `local all all md5` to `local all all trust` (restart the service afterward with `sudo service postgresql restart`)

    - create database ```interview```

  5. Run api.

        gunicorn --reload --bind=0.0.0.0:8081 --timeout 3600 api.app:app

  6. [http://localhost:8081](http://localhost:8081)


## Run tests

    API_ENV=tests pytest -s

## Coverage report

    API_ENV=tests pytest --cov=api


## Alembic migrations

1. Create up to date database from scratch

        python core/db/create_tables.py

2. Update database to most recent migration

        alembic upgrade head

3. Autogenerate migration

        alembic revision --autogenerate -m "Migration message"
