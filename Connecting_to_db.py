# using the mysql-connector-pthon 
import mysql.connector

# giving details to connet to mysql 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "sahaj",
    password = "1234",
    database = "my_info"  # using the database that i created.
)

# initalizing mydbcursor to execute mysql commands
mycursor = mydb.cursor()

# Creating tables 
mycursor.execute("CREATE TABLE  customers2 (name VARCHAR(255), Address VARCHAR(255));")

# checking if the tables exist or not
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)