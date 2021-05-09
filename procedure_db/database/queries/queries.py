import pymysql
import inspect



def select_all():
    DB = pymysql.connect(
            host="localhost",
            user="root",
            password="Passw0rd!",
            database="information_schema"
    )
    cursor =  DB.cursor()
    cursor.execute("USE simprocedures")

    sql = """ SELECT name, arch, file_type, os_version,
                models_os, models_libs
                FROM `simprocedures` """
    try:
        cursor.execute(sql)
    except pymysql.Error as e:
        print('{}: Got error {!r}, errno is {}. Rollback'.format(
            inspect.currentframe().f_lineno, e, e.args[0]))
        DB.rollback()

    result = cursor.fetchall()
    if result == None:
        return []

    datatables = []
    for row in result:
        tmp = {}
        tmp['name'] = row[0]
        tmp['arch'] = row[1]
        tmp['file_type'] = row[2]
        tmp['os_version'] = row[3]
        tmp['models_os'] = row[4]
        tmp['models_libs'] = row[5]
        datatables.append(tmp)


    return datatables 

def select_where(jdata):
    pass
