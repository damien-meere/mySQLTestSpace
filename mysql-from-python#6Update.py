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
        sql = "UPDATE Friends SET age =22 WHERE name = 'Bob';"
        cursor.execute(sql)
        connection.commit()

finally:
    #Close the connection
    connection.close()
