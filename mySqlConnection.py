import mySql.connector
mydb = mySql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)