import os
from cmd2 import Cmd
import argparse


class ForthShell(Cmd):
    def __init__(selfi, prompt):
        pass

    def do_exit(self):
        pass


class DictEntry:
    pass


class Forth:
    def __init__(self):
        _dict = {}
        _stack = []

    def load_dict(self):
        pass

    def init_stack(self):
        pass

    def parse_line(self, line):
        pass

    def run(self):
        quit = False
        while not quit:
            input('# ')

    def load_file(self, file_name):
        f = open('./test1.fs', mode = 'r')

        s = f.read()
        print(s)
        f.close()

        return s


def get_next():
    pass


def main():
    forth = Forth()

    input = forth.load_file('./test1.fs')

    forth.run()


if __name__ == '__main__':
    main()
