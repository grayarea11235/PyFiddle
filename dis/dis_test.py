# Fiddle with dis module

import sys
import dis


def main():
    print('In main')
    dis.dis(file='test1.py')

if __name__ == '__main__':
    main()
