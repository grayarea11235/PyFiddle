#/usr/bin/env python

#from gi.repository import Gst, GObject, Gtk

import os
import gi

gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Wnck


def test():
    res = Gtk.main_iteration()
    screen = Wnck.Screen.get_default()
    screen.force_update()
    wnds = screen.get_windows()
    print(wnds)
    return wnds


if __name__ == '__main__':
    test()
