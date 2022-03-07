from mutagen import File
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

from os import path
from os import walk

from peewee import Model
from peewee import CharField
from peewee import FloatField
from peewee import SqliteDatabase

import sqlite3


db = SqliteDatabase('test.db')

# Object for a title
class Title(Model):
    pass


class AudioFile(Model):
    file_name = CharField()
    length = FloatField()
    type = CharField()
    
    class Meta:
        database = db

        
LOCAL_TEST_DIR = '/home/cpd/Downloads/pilgrim_201909/'
TEST_DIR = '/media/cpd/8067-3833/Audiobooks/'
TEST_FILE = 'Richard P. Feynman - The Pleasure of Finding Things Out Audiobook.mp3'


def print_MPEGInfo(info):
    return info.pprint()
#    print('Length      = {length}'.format(length=info.length))
#    print('Channels    = {channels}'.format(channels=info.channels))
#    print('Bit Rate    = {bitrate}'.format(bitrate=info.bitrate))
#    print('Sampel Rate = {sample_rate}'.format(sample_rate=info.sample_rate))
#encoder_info          
#encoder_settings
#bitrate_mode
#track_gain
#track_peak
#album_gain
#version
#layer
#mode
#protected
#sketchy


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
                print(file)
                new_record = AudioFile(file_name = file_name)

                if isinstance(f, MP3):
                    print('FOUND AN MP3 : {info}'.format(info=print_MPEGInfo(f.info)))
                    new_record.length = f.info.length
                    new_record.type = 'MP3'
                elif isinstance(f, MP4):
                    print('FOUND AN MP4 {file_name}: {info}'.format(file_name=file_name, info=f.info.pprint()))
                    #print(f.info.MP4Chatpers)
                    new_record.length = f.info.length
                    new_record.type = 'MP4'
                else:
                    print(type(f))

                
                new_record.save()


def main():
#    scan_dir(TEST_DIR)
    scan_dir(LOCAL_TEST_DIR)


    file = path.join(TEST_DIR, TEST_FILE)
    print(file)
    File(file).pprint()
    info_file = File(file)
    if info_file is not None and info_file.info is not None:
        print(info_file.info.pprint())


if __name__ == '__main__':
    main()
