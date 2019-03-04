# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from uomi_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        adds a new user
        """
        body = None
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        delete a user from the app
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/users/{user_id}'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_info(self):
        """Test case for get_user_info

        get all user info for the specified user
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/users/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_query_all_users(self):
        """Test case for query_all_users

        get all registered users
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_net_balance(self):
        """Test case for user_net_balance

        retrieve net balance for a user
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/netBalance/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
