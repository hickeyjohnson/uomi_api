import connexion
import six

from uomi_server import util


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


def find_all_transactions(account_id):  # noqa: E501
    """get all transactions within an account

     # noqa: E501

    :param account_id: 
    :type account_id: int

    :rtype: None
    """
    return 'do some magic!'
