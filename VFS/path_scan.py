import os
import sqlite3
from sqlite3 import Error

def create_database(name):

    if not os.path.isfile(db_name):
        conn = None
    
        try:
            conn = sqlite3.connect(name)
            print(sqlite3.version)

            sql_files_table = """ CREATE TABLE IF NOT EXISTS files (
                                            id integer PRIMARY KEY,
                                            full_path text NOT NULL,
                                            create_time int,
                                            modified_time int,
                                            access_time int,
                                            file_size int
                                        ); """

            conn.execute(sql_files_table)

        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


def file_entry_exisits(conn, search_name):
    sql_str = """ SELECT id FROM files WHERE full_path = ? """
    

def add_entry(db_name, conn, entry):
    """
    Create a new file record
    :param conn:
    :param entry:
    :return: project id
    """

    insert_data = (entry.path, entry.stat().st_ctime, entry.stat().st_mtime, entry.stat().st_atime, entry.stat().st_size)

    sql = ''' INSERT INTO files(full_path, create_time, modified_time, access_time, file_size)
              VALUES(?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, insert_data)
    conn.commit()


def path_scan(db_name, path):
    print('Scanning... {path}'.format(path=path))
    
    conn = sqlite3.connect(db_name)

    dir_scan = os.scandir(path)
    for entry in dir_scan:

        add_entry(db_name, conn, entry)

        if entry.is_file():
            print(entry.name + '  ' + str(entry.stat().st_size))
    
    dir_scan.close()


if __name__ == "__main__":
    db_name = './file_data.db'
    create_database(db_name)

    path_scan(db_name, "/media/cpd/USB2")

