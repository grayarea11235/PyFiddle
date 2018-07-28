import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst


class Player:
    def __init__(self):
        self._player = Gst.ElementFactory.make("playbin", "player")
        fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
        self._player.set_property("video-sink", fakesink)

        bus = self._player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

    def on_message(self):
        print("on_message")

    def set_file(self, file):
        self._player.set_property("uri", "file://" + file)

    def play(self):
        self._player.set_state(Gst.State.PLAYING)

    def pause(self):
        self._player.set_state(Gst.State.PAUSED)

    def stop(self):
        self._player.set_state(Gst.State.NULL)


if __name__ == '__main__':
    p = Player()
    p.set_file('/home/cpd/Dev/Python/PyFiddle/Audio/Sherlock_06_The Sign of Four.mp3')
