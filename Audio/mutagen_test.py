from mutagen import File
from os import path
from os import walk

from peewee import Model
from peewee import CharField
from peewee import SqliteDatabase

import sqlite3


db = SqliteDatabase('test.db')

class AudioFile(Model):
    file_name = CharField()

    class Meta:
        database = db


TEST_DIR = '/media/cpd/8067-3833/Audiobooks/'
TEST_FILE = 'Richard P. Feynman - The Pleasure of Finding Things Out Audiobook.mp3'


def scan_dir(start_path):
    db.connect()
    db.create_tables([AudioFile])

    for root, subfolders, files in walk(start_path):
        #print(root)

        for file in files:
            try:
                f = File(path.join(root, file))
            except:
                print('Got exception')
            if f is not None:
                file_name = path.join(root, file) + ' : ' + f.info.pprint()
                print(file_name)
                new_record = AudioFile(file_name = file_name)
                new_record.save()


def main():
    scan_dir(TEST_DIR)


    file = path.join(TEST_DIR, TEST_FILE)
    print(file)
    File(file).pprint()
    info_file = File(file)
    if info_file is not None and info_file.info is not None:
        print(info_file.info.pprint())


if __name__ == '__main__':
    main()
