class Vinyl:
    def __init__(self, album, artist, year):
        self.album = album
        self.artist = artist
        self.year = year

    def display(self):
        print(self.album + ' - ' + self.artist +' - ' + self.year)

def run01():
    taylor = Vinyl('1989', 'Taylor Swift', '2014')
    taylor.display()

run01()