from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ['DATABASE_URL']

Session = sessionmaker()
uri = "postgresql://matthewhickey@localhost/uomi_db"
engine = create_engine(DATABASE_URL)

Session.configure(bind=engine)

db_session = Session()
