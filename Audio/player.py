import sys, threading, time, logging
import gi

gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gst, Gtk


#
# Currently this is jsut a simpel audio player for gstreamer
#
class Player(object):

    def __init__(self):
        # player = Gst.ElementFactory.make("playbin", "player")
        Gst.init(None)
        
        self._player = Gst.ElementFactory.make("playbin", "player")
        fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
        self._player.set_property("video-sink", fakesink)
        print(self._player)

        bus = self._player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

        
    def _dump_obj(self, o):
        #dir_o = dir(o)
        print(type(o))
        for i in dir(o):
            #if callable(i) == True:
            print('\t' + i)
            a = getattr(o, i)
            #print('***** ' + str(type(a("test"))))
            #print(type(a))
            print('\t\t' + str(callable(a)) + ' ' + str(a))
        #print(dir_o)


    def on_message(self, bus, message):
#        print("on_message")
        msg_type = message.type
        print(msg_type)

        if msg_type == Gst.MessageType.EOS:
            #print(Gst.Message.timestamp)
            #print(Gst.Message.src)

            print('EOS!!!')

        if msg_type == Gst.MessageType.INFO:
            print('INFO got')
            #print(Gst.Message.timestamp)
            #print(Gst.Message.src)

        if msg_type == Gst.MessageType.TAG:
            self._dump_obj(Gst.Message.timestamp)
            self._dump_obj(Gst.Message.src)

            
    def set_file(self, file):
        self._player.set_property("uri", "file://" + file)

        
    def play(self):
        #self.play_thread_id = thread.start_new_thread(self.play_thread, ())
        x = threading.Thread(target=self.play_thread, args=(1,))
        print(x)
        x.start()

        ret = self._player.set_state(Gst.State.PLAYING)
        if ret == Gst.StateChangeReturn.FAILURE:
            print("ERROR: Unable to set the pipeline to the playing state")
            sys.exit(1)


    def play_thread(self):
        print('Inside thread')
        play_thread_id = self.play_thread_id
        Gdk.threads_enter()
        print('In play_thread')
        time.sleep(10)
        print('Done thread')
#        self.time_label.set_text("00:00 / 00:00")
        Gdk.threads_leave()


    def pause(self):
        self._player.set_state(Gst.State.PAUSED)


    def stop(self):
        self._player.set_state(Gst.State.NULL)

# Create thread here
def init_thread():
    pass


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info('ENTER Test')

    
    p = Player()
#    p.set_file('/home/cpd/Dev/Python/PyFiddle/Audio/Sherlock_06_The Sign of Four.mp3')
    p.set_file('/home/cpd/Devel/PyFiddle/Audio/mpthreetest.mp3')
    p.play()
    Gtk.main()

