import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pradhan@1994",
  database='p_table' 
)

print(mydb)