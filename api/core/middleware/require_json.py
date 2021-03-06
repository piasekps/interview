import falcon


class RequireJSON:

    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='http://docs.examples.com/api/json'
            )

        if req.method in ('POST', 'PUT') and not req.content_type or 'application/json' not in req.content_type:
            raise falcon.HTTPUnsupportedMediaType(
                'This API only supports requests encoded as JSON.',
                href='http://docs.examples.com/api/json'
            )
