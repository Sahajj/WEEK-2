# using the mysql-connector-pthon 
import mysql.connector

# giving details to connet to mysql 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "sahaj",
    password = "1234",
    database = "week2"  # using the database that i created.
)

# initalizing mydbcursor to execute mysql commands
mycursor = mydb.cursor()

insert_Doc = "INSERT INTO Doctor  VALUES (%s, %s, %s, %s)"

values = [
   (1, 'Dr. Smith', 'Cardiologist', 1),
    (2, 'Dr. Johnson', 'Neurologist', 2),
    (3, 'Dr. Williams', 'Oncologist', 3)
]


# Executing the INSERT statement with the values
mycursor.executemany(insert_Doc, values)

# commit the changes to the database
mydb.commit()

# print the number of records inserted
print(mycursor.rowcount, "records inserted.")