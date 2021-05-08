import os
import sqlite3
from sqlite3 import Error

def create_datastore(name):
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

