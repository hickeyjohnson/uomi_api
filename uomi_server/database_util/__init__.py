from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import os


try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    print("No DATABASE_URL detected on os.environ... Assuming localhost")
    DATABASE_URL = "postgresql://matthewhickey@localhost/uomi_db"

Session = sessionmaker()
engine = create_engine(DATABASE_URL)

Session.configure(bind=engine)

db_session = Session()
