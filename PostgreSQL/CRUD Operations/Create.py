import psycopg2
from psycopg2 import Error
import Connections as conn

def createTable():
    
    try:
        connections = conn.openConnection()
        cursor = connection.cursor()
        conn.openConnection(connections)
        
    except (Exception, Error) as error:
        print("Error while closing the connection to PostgreSQL", error)