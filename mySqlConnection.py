import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Pradhan@1994",
  database='p_table' 
)

print(mydb)