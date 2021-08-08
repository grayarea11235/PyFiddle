import os
#from cmd2 import Cmd
import cmd2


class ObjShell(cmd2.Cmd):
    """The command processor"""
    #def __init__(self):
    #    pass

    def do_modules(self, args):
        modules = os.sys.modules.keys()
        for module in modules:
            self.poutput(module)


    def do_dir(self, args):
        print(args)
        dir_ents = dir(args)
        for ent in dir_ents:
            self.poutput(ent)


def main():
    app = ObjShell()
    app.cmdloop()
    #os.sys.exit(app.cmdloop())
#    os.sys.modules.keys()


if __name__ == '__main__':
    main()
