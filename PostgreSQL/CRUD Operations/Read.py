import psycopg2
from psycopg2 import Error

def readData():
    
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Pradhan@1994",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb")
        