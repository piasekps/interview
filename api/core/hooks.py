from uuid import UUID

from falcon import HTTPNotFound


def get_instance(req, resp, resource, params, model_class):
    """
    Get instance of given model base on ID provided in URL under instance_key and attach it to request object.

    Args:
        req (falcon.request.Request): Request object
        resp (falcon.response.Response): Response object
        resource (class): API class
        params (dict): Query parameters
        model_class (core.db.base.Base): DB model

    Raises:
        falcon.HTTPNotFound: If instance with provided ID does not exist
    """
    instance_id = params.get('object_id')
    db_session = req.context.db_session

    if isinstance(instance_id, UUID):
        instance_id = instance_id.hex

    instance = model_class.get_by_id(db_session, instance_id)

    if not instance:
        raise HTTPNotFound

    req.context.instance = instance
