# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:27:26 2021

@author: Asish
"""
import psycopg2
from psycopg2 import Error

def openConnection():
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="Pradhan@1994",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydb")
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        return connection
    
def closeConnection(conn):
    try:
        
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        return cursor