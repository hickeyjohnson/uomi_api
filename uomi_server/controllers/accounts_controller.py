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
    custom_q = text(
        "SELECT account_id, account_users, last_updated FROM accounts WHERE :x = ANY(account_users::int[])"
    )
    # FIXME: make it map to Account ORM automatically!
    params = {'x': user_id}
    db_conn_mgmt.connect_to_db()
    q = db_conn_mgmt.db_session.execute(clause=custom_q, mapper=Account(), params=params).fetchall()
    result = []
    db_conn_mgmt.disconnect_db()
    for row in q:
        result.append({'account_id': row[0],
                    'account_users' : row[1],
                    'last_updated': row[2]})
    return jsonify(result)
