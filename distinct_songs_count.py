import random
from datetime import date


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.used = 0


songs = []
title_and_artist = set()


with open("charts.csv") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            s = Song(t,a)          # song
            songs.append(s)

for song in songs:
	tna = song.title + '|' + song.artist
	title_and_artist.add(tna)

q = open("list_of_distinct_songs.txt","w")

for e in title_and_artist:
	q.write(e)
	q.write("|")
	q.write(str(0))
	q.write('\n')

# today = date.today()
# dd = today.strftime("%B %d, %Y")

# q.write("\n\n")
# q.write(dd)
# q.write("\n\n")

# q.write("playlist number: ")
# q.write(str(num))
# q.write("\n")

# q.write("number of songs: ")
# q.write(str(numOfSongs))
# q.write("\n")

# q.write("most common artist:   ")
# q.write(mca[0])
# q.write("\t")
# q.write(str(mca[1]))
# q.write("\n")

# q.write("same song collisions:")
# q.write("\t")
# q.write(str(sameSongCollisions))
# q.write("\n\n")

# q.write("\n")
# q.close()

# j = open("newfile.csv","w")

# for x in songs100:
#     j.write(x.title)
#     j.write(";")
#     j.write(x.artist)
#     j.write("\n")

# j.close()

# # write to external file
# k = open("charts.csv","w")
# for y in songs:
#     if y.used == False:
#         k.write(y.title)
#         k.write(",")
#         k.write(y.artist)
#         k.write("\n")

# k.close()