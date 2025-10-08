class SQLBuilder():
    @classmethod
    def create(cls, **kwargs):
        """
        Insert a new record into the database table.

        Args:
            **kwargs: Column-value pairs to insert.

        Returns:
            The last inserted row ID.

        Note:
            The subclass must implement get_connection() method to provide a database connection.
        """
        keys = []
        values = []
        placeholders = []

        for col, meta in cls.columns.items():
            if col in kwargs:
                keys.append(col)
                values.append(kwargs[col])
                placeholders.append("%s")

        sql = f"INSERT INTO {cls.table_name} ({', '.join(keys)}) VALUES ({', '.join(placeholders)})"
        conn = None
        cursor = None
        try:
            conn = cls.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def all(cls):
        """
        Retrieve all records from the database table.

        Returns:
            A list of dictionaries representing all rows.

        Note:
            The subclass must implement get_connection() method to provide a database connection.
        """
        keys = []
        for col, meta in cls.columns.items():
            keys.append(f"{meta["key"]} as {col}")
        sql = f"SELECT {', '.join(keys)} FROM {cls.table_name}"
        conn = None
        cursor = None
        try:
            conn = cls.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def find(cls, id):
        """
        Retrieve a single record by primary key.

        Args:
            id: The primary key value to search for.

        Returns:
            A dictionary representing the found row or None if not found.

        Note:
            The subclass must implement get_connection() method to provide a database connection.
        """
        sql = f"SELECT * FROM {cls.table_name} WHERE {cls.primary_key} = %s"
        conn = None
        cursor = None
        try:
            conn = cls.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, (id,))
            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
