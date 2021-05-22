import os
from stat import S_ISDIR
from cmd2 import Cmd
import argparse
from cmd2 import with_argparser

import requests

argparser = argparse.ArgumentParser()

class SimpleSh(Cmd):
    prompt = "lsh> "
    intro = "Welcome to the real world!"
    
    def __init__(self):
        Cmd.__init__(self, use_ipython=True)
        

    def do_exit(self, line):
        pass

    def do_hello(self, line):
        print('Hello')

    def do_ls(self, line):
        print(line)
        if line == '':
            print('No line... default to cwd')

    @with_argparser(argparser)
    def do_status(self, line):
        if line:
            resp = requests.get(line)
            if resp.status_code == 200:
                print(self.colorize("200", "green"))
            else:
                print(self.colorize(str(resp.status_code), "red"))


class VirtualFS():
    def __init__(self):
        self.cw = '/'
        self.fs = []
        
    def ls(self):
        pass

    def mount(self, fs):
        pass

    def get_mounted(self):
        pass


class PhysicalFS():
    def __init__(self, location):
        self.location = 'file:///' + location
        self.cwd = ''

    def ls(self, path):
        rootdir = 'C:/Temp'
        res = list()

        res = os.listdir(rootdir)

        #for subdir, dirs, files in os.walk(rootdir):
        #    for adir in dirs:
        #        #print(os.path.join(subdir, adir))
        #        res.append(FileObj(os.path.join(subdir, adir)))
        #    for file in files:
        #        res.append(FileObj(os.path.join(subdir, file)))
        #        #print(os.path.join(subdir, file))

        return res


    def create(self, name):
        pass

    def delete(self, name):
        pass

    def rename(self):
        pass


class FTPFS():
    pass


class DropBoxFS():
    pass


class GoogleDriveFS():
    pass

class GitFS():
    pass


class SvnFS():
    pass


class EnvironmentFS():
    pass


class RegistryFS():
    pass


class FileObj():
    def __init__(self, full_path):
        self.full_path = full_path
        self.name = ''


    def get_attr(self):
        info = os.stat(self.full_path)
        #print(info)
        return info


    def is_directory(self):
        info = self.get_attr()
        return S_ISDIR(info.st_mode)



class FileSystemObj():
    pass


if __name__ == '__main__':
    #print('main')
    vfs = VirtualFS()
    pfs = PhysicalFS('C:/Temp')
    files = pfs.ls('/')
#    for file in files:
#        print(file)

    c = SimpleSh()
    c.cmdloop()


    #for file in files:
        #if file.is_directory() == True:
        #    print('Directory!!')
    #    print(file.full_path)
        #print(file.is_directory())
    #print(files)
