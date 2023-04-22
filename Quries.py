import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="sahaj",
  password="1234",
  database="week2"
)

# Create a cursor to execute queries
cursor = db.cursor()

# 1. Total Patients visited a particular hospital in a day
hospital_id = 1
date = '2023-04-23'
query = "SELECT COUNT(*) FROM Appointment WHERE hospital_id = %s AND date = %s"
cursor.execute(query, (hospital_id, date))
result = cursor.fetchone()[0]
print(f"Total Patients visited hospital {hospital_id} on {date}: {result}")

# 2. Total Patients Visited by each doctor in each hospital
query = "SELECT hospital_id, doctor_id, COUNT(*) FROM Appointment GROUP BY hospital_id, doctor_id"
cursor.execute(query)
result = cursor.fetchall()
print("Total Patients visited by each doctor in each hospital:")
for row in result:
    print(f"Hospital {row[0]}, Doctor {row[1]}: {row[2]}")

# 3. Top 5 Hospitals with the highest number of patients
query = "SELECT hospital_id, COUNT(*) FROM Appointment GROUP BY hospital_id ORDER BY COUNT(*) DESC LIMIT 5"
cursor.execute(query)
result = cursor.fetchall()
print("Top 5 Hospitals with the highest number of patients:")
for row in result:
    print(f"Hospital {row[0]}: {row[1]}")

# 4. Top 5 Doctors with the highest number of patients
query = "SELECT doctor_id, COUNT(*) FROM Appointment GROUP BY doctor_id ORDER BY COUNT(*) DESC LIMIT 5"
cursor.execute(query)
result = cursor.fetchall()
print("Top 5 Doctors with the highest number of patients:")
for row in result:
    print(f"Doctor {row[0]}: {row[1]}")

# Close the database connection
db.close()
