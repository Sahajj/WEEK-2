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

# Creating tables 
# Creating the Hospital table
mycursor.execute("CREATE TABLE Hospital (hospital_id INT PRIMARY KEY,hospital_name VARCHAR(255),address VARCHAR(255),city VARCHAR(255),state VARCHAR(255),pincode VARCHAR(255));")

# Creating the Doctor table
mycursor.execute("CREATE TABLE Doctor (doctor_id INT PRIMARY KEY,doctor_name VARCHAR(255),specialization VARCHAR(255),hospital_id INT,FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id));")

# Creating the Patient table
mycursor.execute("CREATE TABLE Patient ( patient_id INT PRIMARY KEY, patient_name VARCHAR(255), age INT, gender VARCHAR(255), contact VARCHAR(255));")

# Creating the Appointment table
mycursor.execute("CREATE TABLE Appointment (appointment_id INT PRIMARY KEY,doctor_id INT,patient_id INT,date DATE,time TIME, FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),FOREIGN KEY (patient_id) REFERENCES Patient(patient_id))")

#checking if the tables exist or not
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


  