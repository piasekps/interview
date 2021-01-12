import importlib
import os


POSTGRESQL = {
    "engine": "postgresql+psycopg2",
    "host": os.environ.get("POSTGRES_HOST"),
    "port": 5432,
    "username": "interview",
    "password": "interview",
    "db_name": "",
    "pool_size": 10,
    "application_name": "interview",
}


SQLALCHEMY = {
    "sessionmaker": {"expire_on_commit": False},
    "debug": False,  # choose between False, True, 'debug'
}


API_VERSIONS = {
    "available": ["v1", "v2"],
    "current": "v2",
}


ENVIRONMENT = os.getenv('API_ENV', 'local')
env_settings = importlib.import_module(f'settings.{ENVIRONMENT}')

for setting in dir(env_settings):
    setting_value = getattr(env_settings, setting)

    try:
        locals()[setting].update(setting_value)
    except (AttributeError, KeyError):
        locals()[setting] = setting_value
