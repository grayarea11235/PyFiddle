"""Battery tracking script."""
# Read the battery status and store in a data store for history

import sqlite3

# /sys/class/power_supply//BATX/


def store_record():
    """Store the data record in datastore"""

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
    print(str(read_battery_info()))


if __name__ == '__main__':
    main()
