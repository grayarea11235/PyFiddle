import csv
import sqlite3
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

NAME_FILE = 'data/names_basics_data.tsv'
TITLE_FILE = 'data/title.basics.tsv'    
AKAS_FILE = 'data/title.akas.tsv'

# This is destructive
def create_db(db):
    cursor = db.cursor()st i

    cursor.execute('''
    DROP TABLE IF EXISTS names
    ''')
    cursor.execute('''
    DROP TABLE IF EXISTS name_profession
    ''')
    cursor.execute('''
    DROP TABLE IF EXISTS name_title
    ''')
    cursor.execute('''
    DROP TABLE IF EXISTS titles
    ''')
    cursor.execute('''
    DROP TABLE IF EXISTS titles_aka
    ''')
    db.commit()
    
    cursor.execute('''
    CREATE TABLE names(id TEXT PRIMARY KEY, name TEXT,
    birth_year TEXT, death_year TEXT)
    ''')
    cursor.execute('''
    CREATE TABLE name_profession(name_id TEXT, prof_name TEXT,
    PRIMARY KEY (name_id, prof_name))
    ''')
    cursor.execute('''
    CREATE TABLE name_title(name_id TEXT, title_id TEXT,
    PRIMARY KEY (name_id, title_id))
    ''')
    cursor.execute('''
    CREATE TABLE titles(title_id TEXT, type TEXT, title TEXT, 
    adult TEXT, start_year TEXT, end_year TEXT, runtime TEXT,
    PRIMARY KEY (title_id))
    ''')
    cursor.execute('''
    CREATE TABLE titles_aka(title_id TEXT, type TEXT, title TEXT, 
    adult TEXT, start_year TEXT, end_year TEXT, runtime TEXT,
    PRIMARY KEY (title_id))
    ''')
    db.commit()


def load_names(db):
    with open(NAME_FILE, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t', quotechar='|')

        cursor = db.cursor()
        count = 0
        print('Starting to load NAMES...')
        
        for row in datareader:
            nconst = row[0]
            primary_name = row[1]
            birth_year = row[2]
            death_year = row[3]
            f_prof = StringIO(row[4])
            profreader = csv.reader(f_prof, delimiter=',')

            f_title = StringIO(row[5])
            titlereader = csv.reader(f_title, delimiter=',')

            cursor.execute('''INSERT INTO names(id, name, birth_year, death_year)
            VALUES(?,?,?,?)''', (nconst, primary_name, birth_year, death_year))

            for prof_list in profreader:
                for prof in prof_list:
                    prof_name = prof
            
                    cursor.execute('''INSERT INTO name_profession(name_id, prof_name)
                    VALUES(?, ?)''', (nconst, prof_name))

            for title_list in titlereader:
                for title in title_list:
                    title_id = title
            
                    cursor.execute('''INSERT INTO name_title(name_id, title_id)
                    VALUES(?, ?)''', (nconst, title_id))

            count = count + 1
            if count % 1000 == 0:
                print('Name: ' + str(count))

        db.commit()


# titleId,ordering,title,region,language,types,attributes,isOriginalTitle
def load_akas(db):
    with open(AKAS_FILE, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t', quotechar='|')

        cursor = db.cursor()
        count = 0
        print('Starting to load AKAS...')

        for row in datareader:
            print(row)

        
# tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres
def load_titles(db):
    with open(TITLE_FILE, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter='\t', quotechar='|')

        cursor = db.cursor()
        count = 0
        print('Starting to load TITLES...')
        
        for row in datareader:
            title_id = row[0]
            the_type = row[1]
            title = row[2]
            adult = row[3]
            start_year = row[4]
            end_year = row[5]
            runtime = row[6]

            cursor.execute('''INSERT INTO titles(title_id, type, title, adult, 
            start_year, end_year, runtime) VALUES(?,?,?,?,?,?,?)''',
                           (title_id, the_type, title, adult,
                            start_year, end_year, runtime))

            count = count + 1
            if count % 1000 == 0:
                print('Title: ' + str(count))

        db.commit()

    
def load_data():
    db = sqlite3.connect('imdb.db')
    db.text_factory = str
    cursor = db.cursor()

    create_db(db)
#    load_names(db)
#    load_titles(db)
    load_akas(db)

if __name__ == '__main__':
    load_data()
# professions, knownfortitles
# actor,writer,director	tt0015863,tt0017925,tt0015324,tt0016332
