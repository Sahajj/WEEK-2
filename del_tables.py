import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sahaj",
  password="1234",
  database="new_database"
)

mycursor = mydb.cursor()

# Deleting table
mycursor.execute("DROP TABLE Hospital")

