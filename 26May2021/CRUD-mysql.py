import mysql.connector

# Create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="######",
  password="######"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.close()
mydb.close()

# Creating table
mydb = mysql.connector.connect(
  host="localhost",
  user="######",
  password="######",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mytable (name VARCHAR(20), city VARCHAR(20))")

# Inserting
sql = "INSERT INTO mytable VALUES (%s, %s)"
val = ("XYZ", "AHM")
mycursor.execute(sql, val)
mydb.commit()

# Update
mycursor.execute("UPDATE mytable SET city='SURAT' WHERE name='XYZ'")
mydb.commit()

# Read
mycursor.execute("SELECT * FROM mytable")
myresult = mycursor.fetchall()
for row in myresult:
  print(row)

# Delete
mycursor.execute("DELETE FROM mytable WHERE name='XYZ'")
mydb.commit()

# Close connection
mycursor.close()
mydb.close()
