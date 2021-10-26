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
        
        sql = '''CREATE TABLE IF NOT EXISTS student (roll_id INT NOT NULL,
                name Text NOT NULL,
                class INT NOT NULL,
                PRIMARY KEY (roll_id))'''
        cursor.execute(sql)
        print('Table created sucessully')
        connection.commit()
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while creating the table", error)
        
createTable()