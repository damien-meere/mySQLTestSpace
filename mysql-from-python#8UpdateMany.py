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
        rows = [(20, 'Bob'), (57, 'Jim'), (35, 'Alan'), (68, 'Brian')]
        sql = "UPDATE Friends SET age = %s WHERE name = %s;"
        cursor.executemany(sql, rows)
        connection.commit()

finally:
    #Close the connection
    connection.close()
