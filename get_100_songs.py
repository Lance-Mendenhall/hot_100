import random
from datetime import date
from collections import Counter
import all_songs_counts
import record_artists

num = 0
with open("number.txt") as f:
    num = f.read()

num = int(num)
num += 1
if num % 10 == 0:
    all_songs_counts.write_stats()
    record_artists.write_stats()

q = open("number.txt","w")
q.write(str(num))
q.close()


def most_frequent(artists: list) -> tuple:
	counter = Counter(artists)
	# print("Most common artist:",counter.most_common(1)[0][0],counter.most_common(1)[0][1])
	return (counter.most_common(1)[0][0],counter.most_common(1)[0][1])

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.used = False

class Song_heard:
    def __init__(self, title, artist, heard):
        self.title = title
        self.artist = artist
        self.heard = heard

NUMSONGS = 100
songs = []
songs100 = []
title_and_artist = set()
list_of_artists = []
what_songs_have_been_heard = {}

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

with open("list_of_distinct_songs.txt") as g:
    for line in g:
        if(line.strip(' \n') != ""):
            # print(line)
            sss = line.split("|")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            h = sss[2].strip()     # heard
            h = int(h)
            k = t + '|' + a
                     
            what_songs_have_been_heard[k] = h


random.shuffle(songs)
numOfSongs = len(songs)
print("\nTotal songs:",numOfSongs)

# song list is all songs. need a list for 100
iterationCounter = 0
counter = NUMSONGS
sameSongCollisions = 0

while counter > 0:

    currentSong = random.choice(songs)
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

# compare what_songs_have_been_heard to songs100

counter = 0
for s in songs100:
    k = s.title + '|' + s.artist
    what_songs_have_been_heard[k] = 1

# tell how many songs have a value of 0
total_songs = len(what_songs_have_been_heard)

sum_total = 0
for x in what_songs_have_been_heard:
    sum_total += what_songs_have_been_heard[x]

# print("sum total", sum_total)

# print("len songs100",len(songs100))

total_heard = sum(what_songs_have_been_heard.values())
# print("total heard", total_heard)
unheard = total_songs - total_heard

print("songs unheard:",unheard)




print("iterations:",iterationCounter)
print("Same song collisions:  ",sameSongCollisions)

mca = most_frequent(list_of_artists)  # mca = most common artist

q = open("collisions.txt","a")

today = date.today()
dd = today.strftime("%B %d, %Y")

q.write("\n\n")
q.write(dd)
q.write("\n\n")

q.write("playlist number: ")
q.write(str(num))
q.write("\n")

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
q.write("\n")

q.write("unheard songs:")
q.write("\t")
q.write(str(unheard))
q.write("\n")

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

b = open("list_of_distinct_songs.txt","w")

for k in what_songs_have_been_heard:
    # tna = k.split('|')
    # t = tna[0].strip()
    # a = tna[1].strip()

    b.write(k)
    b.write("|")
    b.write(str(what_songs_have_been_heard[k]))
    b.write('\n')


b.close()