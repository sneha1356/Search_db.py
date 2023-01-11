import mysql.connector
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS MyDatabase")

#Preparing query to create a database
sql = "CREATE database MYDATABASE";

#Creating a database
cursor.execute(sql)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("use classicmodels")
sql="""select customerNumber from customers"""
sql1="""select customerName from customers"""
cursor.execute(sql)
print(cursor.fetchall())

#Closing the connection
conn.close()