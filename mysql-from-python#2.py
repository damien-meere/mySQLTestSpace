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
        sql = """CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);"""
        cursor.execute(sql)

finally:
    #Close the connection
    connection.close()
