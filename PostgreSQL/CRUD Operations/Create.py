import psycopg2
from psycopg2 import Error
import Connections as conn

def createTable():
    
    try:
        connection = conn.openConnection()
        cursor = connection.cursor()
        conn.openConnection(connection)
        
    except (Exception, Error) as error:
        print("Error while creating the table", error)