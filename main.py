# using the mysql-connector-pthon 
import mysql.connector

# giving details to connet to mysql 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "sahaj",
    password = "1234"
)

# initalizing mydbcursor to execute mysql commands
mydbcursor = mydb.cursor()

# Creating data base 
mydbcursor.execute("CREATE DATABASE week2")