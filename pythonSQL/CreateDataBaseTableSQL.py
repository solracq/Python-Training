import sqlite3

class CreateDB:

    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

    def createTable(self, table):
        self.cur.execute("DROP TABLE IF EXISTS " + table)
        self.cur.execute('CREATE TABLE ' + table + ' (id TEXT, fullName TEXT, gender TEXT, bday DATE)')

    def insertData(self, id, fullName, gender, bday):
        self.cur.execute('INSERT INTO UserRecords (id, fullName, gender, bday) VALUES (?, ?, ?, ?)', (id, fullName, gender, bday))
        self.conn.commit()

    def closeDB(self):
        self.conn.close()

    def displayTable(self, table, sorted, columnNum):
        if sorted == True:
            self.cur.execute('SELECT * FROM ' + table + ' ORDER BY ' + str(columnNum) + ' ASC')
        else:
            self.cur.execute('SELECT * FROM ' + table)
        for row in self.cur:
            print(row)

    def groupUserNames(self, table):
        self.cur.execute('SELECT * FROM ' + table + ' WHERE fullName IN (\'CLARA^OSWALD\')')
        for row in self.cur:
            print(row)