# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from uomi_server.test import BaseTestCase


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def test_open_new_account(self):
        """Test case for open_new_account

        add a new account including users involved
        """
        body = None
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/accounts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_account(self):
        """Test case for remove_account

        deletes an account given the account id
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/accounts/remove/{account_id}'.format(account_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_all_accounts(self):
        """Test case for user_all_accounts

        Get all accounts associated with a given user
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/accounts/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
