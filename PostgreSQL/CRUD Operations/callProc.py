# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:03:40 2021

@author: HP
"""

import psycopg2
from psycopg2 import Error


def callProc(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="Pradhan@1994",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydb")
        
        cur = connection.cursor()
        cur.execute('readstudentdetails' ,[id])
        
        rec = cur.fetchall()
        
        print('The result is :',rec)
        
        connection.close()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        return connection