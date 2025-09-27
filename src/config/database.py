import mysql.connector
from mysql.connector import errorcode


try:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456789",
        database="bitly")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Database connected successfully")


def fetchRaw(query):
    if cnx and cnx.is_connected():
        with cnx.cursor(dictionary=True) as cursor:
            result = cursor.execute(query)
            rows = []
            for row in cursor:
                rows.append(row)
        return rows
    else:
        print("Could not connect")


def fetchOneRaw(query):
    data = fetchRaw(query)
    if len(data) > 0:
        return data[0]
    else:
        return None


def insertRaw(query):
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute(query)
            last_insert_row_id = cursor.lastrowid
        cnx.commit()
        return last_insert_row_id
    else:
        print("Could not connect")


def updateRaw(query):
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute(query)
        cnx.commit()
    else:
        print("Could not connect")
