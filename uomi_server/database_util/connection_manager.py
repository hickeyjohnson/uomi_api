from uomi_server.database_util import orm

class DatabaseConnectionManager():
    """
    Class for managing connections to database
    """

    def __init__(self):
        db_session = None

    def connect_to_db(self):
        self.db_session = orm.init_db("postgresql://matthewhickey@localhost/uomi_db")

    def disconnect_db(self):
        self.db_session.remove()
