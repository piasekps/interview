from sqlalchemy import create_engine

import settings


engine = create_engine(
    "{engine}://{username}:{password}@{host}:{port}/{db_name}".format(**settings.POSTGRESQL),
    pool_size=settings.POSTGRESQL["pool_size"],
    connect_args={"application_name": settings.POSTGRESQL["application_name"]},
    echo=settings.SQLALCHEMY["debug"],
)
