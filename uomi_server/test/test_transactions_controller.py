# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from uomi_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_add_transaction(self):
        """Test case for add_transaction

        add transaction to an account
        """
        body = None
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/transactions/{account_id}'.format(account_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_transaction(self):
        """Test case for delete_transaction

        removes a transaction from an account
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/transactions/remove/{transaction_id}'.format(transaction_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_transactions(self):
        """Test case for find_all_transactions

        get all transactions within an account
        """
        response = self.client.open(
            '/matthickey709/uomi_api/1.0.0/transactions/{account_id}'.format(account_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
