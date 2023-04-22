import mysql.connector
import csv

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="sahaj",
  password="1234",
  database="week2"
)

# Define the hospital ID and date
hospital_id = 1
date = '2023-04-23'

# Query to get daily unique patient count
unique_patient_query = f"SELECT COUNT(DISTINCT patient_id) AS unique_patients FROM Appointment WHERE hospital_id={hospital_id} AND date='{date}'"

# Query to get repeating patient count
repeating_patient_query = f"SELECT COUNT(*) - COUNT(DISTINCT patient_id) AS repeating_patients FROM Appointment WHERE hospital_id={hospital_id} AND date='{date}'"

# Execute the queries
cursor = mydb.cursor()
cursor.execute(unique_patient_query)
unique_patients = cursor.fetchone()[0]
cursor.execute(repeating_patient_query)
repeating_patients = cursor.fetchone()[0]

# Define the file name and path
file_name = f"{date}_hospital{hospital_id}_visit_summary.csv"
file_path = f"{file_name}"   

# Write data to CSV file
with open(file_path, mode='w', newline='') as csv_file:
    fieldnames = ['Date', 'Hospital ID', 'Unique Patients', 'Repeating Patients']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Date': date, 'Hospital ID': hospital_id, 'Unique Patients': unique_patients, 'Repeating Patients': repeating_patients})

# Close database connection
mydb.close()
