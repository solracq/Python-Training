import pymssql

print("stared ms sql test connection:")
conn = pymssql.connect(server='localhost', user='sa', password='mssqlmik0', database='MYDB') # 172.17.0.2
print(conn)
cursor = conn.cursor()
cursor.execute('SELECT name, database_id, create_date FROM sys.databases ORDER BY name;')
row = cursor.fetchone()
while row:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()