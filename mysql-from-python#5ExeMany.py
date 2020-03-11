import os 
import datetime
import pymysql

#Get username
username = os.getenv('C9_USER')

#Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password="",
                            db='Chinook')

try:
    #Run a Query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1954-04-02 23:04:56"),
                ("Alan", 33, "1968-12-08 23:04:56"),
                ("Brian", 67, "1945-06-24 23:04:56")]
        sql = "INSERT INTO Friends VALUES (%s, %s, %s);"
        cursor.executemany(sql, rows)
        connection.commit()

finally:
    #Close the connection
    connection.close()
