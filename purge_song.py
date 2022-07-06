
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.crap = False

songs = []

crapTitle = input("\nEnter the title of the song to delete\n")
crapArtist = input("Enter the artist of the song to delete\n")

with open("charts.csv") as f:
    for line in f:
        sss = line.split(",")
        # print(line)
        t = sss[0].strip()     # title
        a = sss[1].strip()     # artist
        s = Song(t,a)          # song
        songs.append(s)


# song list is all songs. need a list for 100
counter = 0
for s in songs:
    if crapTitle == s.title and crapArtist == s.artist:
        s.crap = True
        counter += 1


print("\ndeleted",counter,"songs\n")

# write to external file
k = open("charts.csv","w")
for y in songs:
    if y.crap == False:
        k.write(y.title)
        k.write(",")
        k.write(y.artist)
        k.write("\n")

k.close()