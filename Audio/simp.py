#!/usr/bin/env python

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst


Gst.init(None)

player = Gst.ElementFactory.make("playbin", "player")
fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
player.set_property("video-sink", fakesink)
player.set_property("uri", "file:///home/cpd/Dev/Python/PyFiddle/Audio/mpthreetest.mp3")

format = Gst.Format(Gst.Format.TIME)
duration = player.query_duration(format)[0]
