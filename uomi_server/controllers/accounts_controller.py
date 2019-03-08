import connexion
import six

from uomi_server import util
from uomi_server.database_util.connection_manager import DatabaseConnectionManager
from uomi_server.database_util import orm
from uomi_server.database_util.orm import Account
from uomi_server.database_util.helper_queries import get_user_id, get_user_account_balance
from sqlalchemy.sql import text
from flask import jsonify
from datetime import datetime

db_conn_mgmt = DatabaseConnectionManager()


def open_new_account(body):  # noqa: E501
    """add a new account including users involved

     # noqa: E501

    :param body:
    :type body:

    :rtype: None
    """
    # May not work, but maybe
    # Expect the input command to have appropiate keys, if not return a 404
    try:
        # TODO: search database for user_ids that match whoever the user wants in account
        account_users = []
        account_users.append(body["current_user_id"])
        for email in body["user_emails"]:
            user_id = get_user_id(email)
            if user_id is None:
                return jsonify({"error": "specified user doesn't exist"}), 404
            account_users.append(user_id)
    except KeyError as kerr:
        return jsonify({"error": "did not receive correct params"}), 404

    db_conn_mgmt.connect_to_db()
    new_account = Account(account_users=account_users, last_updated=datetime.utcnow())
    db_conn_mgmt.db_session.add(new_account)
    db_conn_mgmt.db_session.commit()
    return jsonify(), 201


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
    filter_user = text(":x = ANY(account_users::int[])")
    db_conn_mgmt.connect_to_db()
    # Query on accounts using custom filter where the param is user_id, order by last_updated desc for ordering
    q = db_conn_mgmt.db_session.query(Account).filter(filter_user).params(x=user_id).order_by(Account.last_updated.desc()).all()
    db_conn_mgmt.disconnect_db()
    accounts_list = [account.dump() for account in q]
    # Get the balance for each account
    for account in accounts_list:
        account['acc_balance'] = get_user_account_balance(user_id, account['account_id'])
    return jsonify(accounts_list), 200
