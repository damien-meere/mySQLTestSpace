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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "Select * From Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)

finally:
    #Close the connection
    connection.close()
