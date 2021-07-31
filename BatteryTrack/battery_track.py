"""Battery tracking script."""
# Read the battery status and store in a data store for history

import sqlite3
import datetime
import os

# /sys/class/power_supply//BATX/


def database_exists(name):
    """Check if the database exists."""


def create_database(name):
    """Create the database."""
    conn = sqlite3.connect(name)

    cur = conn.cursor()

    # Create table
    cur.execute('''CREATE TABLE batt_rec 
                (timestamp text, inteeger charge, text status)''')

    # Insert a row of data
    # cur.execute("INSERT INTO batt_rec VALUES ('2006-01-05', 100,'Full')")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def store_record(dbname, batt_data):
    """Store the data record in datastore."""
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()
   
    timestamp = datetime.datetime.now().isoformat()
    print(timestamp)
    cur.execute(
            '''INSERT INTO batt_rec 
            VALUES ('{timestamp}', '{capacity}', '{status}')'''.format(
                timestamp=timestamp,
                capacity=batt_data['capacity'],
                status=batt_data['status']))
    conn.commit()
    conn.close()


def read_battery_info():
    """
    Read the battery status from the linux only system.

    Returns:
        a dictionary of the information.
    """
    with open('/sys/class/power_supply//BATX/capacity', 'r') as in_file:
        capacity = in_file.readline().rstrip()

    with open('/sys/class/power_supply//BATX/status', 'r') as in_file:
        status = in_file.readline().rstrip()

    return {
        'capacity': capacity,
        'status': status
    }


def main():
    """Start the script."""
    dbname = 'test.db'

    print(str(read_battery_info()))
    if not os.path.exists(dbname):
        create_database(dbname)

    batt_info = read_battery_info()
    store_record(dbname, batt_info)


if __name__ == '__main__':
    main()
