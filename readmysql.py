import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "DatabaseManagement"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM DatabaseManagement.Store")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
