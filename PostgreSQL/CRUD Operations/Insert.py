import psycopg2
from psycopg2 import Error

def insertStudent(id,name,clas):
    
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        
        cursor = connection.cursor()
        
        sql = '''Insert into student(roll_id,name,class) Values(%s,%s,%s)'''
        data  = []
        data.append(id)
        data.append(name)
        data.append(clas)
        cursor.execute(sql,data)
        print('Data inserteed succefully')
        connection.commit()
        connection.close()
    
    except (Exception, Error) as error:
        print("Error while creating the table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
insertStudent(3,'Deepak',5)
