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
        print('Read all records:',record)
        cursor.close()
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while fetching the data", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")    
        
def readDataById(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        cursor = connection.cursor()
        sql = '''Select * from Student where roll_id = %s'''
        ar = []
        ar.append(id)
        cursor.execute(sql,ar)
        record = cursor.fetchall()
        cursor.close()
        print('Read only one record:',record)       
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while fetching the data", error)
    
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        
readData()
readDataById(1)