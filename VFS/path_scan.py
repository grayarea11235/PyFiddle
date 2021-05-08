import os
import sqlite3
from sqlite3 import Error

def create_datastore(name):
    
    conn = None
    
    try:
        conn = sqlite3.connect(name)
        print(sqlite3.version)


        sql_files_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def add_entry(entry):
    pass


def path_scan(path):
    print('Scanning... {path}'.format(path=path))

    dir_scan = os.scandir(path)
    for entry in dir_scan:
        if entry.is_file():
            print(entry.name + '  ' + str(entry.stat().st_size))
    
    dir_scan.close()


if __name__ == "__main__":
    path_scan("/media/cpd/USB2")

