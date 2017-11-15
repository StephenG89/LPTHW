class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

Lyrics = ["Happy birthday to you",
            "I don't want to get sued",
            "So I'll stop right there"]

happy_bday = Song(Lyrics)

Lyrics = ["They rally around that family",
            "With pockets full of shells"]

bulls_on_parade = Song(Lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
