import eyed3


class TrackInfo:
    def __init__(self, track_file):
        self.audio = eyed3.load(track_file)
        print(self.audio.tag.artist)
        print(self.audio.tag.album)
        print(self.audio.tag.title)
        print(self.audio.tag.genre)
        print(self.audio.tag.track_num)

        self.artist = self.audio.tag.artist
        self.album = self.audio.tag.album
        self.title = self.audio.tag.title
        self.genre = self.audio.tag.genre
        self.album_artist = self.audio.tag.album_artist
        self.track_num, self.track_max = self.audio.tag.track_num
        print(str(self.track_num) + ' of ' + str(self.track_max))
        # self.audio.tag.


if __name__ == '__main__':
    # ti = TrackInfo("Sherlock_06_The Sign of Four.mp3")
    # ti = TrackInfo("/home/cpd/Dev/Python/PyFiddle/Audio/Kim Stanley Robinson M1 Red Mars/07-34 - Red Mars - Kim Stanley Robinson.mp3")
    ti = TrackInfo("/home/cpd/Dev/Python/PyFiddle/Audio/From Bacteria to Bach and Back The Evolution of Minds (Unabridged)/From Bacteria to Bach and Back - 007.mp3")
