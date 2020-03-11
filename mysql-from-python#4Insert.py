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
        row = ("Bob", 21, "1990-02-06 23:04:56")
        sql = "INSERT INTO Friends VALUES (%s, %s, %s);"
        cursor.execute(sql, row)
        connection.commit()

finally:
    #Close the connection
    connection.close()
