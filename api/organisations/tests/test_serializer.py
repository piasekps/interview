import pytest
from falcon.testing import TestCase
from marshmallow import ValidationError

from organisations.serializers import OrganisationPostRequestSchema

class OrganisationSerializerTestCase(TestCase):

    def test_validate_name_too_long_name(self):
        with pytest.raises(ValidationError, match='Longer than maximum length 128.'):
            OrganisationPostRequestSchema().load({"name": "a" * 500})
