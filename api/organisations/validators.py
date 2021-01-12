from functools import partial

import sqlalchemy

from marshmallow.exceptions import ValidationError
from sqlalchemy import func

from core.db.session import session_manager
from core.validators import validate_instance_of_model_exists_by_id
from organisations.models import Organisation


validate_organisation_exists = partial(
    validate_instance_of_model_exists_by_id, Organisation
)


def validate_unique_organisation_name(name):
    """
    Validates if provided english name already used by another Organisation.

    Args:
        name (str): Organisation name

    Raises:
        (ValidationError): Organisation with provided name already exists
    """
    with session_manager() as db_session:
        exists = db_session.query(
            sqlalchemy.exists().where(
                func.lower(Organisation.name) == func.lower(name)
            )
        ).scalar()

        if exists:
            raise ValidationError(f'Organisation name {name} already exists')
