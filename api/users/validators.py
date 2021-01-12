import sqlalchemy

from marshmallow.exceptions import ValidationError

from core.db.session import session_manager
from users.models import User


def validate_unique_user_email(email):
    """
    Validates if email already was used by another User.

    Args:
        email (str): Email to validate

    Raises:
        (ValidationError): Email already exists
    """
    with session_manager() as db_session:
        exists = db_session.query(
            sqlalchemy.exists().where(
                User.email == email
            )
        ).scalar()

        if exists:
            raise ValidationError(f'User email {email} already exists')
