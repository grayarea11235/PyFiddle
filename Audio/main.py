import gi
import sys
import Player

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Controller:
    def __init__(self):
        self._player = Player()


class MyWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
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

        vbox.add(self.h_scale)
        vbox.add(test_btn)
        self.add(vbox)

        self.player = Player()

    def btn_clicked(self, w):
        print(w)

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


if __name__ == '__main__':
    # create and run the application, exit with the'?' for help.
    # running the program
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
