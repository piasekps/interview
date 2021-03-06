from unittest.mock import ANY

from falcon import HTTP_201

from core.tests.base import BaseApiTestCase
from organisations.models import Organisation
from users.models import User


class BaseUserTestCase(BaseApiTestCase):
    def create_organisation(self, name='Die Hard', status=None):
        """
        Helper to create Organisation instance.

        Args:
            name (str): Organisation name
            status (int): OrganisationStatus value
        """
        params = {
            'name': name
        }
        if status:
            # default status is ENABLED
            params['status'] = status

        return Organisation.create(db_session=self.db_session, **params)

    def create_user(self, organisation_id, first_name='John', last_name='McClane', email='john@example.com'):
        """
        Helper to create User instance.

        Args:
            organisation_id (int): Organisation ID
            first_name (str): User first name
            last_name (str): User last name
            email (str): User email
        """
        return User.create(
            db_session=self.db_session,
            first_name=first_name,
            last_name=last_name,
            email=email,
            organisation_id=organisation_id
        )


class UserPostTestCase(BaseUserTestCase):
    def test_create_user(self):
        organisation = self.create_organisation('Die Hard')

        response = self.request_post(
            path='/v1/users',
            status=HTTP_201,
            body={
                'first_name': 'John',
                'last_name': 'McClean',
                'email': 'john@example.com',
                'organisation_id': organisation.id
            }
        )
        self.assertDictEqual(
            response.json,
            {"id": ANY, "name": "John McClean", "email": "john@example.com"}
        )
