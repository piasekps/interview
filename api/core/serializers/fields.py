from marshmallow import fields, utils


class Date(fields.Date):

    def _deserialize(self, value, attr, data):
        """
        Deserialize an ISO8601-formatted date string to a :class:`datetime.date` object.
        """
        if not value:  # falsy values are invalid
            self.fail('invalid')
        try:
            return utils.from_iso_date(value, use_dateutil=False)
        except (AttributeError, TypeError, ValueError):
            self.fail('invalid')
