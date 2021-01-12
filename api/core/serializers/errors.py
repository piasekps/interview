def error_serializer(req, resp, exception):
    """
    Force error response content type and return always 'application/json'.

    Args:
        req: Falcon request.
        resp: Falcon response.
        exception: Falcon exception.
    """

    resp.body = exception.to_json()
    resp.content_type = 'application/json'
