import pymysql
from database.db_setup.database_table_schemas import db_table_schemas

def init_db():
    DB = pymysql.connect(
        host="localhost",
        user="root",
        password="Passw0rd!", 
        database="information_schema"
    )
    cursor =  DB.cursor()

    # Check if DB exists
    sql = "SHOW DATABASES like 'simprocedures'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result != None:
        return False

    # DB setup
    sql = "CREATE DATABASE IF NOT EXISTS simprocedures"
    cursor.execute(sql)

    # Swap to DB
    sql = "use simprocedures"
    cursor.execute(sql)

    # Build tables
    (table_list, table_attributes) = db_table_schemas()
    for table in table_list:
        if table in table_attributes:
            sql = "CREATE TABLE IF NOT EXISTS %s (" % table
            for columns in table_attributes[table]:
              sql += """ %s %s %s comment '%s' , """ % (columns[0], columns[1], columns[2], columns[3])
            sql += """ PRIMARY KEY(recno)) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
            cursor.execute(sql)

    return True
