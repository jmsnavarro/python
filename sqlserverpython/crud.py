#!/usr/bin/python
"""This script runs CRUD commands via SQL Server via pyodbc"""

#Create Python apps using SQL Server on Windows
#https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/step/2.html

import pyodbc
SERVER = 'centos.localsandbox.com'
DATABASE = 'SampleDB'
USERNAME = 'sa'
PASSWORD = 'pAssw0rd123$'
CONNECTION = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};\
    SERVER='+SERVER+';PORT=1443;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
CURSOR = CONNECTION.cursor()

#Reset table
print('')
print('Preparing Employees table...')
TSQL = "DROP TABLE IF EXISTS dbo.Employees;"    # new in SQL Server 2016
TSQL = TSQL + " CREATE TABLE Employees (Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,\
    Name NVARCHAR(50),Location NVARCHAR(50)); "
TSQL = TSQL + " INSERT INTO Employees (Name, Location) VALUES \
    (N'Jared', N'Australia'), \
    (N'Nikita', N'India'), \
    (N'Tom', N'Germany'); "
with CURSOR.execute(TSQL):
    print('Successfully preparing Employees table')
print('')

#print('Inserting a new row into table')
#Insert Query
TSQL = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with CURSOR.execute(TSQL, 'Jake', 'United States'):
    print('Successfuly Inserted Jake!')

#Update Query
print('Updating Location for Nikita!')
TSQL = "UPDATE Employees SET Location = ? WHERE Name = ?"
with CURSOR.execute(TSQL, 'Sweden', 'Nikita'):
    print('Successfuly Updated Nikita!')

#Delete Query
print('Deleting user Jared')
TSQL = "DELETE FROM Employees WHERE Name = ?"
with CURSOR.execute(TSQL, 'Jared'):
    print('Successfuly Deleted Jared!')

#Select Query
print('')
print('Reading data from table...')
TSQL = "SELECT Name, Location FROM Employees;"
ROW_COUNT = 0
with CURSOR.execute(TSQL):
    ROW = CURSOR.fetchone()
    while ROW:
        ROW_COUNT += 1
        print(str(ROW_COUNT) + "\t" + str(ROW[0]) + "\t" + str(ROW[1]))
        ROW = CURSOR.fetchone()

print('')
