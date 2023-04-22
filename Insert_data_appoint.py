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

insert_app = "INSERT INTO Appointment VALUES (%s, %s, %s, %s, %s)"

values = [
    (1, 1, 1, '2021-10-01', '10:00:00'),
    (2, 2, 2, '2021-10-02', '11:00:00'),
    (3, 3, 3, '2021-10-03', '12:00:00')
]

# Executing the INSERT statement with the values
mycursor.executemany(insert_app, values)

# commit the changes to the database
mydb.commit()

# print the number of records inserted
print(mycursor.rowcount, "records inserted.")
