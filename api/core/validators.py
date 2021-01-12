import falcon
import sqlalchemy

from marshmallow import ValidationError

from core.db.session import session_manager


def validate_object_id(req, resp, resource, params, model_class):
    """
    Validates if ID passed in URL is valid number.

    Args:
        req (falcon.request.Request): Request object
        resp (falcon.response.Response): Response object
        resource (class): API class
        params (dict): Query parameters
        model_class (sqlalchemy.ext.declarative.api.DeclarativeMeta): DB Model

    Raises:
        (falcon.HTTPBadRequest) if ID passed in URL is not valid number.
    """
    object_id = params.get('object_id')
    if not object_id.isdigit():
        raise falcon.HTTPBadRequest(f'Invalid {model_class.__name__} ID')


def validate_instance_of_model_exists_by_id(model, instance_id):
    """
    Validates if instance of given model with provided ID exists.

    Args:
        model (class): Model class
        instance_id (int): Instance ID

    Raises:
        (ValidationError): Instance with provided ID of given model does not exist
    """
    with session_manager() as db_session:
        exists = db_session.query(
            sqlalchemy.exists().where(model.id == instance_id)
        ).scalar()

        if not exists:
            raise ValidationError(f'{model.__name__} with given ID ({instance_id}) does not exist')
