import connexion
import six

from uomi_server import util
from uomi_server.database_util.connection_manager import DatabaseConnectionManager
from uomi_server.database_util import orm
from uomi_server.database_util.orm import Account
from sqlalchemy.sql import text
from flask import jsonify

db_conn_mgmt = DatabaseConnectionManager()


def open_new_account(body):  # noqa: E501
    """add a new account including users involved

     # noqa: E501

    :param body:
    :type body:

    :rtype: None
    """
    return 'do some magic!'


def remove_account(account_id):  # noqa: E501
    """deletes an account given the account id

     # noqa: E501

    :param account_id: unique account identifier
    :type account_id: int

    :rtype: None
    """
    return 'do some magic!'


def user_all_accounts(user_id):  # noqa: E501
    """Get all accounts associated with a given user

     # noqa: E501

    :param user_id: unique user_id
    :type user_id: int

    :rtype: object
    """

    # Custom filter for getting all accounts where user is a part of
    filter_user = text(
        ":x = ANY(account_users::int[])"
    )
    db_conn_mgmt.connect_to_db()
    # Query on accounts using custom filter where the param is user_id
    q = db_conn_mgmt.db_session.query(Account).filter(filter_user).params(x=user_id).all()
    db_conn_mgmt.disconnect_db()
    return jsonify([account.dump() for account in q])
