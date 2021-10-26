from psycopg2 import Error
import Connections as conn

def createTable():
    
    try:
        connection = conn.openConnection()
        cursor = connection.cursor()
        
        
        cursor.execute("SELECT version();")
        
        conn.openConnection(connection)
        
    except (Exception, Error) as error:
        print("Error while creating the table", error)
        
createTable()