import _sqlite3
from CreateDataBaseTableSQL import CreateDB

def create_users_database_table():
    sql_database = CreateDB('userRecords.sqlite')
    sql_database.createTable('UserRecords')

    sql_database.insertData('PID1', 'POND^AMY', 'F', 19890224)
    sql_database.insertData('PID2', 'WILLIAMS^RORY', 'M', 19881102)
    sql_database.insertData('PID3', 'POND^AMY', 'F', 19890224)
    sql_database.insertData('PID4', 'CLARA^OSWALD', 'F', 19890224)
    sql_database.insertData('PID5', 'POND^AMY', 'F', 20010911)
    sql_database.insertData('PID6', 'CLAR^OSWALD', 'F', 19890224)
    sql_database.insertData('PID7', 'POND^AMELIA', 'F', 20010911)
    sql_database.insertData('PID8', 'CLARA^oswald', 'F', 19890224)
    sql_database.insertData('PID9', 'TYLER^ROSE', 'F', 20000101)
    sql_database.insertData('PID10', 'NOBLE^DONNA', 'F', 19780405)
    sql_database.insertData('PID11', 'TYLER^ROSE', 'F', 20000101)
    sql_database.insertData('PID12', 'NOBLE^DONN', 'F', 19780405)
    sql_database.insertData('PID13', 'TYLER^ROS', 'F', 20000102)
    sql_database.insertData('PID14', 'CLARA^OSWALD^COLEMAN', 'F', 19890224)

    sql_database.displayTable('UserRecords', True, 2)
    print()
    sql_database.groupUserNames('UserRecords')

    sql_database.closeDB()

if __name__ == "__main__":
    create_users_database_table()