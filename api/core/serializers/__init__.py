from marshmallow import fields, validate, validates_schema, Schema
from marshmallow.exceptions import ValidationError


class BaseSchema(Schema):
    class Meta:
        strict = True


class StrictSchema(BaseSchema):

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data, partial, many):
        """
        Checks if any unspecified data have been passed in the request body

        Args:
            data (dict): Serialized data passed in the request
            original_data (dict): Raw input data passed in the request
        """
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', list(unknown))


class BaseSearchSortGetRequestSchema(BaseSchema):
    search = fields.List(
        fields.String(),
        required=False,
        missing=[]
    )
    sorting = fields.Str(required=False)


class BasePaginatedRequestSchema(BaseSchema):
    size = fields.Int(
        missing=10,
        required=False,
        validate=validate.Range(min=1, max=1000)
    )
    page = fields.Int(
        missing=0,
        required=False,
        validate=validate.Range(min=0)
    )
