import sqlite3
from trackinfo import TrackInfo
from sqlite3 import OperationalError


class Datastore:

    def __init__(self, name):
        self.name = name

    def create_datastore(self):
        # Create a database in RAM
        # db = sqlite3.connect(':memory:')
        # Creates or opens a file called mydb with a SQLite3 DB
        self.db = sqlite3.connect(self.name)

        # Get a cursor objecttitle
        cursor = self.db.cursor()

        try:
            cursor.execute('''
                           CREATE TABLE tracks(id INTEGER PRIMARY KEY, name TEXT,
                           location TEXT, artist TEXT, title TEXT, genre TEXT,
                           album TEXT, length INTEGER, current TEXT)
                           ''')

            cursor.execute('''
                           CREATE TABLE properties(id INTEGER PRIMARY KEY,
                           name TEXT unique, value TEXT)
                           ''')

            self.db.commit()
        except OperationalError as oe:
            print(oe)

    def destroy_datastore(self, name):
        cursor = self.db.cursor()

        cursor.execute('''
                       DROP TABLE tracks
                       ''')

        cursor.execute('''
                       DROP TABLE properties
                       ''')

        self.db.commit()

    def get_all_tracks(self):
        pass

    def add_file(self, filename):
        ti = TrackInfo(filename)
        print(ti.genre)

        cursor = self.db.cursor()

        cursor.execute('''INSERT INTO tracks(id, name, location, artist, title, genre, album, length, current)
                       VALUES(?,?,?,?,?,?,?,?,?)''', (1, ti.title, filename, ti.artist, 
                                                      str(ti.title), 
                                                      str(ti.genre), 
                                                      ti.album, 
                                                      1, 
                                                      'Test'))

        self.db.commit()

        def scan_directory(self, directory):
            pass


if __name__ == '__main__':
    ds = Datastore('myds.db')
    ds.create_datastore()
    ds.add_file("Sherlock_06_The Sign of Four.mp3")
    # ds.destroy_datastore('myds')
