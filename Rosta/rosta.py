import re
import datetime

from ics import Calendar, Event

days = [ 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', ]
months = { 'JAN' : 1, 'FEB' : 2, 'MAR' : 3, 'APR' : 4, 'MAY' : 5, 'JUN' : 6, 'JUL' : 7, 'AUG' : 8, 'SEP' : 9, 'OCT' : 10, 'NOV' : 11, 'DEC' : 12, } 

def read_rosta(filename):
    with open(filename) as file:
        res = file.readlines()

    return res

def current_year():
    return 2019

def get_date(line):
    day = int(line[1])
    print(months[line[2]])
    month = int(months[line[2]])
    year = current_year()

    return datetime.datetime(year, month, day)


def preprocess_data():
    pass

def sp_line(line):
    return re.sub('\s+', ' ', line).strip().split()
    

# Rules - 
# yyy dd MMM = DATE(Assume the first oen is in current year)
# yyy = Day of week(MON, TUE, WED,)
# dd = date(zero pad)
# MMM = month (JAN, FEB, MAR etc)
#
# 1. DATE 
def process(lines):
    cal = Calendar()

    
#    for line in lines:
    while len(lines) > 0:
        line = lines.pop(0)
        
        split_line = re.sub('\s+', ' ', line).strip().split()
        if len(split_line) > 0:


            if split_line[0] in days:
                the_date = get_date(split_line)
                print(split_line)
                print('GOT A DATE!! ' + str(the_date))
                if split_line[3] == 'AVAILABLE':
                    print('GOT an AVAILABLE!!')
                    evt = Event()
                    evt.name = 'Avaliable'
                    evt.begin = the_date
                    cal.events.add(evt)

                if split_line[3] == 'OFF' and split_line[4] == 'DUTY':
                    print('GOT an OF DUTY!!')


                    evt = Event()
                    evt.name = 'Off Duty'
                    evt.begin = the_date
                    cal.events.add(evt)

                # REQUESTED BY CREW MEMBER
                if split_line[3] == 'REQUESTED': 
                    print('GOT A REQUESTED BY CREW!')
                    # read the report line
                    report_line = lines.pop(0)
                    print(report_line)
                    flightinfo_line = lines.pop(0)
                    print(flightinfo_line)

                    done = False
                    crew_info = ''
                    while not done:
                        x = sp_line(lines[0])

                        # We need to find the next line with a date
                        if x[0] in days:
                            done = True
                        else:
                            crew_info = crew_info + lines[0]
                            lines.pop(0)
                    

                    evt = Event()
                    evt.name = 'Outbound Flight'
                    evt.begin = the_date
                    evt.description = report_line + ' ' + flightinfo_line + crew_info
                    cal.events.add(evt)


                    # Now we process the return
                    print(' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ' + str(lines[0]))
                    x = sp_line(lines[0])
                    flight_date = get_date(x)

                    evt = Event()
                    evt.name = 'Return Flight'
                    evt.begin = flight_date
                    evt.description = 'DESCRIPTION NOT DONE!'
                    cal.events.add(evt)

    with open('test.ics', 'w') as my_file:
        my_file.writelines(cal)
        
        
def main():
    print('In main...')
#    print(sys.argv.count)
    rosta_list = read_rosta('./rosta_20191019.txt')
    process(rosta_list)
    
    
if __name__ == '__main__':
    main()



