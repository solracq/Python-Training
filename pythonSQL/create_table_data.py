import sqlite3

conn = sqlite3.connect('students.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS BasicInfo')
cur.execute('CREATE TABLE BasicInfo (name TEXT, lastName TEXT, age INTEGER, gender TEXT, grade INTEGER, favoriteSubject TEXT)')
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Leo', 'Palma', 38, 'M', 6, 'Ingenieria Electrica'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Heron', 'Tovar', 35, 'M', 8, 'Electromagnetismo'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Paulo', 'Dybala', 24, 'M', 9, 'Soccer'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Christiano', 'Ronaldo', 34, 'M', 10, 'Soccer'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Bezarro', 'Pend', 39, 'M', 8, 'RF Technology'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('El Nino', 'Mamel', 38, 'M', 9, 'Databases'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Milton', 'Cregueras', 30, 'M', 7, 'Religion'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Octavio', 'Perez', 44, 'M', 5, 'Primaria'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Elo', 'Perez', 37, 'F', 9, 'Biologia'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Jessica', 'Parker', 22, 'F', 9, 'Kindergarten'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Silvia', 'Campos', 26, 'F', 8, 'Music'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Lorenia', 'Her', 33, 'F', 7, 'Veterinaira'))
cur.execute('INSERT INTO BasicInfo (name, lastName, age, gender, grade, favoriteSubject) VALUES (?, ?, ?, ?, ?, ?)', ('Doug', 'Hefernnan', 43, 'M', 6, 'Truck Driving'))
conn.commit()

print()
print('Students Basic Info Table:')
print('Printing students with only certain age')
cur.execute("SELECT * FROM BasicInfo WHERE age = 38")
for record in cur:
    print(record)

print('\nPrinting all students ordered by alphabetical order')
cur.execute("SELECT * FROM BasicInfo ORDER BY name")
for row in cur:
    print(row)

print('\nPrinting all students in grade order, showing certain columns')
cur.execute("SELECT name, lastName, favoriteSubject, grade FROM BasicInfo ORDER BY grade DESC") # ASC if ascendent order
for row in cur:
    print(row)

print('\nPrinting all students based on their favorite subject')
cur.execute("SELECT name, lastName, favoriteSubject FROM BasicInfo ORDER BY favoriteSubject ASC")
for row in cur:
    print(row)

cur.execute("DELETE FROM BasicInfo WHERE lastName = \'Mamel\'")
conn.commit()

print('\nVerifying deleting of mamel student')
cur.execute('SELECT * FROM BasicInfo ORDER BY lastName')
for row in cur:
    print(row)

print('\nUpdating favorite subject of Octavio')
cur.execute("UPDATE BasicInfo SET favoriteSubject = \'Politica\' WHERE name = \'Octavio\'")
conn.commit()

cur.execute("SELECT * FROM BasicInfo ORDER BY name ASC")
for row in cur:
    print(row)

cur.close()