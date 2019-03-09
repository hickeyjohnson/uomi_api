from uomi_server.database_util.orm import User, Account
from uomi_server.database_util.connection_manager import DatabaseConnectionManager
from uomi_server.database_util import orm
from sqlalchemy import func
from flask import jsonify

db_conn_mgmt = DatabaseConnectionManager()


def get_user_id(email):
    """
    will retrieve a user_id from the database given a user's email.

    returns the user_id if it is found, None otherwise
    """
    # set instance of database management
    db_conn_mgmt.connect_to_db()
    q = db_conn_mgmt.db_session.query(User).filter_by(email=email).one_or_none()
    db_conn_mgmt.disconnect_db()
    if q is not None:
        return q.user_id
    else:
        return -1

def get_user_account_balance(user_id, account_id):
    """
    will retrive the balance of an account for a user
    """
    data = db_conn_mgmt.connect_to_db()
    q = db_conn_mgmt.db_session.query(func.public.calc_account_balance(user_id, account_id)).one()
    print("11111111111111111")
    acc_bal = q[0]
    print(acc_bal)
    return acc_bal
