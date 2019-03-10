from sqlalchemy import create_engine, Column, Numeric, DateTime, String, Sequence, Integer  # noqa
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    """
    Class to represent a user object from the DB
    """
    __tablename__ = 'users'
    user_id = Column(Integer(), Sequence('users_id_seq'), primary_key=True)
    email = Column(String())
    hashed_password = Column(String())
    first_name = Column(String())
    last_name = Column(String())
    fb_token = Column(String())
    net_balance = Column(Numeric())
    created_time = Column(DateTime())

    def dump(self):
        return dict([(key, val) for key, val in self.__dict__.items() if key[0] != '_'])

class Account(Base):
    __tablename__ = 'accounts'
    account_id = Column(Integer(), Sequence('accounts_id_seq'), primary_key=True)
    last_updated = Column(DateTime())
    account_users = Column(postgresql.ARRAY(Integer))

    def dump(self):
        return dict([(key, val) for key, val in self.__dict__.items() if key[0] != '_'])

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer(), Sequence('transactions_id_seq'), primary_key=True)
    account_id = Column(Integer())
    trans_label = Column(String())
    amount = Column(Numeric())
    user_owed = Column(Integer())
    transaction_timestamp = Column(DateTime())

    def dump(self):
        return dict([(key, val) for key, val in self.__dict__.items() if key[0] != '_'])
