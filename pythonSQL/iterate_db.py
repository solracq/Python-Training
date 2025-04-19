import pymssql

conn = pymssql.connect(server='172.17.0.2', user='sa', password='mssqlmik0', database='tempdb')
cursor = conn.cursor()
# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')

cursor.execute('SELECT * FROM persons')

for row in cursor:
    print(f'row = {row}')

cursor.execute('SELECT * FROM persons ORDER BY name')
print("\nDatabase tempdb")
for row in cursor:
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))

conn.close()