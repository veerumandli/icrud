class SQLBuilder():
    @classmethod
    def __build_where(cls, filter: str):
        """
        Conditions: gt, lt, ge, le, eq
        Logical Operators: and, or
        Example: count eq 10 and status eq 1 ==> where count = 10 and status = 1

        """
        if filter == '':
            return ''
        else:
            # where_clause = 'where '+ filter.replace('eq', '=')
            # return where_clause
            conditions = {
                ' eq ': ' = ',
                ' gt ': ' > ',
                ' lt ': ' < ',
                ' ge ': ' >= ',
                ' le ': ' <= ',
                ' ne ': ' != '
            }
            column_map = {}
            for col, meta in cls.columns.items():
                if col != meta['key']:
                    column_map[col] = meta['key']

            for alias, column in column_map.items():
                filter = filter.replace(alias, column)

            build_where = f"WHERE {filter}"
            for key, value in conditions.items():
                build_where = build_where.replace(key, value)
            return build_where

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
    def all(cls, page=0, limit=0, filter=''):
        """
        Retrieve all records from the database table.

        Returns:
            A list of dictionaries representing all rows.

        Note:
            The subclass must implement get_connection() method to provide a database connection.
        """
        conn = None
        cursor = None
        conn = cls.get_connection()
        keys = []
        for col, meta in cls.columns.items():
            keys.append(f'{meta["key"]} as {col}')
        conditions = cls.__build_where(filter)
        if page and limit:
            sql = f"SELECT {', '.join(keys)} FROM {cls.table_name} {conditions} limit {limit} offset {(page-1)*limit}"
        else:
            sql = f"SELECT {', '.join(keys)} FROM {cls.table_name} {conditions}"

        print(sql)
        try:
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
        conn = None
        cursor = None
        conn = cls.get_connection()
        sql = f"SELECT * FROM {cls.table_name} WHERE {cls.slug_column} = '{id}' limit 0, 1"
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
