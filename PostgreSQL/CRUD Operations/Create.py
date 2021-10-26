import psycopg2
from psycopg2 import Error

def createTable():
    
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        
        
        record = cursor.fetchone()
        print('The version',record)
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while creating the table", error)
        
createTable()