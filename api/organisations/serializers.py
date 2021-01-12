from marshmallow.fields import Integer, String
from marshmallow.validate import OneOf, Length

from core.serializers import BasePaginatedRequestSchema, BaseSearchSortGetRequestSchema, StrictSchema
from organisations.enums import OrganisationStatus
from organisations.validators import validate_unique_organisation_name


class OrganisationGetRequestSchema(BaseSearchSortGetRequestSchema, BasePaginatedRequestSchema):
    pass


class OrganisationPatchRequestSchema(StrictSchema):
    name = String(
        required=True,
        validate=Length(max=128)
    )
    status = Integer(
        required=True,
        validate=OneOf(OrganisationStatus.values())
    )


class OrganisationPostRequestSchema(StrictSchema):
    name = String(
        required=True,
        validate=[Length(max=128), validate_unique_organisation_name]
    )
