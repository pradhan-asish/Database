import psycopg2
from psycopg2 import Error

def readData():
    
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        cursor = connection.cursor()
        sql = '''Select * from Student'''
        cursor.execute(sql)
        record = cursor.fetchall()
        print(record)
        
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while fetching the data", error)
        
def readDataById(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        cursor = connection.cursor()
        sql = '''Select * from Student where id = %s'''
        cursor.execute(sql,id)
        record = cursor.fetchall()
        print(record)
        
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while fetching the data", error)
        
readData()
