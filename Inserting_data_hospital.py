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


# Defining the INSERT statement
insert_query = "INSERT INTO Hospital (hospital_id, hospital_name, address, city, state, pincode) VALUES (%s, %s, %s, %s, %s, %s)"

values = [
    (1, 'XYZ Hospital', '123 Main St', 'New York', 'NY', '10001'),
    (2, 'ABC Hospital', '456 Center St', 'Los Angeles', 'CA', '90001'),
    (3, 'DEF Hospital', '789 North St', 'Columbus', 'OH', '43004')  
]

# Executing the INSERT statement with the values
mycursor.executemany(insert_query, values)
# commit the changes to the database
mydb.commit()

# print the number of records inserted
print(mycursor.rowcount, "records inserted.")





