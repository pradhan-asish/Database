import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="asish",
  password="Pradhan@1994",
  database='p_table' 
)

print(mydb)