from falcon import HTTPNotFound

from settings import API_VERSIONS


class VersionMiddleware:
    """
    Checks if provided api_version URL parameter is a correct version number,
    if version is different then current runs necessary conversion functions
    on request and response
    """
    def process_resource(self, req, resp, resource, params):
        if req.method == 'OPTIONS' or 'api_version' not in params:
            return

        version = params.pop('api_version')
        if version not in API_VERSIONS['available']:
            raise HTTPNotFound(
                title='Unsupported version',
                description=f'Provided version number: {version} is not supported'
            )

        req.context['api_version'] = version
