import sys

days = [ 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', ]


def read_rosta(filename):
    with open(filename) as file:
        res = file.readlines()

    return res


def main():
    print('In main...')
#    print(sys.argv.count)
    rosta_list = read_rosta('./rosta_20191019.txt')
    for line in rosta_list:
        print(line)

    
if __name__ == '__main__':
    main()



