# using the mysql-connector-pthon 
import mysql.connector

# giving details to connet to mysql 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "sahaj",
    password = "1234",
    database = "week2"
)

# initalizing mydbcursor to execute mysql commands
mycursor = mydb.cursor()

# Show data base 
mycursor.execute("UPDATE Patient SET contact = '894-997-0949' WHERE patient_id = 1")

# commit the changes to the database
mydb.commit()

# print the number of records inserted
print(mycursor.rowcount, "records inserted.")


# check if the data is upadted or not
mycursor.execute("SELECT * FROM Patient")


for x in mycursor:
  print(x)


# Before 

# +------------+--------------+------+--------+--------------+
# | patient_id | patient_name | age  | gender | contact      |
# +------------+--------------+------+--------+--------------+
# |          1 | John Doe     |   35 | M      | 555-555-5555 |
# |          2 | Jane Doe     |   28 | F      | 555-555-5555 |
# |          3 | Bob Johnson  |   45 | M      | 555-555-5555 |
# +------------+--------------+------+--------+--------------+


# After

# +------------+--------------+------+--------+--------------+
# | patient_id | patient_name | age  | gender | contact      |
# +------------+--------------+------+--------+--------------+
# |          1 | John Doe     |   35 | M      | 894-997-0949 |
# |          2 | Jane Doe     |   28 | F      | 555-555-5555 |
# |          3 | Bob Johnson  |   45 | M      | 555-555-5555 |
# +------------+--------------+------+--------+--------------+
#