import sqlite3


class Datastore:

    def __init__(self, name):
        self.name = name

    def create_datastore(self):
        # Create a database in RAM
        # db = sqlite3.connect(':memory:')
        # Creates or opens a file called mydb with a SQLite3 DB
        self.db = sqlite3.connect(self.name)

        # Get a cursor object
        cursor = self.db.cursor()

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

    def destroy_datastore(name):
        pass
    
    def get_all_tracks():
        pass


if __name__ == '__main__':
    ds = Datastore('myds')
    ds.create_datastore()
