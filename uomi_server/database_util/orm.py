from sqlalchemy import create_engine, Column, Numeric, DateTime, String, Sequence, Integer  # noqa
from sqlalchemy.dialects.postgresql import MONEY
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

# class Account(Base):
#     __tablename__ = 'accounts'
#     pass
#
# class Transaction(Base):
#     pass


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
