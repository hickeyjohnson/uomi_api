from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

Session = sessionmaker()
uri = "postgresql://matthewhickey@localhost/uomi_db"
engine = create_engine(uri)

Session.configure(bind=engine)

db_session = Session()
