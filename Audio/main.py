import gi
import sys
from player import Player
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Controller:
    def __init__(self):
        self._player = Player()


class MyWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Audio player 1", application=app)
        vbox = Gtk.VBox()


        test_btn = Gtk.Button()
        test_btn.set_label("Test")
        test_btn.connect("clicked", self.btn_clicked)
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)


        
        
        # an horizontal scale
        self.h_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        # of integers (no digits)
        self.h_scale.set_digits(0)
        # that can expand horizontally if there is space in the grid (see
        # below)
        self.h_scale.set_hexpand(True)
        # that is aligned at the top of the space allowed in the grid (see
        # below)
        self.h_scale.set_valign(Gtk.Align.START)

        # we connect the signal "value-changed" emitted by the scale
        # with the callback function scale_moved
        self.h_scale.connect("value-changed", self.scale_moved)

        # Main listbox
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
#        self.listbox

        
#        vbox.add(self.h_scale)
        vbox.add(test_btn)
        vbox.add(self.listbox)
        self.add(vbox)

        
    def btn_clicked(self, w):
        print(w)
        self.player = Player()
        self.player.set_file('/home/cpd/Dev/Python/PyFiddle/Audio/mpthreetest.mp3')
        self.player.play()


    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
        
    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

#        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

        
        
    def scale_moved(self, event):
        print("Horizontal scale is " +
              str(int(self.h_scale.get_value())) + ".")
        print(self.get_size())


class MyApplication(Gtk.Application):
    # constructor of the Gtk Application
    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application the window belongs to.
    # Note that the function in C activate() becomes do_activate() in Python
    def do_activate(self):
        win = MyWindow(self)
        # show the window and all its content
        # this line could go in the constructor of MyWindow as well
        win.show_all()

    # start up the application
    # Note that the function in C startup() becomes do_startup() in Python
    def do_startup(self):
        Gtk.Application.do_startup(self)


def main():
    # create and run the application, exit with the'?' for help.
    # running the program
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
    

if __name__ == '__main__':
    main()
