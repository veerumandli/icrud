import mysql.connector
from mysql.connector import errorcode
from src.config.database import host, port, user, password, database
from src.core.SQLBuilder import SQLBuilder


class Model(SQLBuilder):
    """
    Base Model class providing ORM-like features.
    """
    table_name = ""
    slug_column = ""
    columns = {}
    time_stamps = True
    primary_key = "id"
    created_at = "created_at"
    modified_at = "modified_at"
    validations = []

    def __init__(self, **kwargs):
        """
        Initialize the model instance with given keyword arguments.
        """
        for col in self.columns.keys():
            setattr(self, col, kwargs.get(col))

    @classmethod
    def _get_connection(cls):
        """
        Get a database connection.
        """
        return cls.get_connection()

    @classmethod
    def get_connection(cls):
        """
        Create and return a new MySQL database connection using configuration values.
        Handles authentication and database errors gracefully.
        """
        if cls.slug_column == "":
            cls.slug_column = cls.primary_key
        if cls.time_stamps:
            if cls.created_at != "":
                cls.columns[cls.created_at] = {
                    "key": cls.created_at,
                    "type": "timestamp",
                }
            if cls.modified_at != "":
                cls.columns[cls.modified_at] = {
                    "key": cls.modified_at,
                    "type": "timestamp",
                }
        try:
            conn = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            return conn
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception(
                    "Database authentication failed: Check your username or password.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception(f"Database '{database}' does not exist.")
            else:
                raise Exception(f"Database connection error: {err}")

    def before(self):
        """
        Lifecycle hook called before any operation.
        """
        pass

    def after(self):
        """
        Lifecycle hook called after any operation.
        """
        pass

    def beforeInsert(self):
        """
        Lifecycle hook called before insert operation.
        """
        pass

    def afterInsert(self):
        """
        Lifecycle hook called after insert operation.
        """
        pass

    def beforeUpdate(self):
        """
        Lifecycle hook called before update operation.
        """
        pass

    def afterUpdate(self):
        """
        Lifecycle hook called after update operation.
        """
        pass

    def beforeDelete(self):
        """
        Lifecycle hook called before delete operation.
        """
        pass

    def afterDelete(self):
        """
        Lifecycle hook called after delete operation.
        """
        pass
