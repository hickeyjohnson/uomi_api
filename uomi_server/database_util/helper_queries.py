from uomi_server.database_util.orm import User, Account
from uomi_server.database_util import orm
from sqlalchemy import func
from flask import jsonify
from uomi_server.database_util import db_session

def get_user_id(email):
    """
    will retrieve a user_id from the database given a user's email.

    returns the user_id if it is found, None otherwise
    """
    # set instance of database management
    q = db_session.query(User).filter_by(email=email).one_or_none()
    if q is not None:
        return q.user_id
    else:
        return -1

def get_user_account_balance(user_id, account_id):
    """
    will retrive the balance of an account for a user
    """
    q = db_session.query(func.public.calc_account_balance(user_id, account_id)).one()
    acc_bal = q[0]
    return acc_bal

def get_account_size(account_id):

    q = db_session.query(Account).filter(Account.account_id == account_id).one()

    return len(q.account_users)
