import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sahaj",
  password="1234",
  database="my_info"
)

mycursor = mydb.cursor()

# altering the customers table to create 
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")