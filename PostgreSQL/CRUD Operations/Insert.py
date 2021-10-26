import psycopg2
from psycopg2 import Error

def insertStudent():
    
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        
        cursor = connection.cursor()
        
        sql = '''Insert into student(roll_id,name,class) Values(1,'Asish',10)'''
        cursor.execute(sql)
        
    
    except (Exception, Error) as error:
        print("Error while creating the table", error)
        
        