import sqlite3

# The code to create a database file and a table named Tracks with two columns in the database

# Make a connection to the database stored in the file music.sqlite (locally stored)
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
# Create the table Tracks with a title column of type TEXT and a plays column of type INTEGER
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()