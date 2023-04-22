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
# PATIENTE

insert_patient = "INSERT INTO Patient VALUES (%s, %s, %s, %s, %s)"

values = [
    (1, 'John Doe', 35, 'M', '555-555-5555'),
    (2, 'Jane Doe', 28, 'F', '555-555-5555'),
    (3, 'Bob Johnson', 45, 'M', '555-555-5555')
]

mycursor.executemany(insert_patient, values)

# commit the changes to the database
mydb.commit()

# print the number of records inserted
print(mycursor.rowcount, "records inserted.")