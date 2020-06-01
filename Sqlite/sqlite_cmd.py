import subprocess

# Just fun with using the cmd line sqlite thing to do SQL

def run_cmd(db, cmd):
    prog = 'sqlite'
    ret = subprocess.call([prog, '-line', db, cmd])
    return ret


def main():
    run_cmd('test.db', '''
    CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY,
    given_name TEXT NOT NULL,
    family_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL UNIQUE);
    ''')

    run_cmd('test.db', 'DROP TABLE IF EXISTS contacts')


if __name__ == '__main__':
    main()
