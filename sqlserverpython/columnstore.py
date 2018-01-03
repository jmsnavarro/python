#!/usr/bin/python
"""This script demonstrates column indexes feature of SQL Server
via pyodbc"""

from datetime import datetime
import pyodbc

#Connect to SQL Server
SERVER = 'centos.localsandbox.com'
DATABASE = 'SampleDB'
USERNAME = 'sa'
PASSWORD = 'pAssw0rd123$'
CONNECTION = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};\
    SERVER='+SERVER+';PORT=1443;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
CURSOR = CONNECTION.cursor()

#Prepare sample table
print('\nPreparing sample table...')
TSQL = ""
TSQL = "DROP TABLE IF EXISTS dbo.Table_with_5M_rows"
with CURSOR.execute(TSQL):
    print('')
TSQL = ""
TSQL = " WITH a AS (SELECT * FROM (VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10)) AS a(a)) \
    SELECT TOP(5000000)\
    ROW_NUMBER() OVER (ORDER BY a.a) AS OrderItemId \
    ,a.a + b.a + c.a + d.a + e.a + f.a + g.a + h.a AS OrderId \
    ,a.a * 10 AS Price \
    ,CONCAT(a.a, N' ', b.a, N' ', c.a, N' ', d.a, N' ', e.a, N' ', f.a, N' ', g.a, N' ', h.a) AS ProductName \
    INTO Table_with_5M_rows \
    FROM a, a AS b, a AS c, a AS d, a AS e, a AS f, a AS g, a AS h; "

with CURSOR.execute(TSQL):
    print('Successfully preparing sample table...\n')

#Aggregate query
TSQL = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
A = datetime.now()
with CURSOR.execute(TSQL):
    B = datetime.now()
    C = B - A
    for ROW in CURSOR:
        print('Sum\t\t1:', str(ROW[0]))
    print('QueryTime\t1:', C.microseconds, 'ms')

#Add column store index
print('\nAdding column store index...')
TSQL = ""
TSQL = " CREATE CLUSTERED COLUMNSTORE INDEX Columnstoreindex \
    ON Table_with_5M_rows; "
with CURSOR.execute(TSQL):
    print('Successfully adding column store index on Table_with_5M_rows\n')

#Aggregate query
TSQL = ""
TSQL = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
A = datetime.now()
with CURSOR.execute(TSQL):
    B = datetime.now()
    C = B - A
    for ROW in CURSOR:
        print('Sum\t\t2:', str(ROW[0]))
    print('QueryTime\t2:', C.microseconds, 'ms')

print('')
