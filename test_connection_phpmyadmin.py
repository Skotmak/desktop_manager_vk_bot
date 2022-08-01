'''
import pymysql

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="lol", passwd="4444", database="test_con")
cursor = connection.cursor()
# some other statements  with the help of cursor
cursor.execute("""SELECT * FROM test""")
print(cursor)
connection.close()
'''

'''
import mysql.connector

database_connection = mysql.connector.connect(
   host="localhost",
   port=3306,
   user="lol",
   password="4444",
   database="test_con"
)

print(database_connection)
'''


# '''
# Module Imports

# Connect to MariaDB Platform

import mariadb
conn = mariadb.connect(
    user="lol",
    password="4444",
    host="localhost",
    port=3306,
    database="test_con")


# Get Cursor
cur = conn.cursor()
# '''
