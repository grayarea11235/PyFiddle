#!/usr/bin/env python

import os
import gi

gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gst, GObject, Gtk


class GTK_Main(object):
    def __init__(self):
        window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        window.set_title("Test Harness 1")
        window.set_default_size(400, -1)
        window.connect("destroy", Gtk.main_quit, "WM destroy")

        vbox = Gtk.VBox()
        hbox = Gtk.HBox()

        window.add(vbox)
        self.entry = Gtk.Entry()
        #self.entry.set_text('./mpthreetest.mp3')
        self.entry.set_text('./Sherlock_06_The Sign of Four.mp3')

        vbox.pack_start(self.entry, False, True, 0)

        self.button = Gtk.Button("Start")
        self.button.connect("clicked", self.play_pause)

        self.stop_button = Gtk.Button("Stop")
        self.stop_button.connect("clicked", self.stop)

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

        # we connect the signal "value-changed" emitted by the scale with the callback
        # function scale_moved
        self.h_scale.connect("value-changed", self.scale_moved)

        vbox.add(self.button)
        vbox.add(self.stop_button)
        vbox.add(self.h_scale)

        window.show_all()

        self.player = Gst.ElementFactory.make("playbin", "player")
        fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

        filepath = self.entry.get_text().strip()
        filepath = os.path.realpath(filepath)
        self.player.set_property("uri", "file://" + filepath)
        print(self.player.get_property("uri"))
        print(self.player.get_property("volume"))

    def print_state(self):
        success, state, pending = self.player.get_state(50)
        print("state = {}".format(state))

    def stop(self, w):
        print('Stop pressed')
        self.print_state()
        self.player.set_state(Gst.State.NULL)
        self.print_state()

    def play_pause(self, w):

        print(self.button.get_label())
        #success, state, pending = self.player.get_state(50)
        #print("success = {} state = {} pending = {}".format(success, state, pending))
        #        print(self.player.get_state())

        if self.button.get_label() == "Start":
            self.print_state()
            self.button.set_label("Pause")
            self.player.set_state(Gst.State.PLAYING)
            self.print_state()
        else:
            self.print_state()
            self.player.set_state(Gst.State.PAUSED)
            self.button.set_label("Start")
            self.print_state()

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.player.set_state(Gst.State.NULL)
            self.button.set_label("Start")
        elif t == Gst.MessageType.ERROR:
            self.player.set_state(Gst.State.NULL)
            err, debug = message.parse_error()
            print("Error: %s" % err, debug)
            self.button.set_label("Start")

    def scale_moved(self, event):
        print("Horizontal scale is " +
              str(int(self.h_scale.get_value())) + ".")


if __name__ == '__main__':
    Gst.init(None)
    GTK_Main()
    GObject.threads_init()
    Gtk.main()
