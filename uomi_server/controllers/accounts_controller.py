import connexion
import six

from uomi_server import util


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
    return 'do some magic!'
