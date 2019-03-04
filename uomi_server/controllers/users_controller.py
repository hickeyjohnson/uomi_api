import connexion
import six

from uomi_server import util


def create_user(body):  # noqa: E501
    """adds a new user

    Adds login information for a new user # noqa: E501

    :param body: User object that must be added to the database
    :type body:

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


def user_net_balance(user_id):  # noqa: E501
    """retrieve net balance for a user

     # noqa: E501

    :param user_id: unique user identifier
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'
