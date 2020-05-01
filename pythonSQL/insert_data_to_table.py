import sqlite3

conn = sqlite3.connect("music.sqlite")
cur = conn.cursor()

# INSERT two rows into the Tracks table
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thundercats', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
# force data to be written to the database
conn.commit()

print('Tracks:')
# retrieve (SELECT) the rows we just inserted from the table
cur.execute('SELECT title, plays FROM Tracks')
# looping the contents of cur as with SELECT the cur access the data on demand
for row in cur:
    print(row)

# Using * indicates that you want the database to return all of the columns for each
# row that matches the WHERE clause
cur.execute('SELECT * FROM Tracks WHERE title = \'My Way\'')
for row in cur:
    print(row)

# request that the returned rows be sorted by one of the fields
cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
for row in cur:
    print(row)

# UPDATE a a column/s within one or more rows in a table
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = \'My Way\'')
conn.commit()

# DELETE statement needs te WHERE clause
cur.execute('DELETE FROM Tracks WHERE title = \'Thundercats\'')
conn.commit()

# DELETE the rows we have just created using the WHERE clause to match the criteria
cur.execute('DELETE FROM Tracks WHERE plays < 100')
#conn.commit()

cur.close()