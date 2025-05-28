import mysql.connector 

con = mysql.connector.connect(host = "localhost", user="root",passwd="#Thakur#123",database="new")

if con.is_connected():
    print("succ connected")
else:
    raise print("Not")    