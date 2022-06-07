import random
from datetime import date
from collections import Counter

def most_frequent(artists: list) -> tuple:
	counter = Counter(artists)
	# print("Most common artist:",counter.most_common(1)[0][0],counter.most_common(1)[0][1])
	return (counter.most_common(1)[0][0],counter.most_common(1)[0][1])

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.used = False

NUMSONGS = 100
songs = []
songs100 = []
title_and_artist = set()
list_of_artists = []

def canSongBeUsed(mysong: Song) -> bool: 
    oktouse = True
    tna = mysong.title + "|" + mysong.artist
    if tna in title_and_artist:
        print("Duplicate:",mysong.title,"  ",mysong.artist)
        oktouse = False
    else:
        title_and_artist.add(tna)
    return oktouse
        

with open("charts.csv") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            s = Song(t,a)          # song
            songs.append(s)
            list_of_artists.append(a)

numOfSongs = len(songs)
print("\nTotal songs:",numOfSongs)

# song list is all songs. need a list for 100
iterationCounter = 0
counter = NUMSONGS
sameSongCollisions = 0

while counter > 0:
    songnum = random.randint(0,numOfSongs-1)
    currentSong = songs[songnum]
    iterationCounter += 1
    if currentSong.used == True:
        sameSongCollisions += 1
    else:
        ok = canSongBeUsed(currentSong)
        if ok:
            currentSong.used = True
            songs100.append(currentSong)
            counter -= 1

    if iterationCounter >= 1000:
        counter = 0

print("iterations:",iterationCounter)
print("Same song collisions:  ",sameSongCollisions)



mca = most_frequent(list_of_artists)  # mca = most common artist
# print(x[0],x[1])

q = open("collisions.txt","a")

today = date.today()
dd = today.strftime("%B %d, %Y")

q.write("\n\n")
q.write(dd)
q.write("\n\n")

q.write("number of songs: ")
q.write(str(numOfSongs))
q.write("\n")

q.write("most common artist:   ")
q.write(mca[0])
q.write("\t")
q.write(str(mca[1]))
q.write("\n")

q.write("same song collisions:")
q.write("\t")
q.write(str(sameSongCollisions))
q.write("\n\n")

q.write("\n")
q.close()


j = open("newfile.csv","w")

for x in songs100:
    j.write(x.title)
    j.write(";")
    j.write(x.artist)
    j.write("\n")

j.close()

# write to external file
k = open("charts.csv","w")
for y in songs:
    if y.used == False:
        k.write(y.title)
        k.write(",")
        k.write(y.artist)
        k.write("\n")

k.close()