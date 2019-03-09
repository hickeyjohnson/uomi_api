import connexion
import six

from uomi_server import util
from datetime import datetime
from uomi_server.database_util.connection_manager import DatabaseConnectionManager
from uomi_server.database_util import orm
from uomi_server.database_util.helper_queries import get_user_id, get_user_account_balance
from uomi_server.database_util.orm import User
from flask import jsonify

db_conn_mgmt = DatabaseConnectionManager()

def create_user(body):  # noqa: E501
    """adds a new user

    Adds login information for a new user. # noqa: E501

    If the user is already created, no further action is taken, but user_id
    returned for the existing user.

    :param body: User object that must be added to the database
    :type body:

    :rtype: user_id
    """
    email = body['email']
    try:
        pw = body['pw']
    except KeyError as kerr:
        pw = None
    try:
        fb_token = body['fb_token']
    except KeyError as kerr:
        fb_token = None



    db_conn_mgmt.connect_to_db()
    user_id = get_user_id(email)
    if user_id != -1:
        return jsonify({'existing_user': True, 'user_id': user_id}), 200

    new_user = User(email=email, hashed_password=pw, fb_token=fb_token, first_name=body['first_name'],
                    last_name=body['last_name'], created_time=datetime.utcnow(), net_balance=0)

    db_conn_mgmt.db_session.add(new_user)
    db_conn_mgmt.db_session.commit()

    ret_dict = {"existing_user": False, "user_id": new_user.user_id}

    return jsonify(ret_dict), 201


def delete_user(user_id):  # noqa: E501
    """delete a user from the app

     # noqa: E501

    :param user_id: unique user_id
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_info(user_id):  # noqa: E501
    """get all user info for the specified user

     # noqa: E501

    :param user_id: unique user_id
    :type user_id: int

    :rtype: object
    """
    return 'do some magic!'


def query_all_users():  # noqa: E501
    """get all registered users

     # noqa: E501


    :rtype: None
    """
    # set instance of database management
    db_conn_mgmt.connect_to_db()
    q = db_conn_mgmt.db_session.query(User)
    db_conn_mgmt.disconnect_db()
    return jsonify([u.dump() for u in q])


def user_net_balance(user_id):  # noqa: E501
    """retrieve net balance for a user

     # noqa: E501

    :param user_id: unique user identifier
    :type user_id: int

    :rtype: None
    """
    db_conn_mgmt.connect_to_db()
    q = db_conn_mgmt.db_session.query(User.net_balance).filter(User.user_id == user_id).one()
    db_conn_mgmt.disconnect_db()
    return jsonify({"netBalance": q[0]})
