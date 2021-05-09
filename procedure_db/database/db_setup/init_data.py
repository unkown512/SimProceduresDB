import os
import pymysql
import json
import inspect

def default_data():
    '''
        For demo purposes

    '''
    DB = pymysql.connect(
        host="localhost",
        user="root",
        password="Passw0rd!",
        database="information_schema"
    )
    cursor =  DB.cursor()
    cursor.execute("USE simprocedures")
    data_dir = '/home/djbey/angr_extended/SimProceduresDB/procedure_db/database/simprocedures/'

    procedures = os.listdir(data_dir)
    if len(procedures) == 0:
        print("No simprocedures found locally")
        return False

    for procedure in procedures:
        files = os.listdir(os.path.join(data_dir, procedure))
        for f in files:
            if ".conf.json" in f and ".swp" not in f:
                # get file info
                f_path = os.path.join(data_dir, procedure, f)
                print(f_path)
                f_obj = open(f_path, 'r')
                f_data = json.load(f_obj)
                if len(f_data) > 0:
                    sql = """ INSERT INTO `simprocedures`(name, arch, file_type
                                , os_version, contains_bytes, models_os, 
                                models_libs)

                                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    """
                    values = (f_data['name'], f_data['arch'], f_data['file_type'],
                            f_data['os_version'], f_data['contains_bytes'],
                            f_data['models_os'], f_data['models_libs'])
                    print("SQL", sql, values)
                    try:
                        cursor.execute(sql % values)
                    except pymysql.Error as e:
                        print('{}: Got error {!r}, errno is {}. Rollback'.format(
                            inspect.currentframe().f_lineno, e, e.args[0]))
                        DB.rollback()
                
        continue

default_data()
