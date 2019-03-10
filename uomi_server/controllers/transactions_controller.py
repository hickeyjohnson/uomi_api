import connexion
import six

from uomi_server import util
from uomi_server import util
from uomi_server.database_util import orm
from uomi_server.database_util.orm import Transaction
from uomi_server.database_util.helper_queries import get_user_id, get_user_account_balance, get_account_size
from sqlalchemy.sql import text
from flask import jsonify
from datetime import datetime
from uomi_server.database_util import db_session

def add_transaction(account_id, body):  # noqa: E501
    """add transaction to an account

     # noqa: E501

    :param account_id: account unique identifier
    :type account_id: int
    :param body: info about the transaction to be added
    :type body:

    :rtype: None
    """
    return 'do some magic!'


def delete_transaction(transaction_id):  # noqa: E501
    """removes a transaction from an account

     # noqa: E501

    :param transaction_id: transaction item unique identifier
    :type transaction_id: int

    :rtype: None
    """
    return 'do some magic!'


def find_all_transactions(account_id, user_id):  # noqa: E501
    """get all transactions within an account

     # noqa: E501

    :param account_id:
    :type account_id: int

    :rtype: None
    """

    query_filter = ""

    # query the database
    q = db_session.query(Transaction).filter(Transaction.account_id == account_id).order_by(Transaction.transaction_timestamp.desc()).all()
    transactions_list = [transaction.dump() for transaction in q]
    # find number of users in the account
    account_size = get_account_size(account_id)
    # Iterate through transactions list, dividing non-user transactions by account_size-1
    for transaction in transactions_list:
        if transaction['user_owed'] != user_id:
            transaction['amount'] = -transaction['amount'] / (account_size - 1)
    return_object = {"account_balance": get_user_account_balance(user_id, account_id),
                     "transactions_list" : transactions_list}



    return jsonify(return_object), 200
