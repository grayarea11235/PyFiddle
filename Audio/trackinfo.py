import eyed3

class TrackInfo:
    def __init__(self, track_file):
        self.audio = eyed3.load(track_file)
        print(self.audio.tag.artist)
        print(self.audio.tag.album)
        print(self.audio.tag.title)
        print(self.audio.tag.genre)
        self.artist = self.audio.tag.artist
        self.album = self.audio.tag.album
        self.title = self.audio.tag.title
        self.genre = self.audio.tag.genre
        # self.audio.tag.


if __name__ == '__main__':
    ti = TrackInfo("Sherlock_06_The Sign of Four.mp3")
