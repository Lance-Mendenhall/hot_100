import random
from datetime import date
import all_songs_counts
import record_artists
import monte_carlo

prob_of_no_dups = monte_carlo.loopy()

num = 0
with open("number.txt") as f:
    num = f.read()

num = int(num)
num += 1
if num % 10 == 0:
    all_songs_counts.write_stats()
    record_artists.write_stats()

q = open("number.txt","w")
num = str(num)
q.write(num)
q.close()

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.used = False

NUMSONGS = 100
songs = []
songs100 = []
title_and_artist = set()
NUM_DISTINCT_SONGS = 20610
previous_two = []

unheard_songs = set()
all_distinct_songs = set()
all_distinct_artists = set()
removal_set = set()
dup_count = 0
dict_of_songs = {}
pcounter = 0

with open("last_two.txt") as lt:
    for line in lt:
        line = line.strip()
        if line != "":
            previous_two.append(line)

def canSongBeUsed(mysong: Song) -> bool: 
    oktouse = True
    global dup_count
    tna = mysong.title + "|" + mysong.artist
    if tna in title_and_artist:
        oktouse = False
        dup_count += 1
    elif tna in previous_two:
        global pcounter
        pcounter += 1
        oktouse = False
    else:
        title_and_artist.add(tna)
    return oktouse

with open("charts.csv") as f:
    for line in f:
        line = line.strip()
        if line != "":
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            s = Song(t,a)          # song
            songs.append(s)
            all_distinct_songs.add(t + '|' + a)
            all_distinct_artists.add(a)
            tna = t + "|" + a

            # adding song to dictionry with values as count
            if tna in dict_of_songs.keys():
                dict_of_songs[tna] += 1
            else:
                dict_of_songs[tna] = 1


distinct_song_count = len(all_distinct_songs)
distinct_artist_count = len(all_distinct_artists)

with open("list_of_unheard_songs.txt") as g:
    for line in g:
        line = line.strip()
        if line != "":
            unheard_songs.add(line)



random.shuffle(songs)
numOfSongs = len(songs)

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

maxi = -1
title = ""
artist = ""

for k in dict_of_songs.keys():
	if dict_of_songs[k] > maxi and k in unheard_songs:
		maxi = dict_of_songs[k]

		sss = k.split("|")
		title = sss[0].strip()     # title
		artist = sss[1].strip()    # artist

temp_list = list(title_and_artist)
previous_two += temp_list
previous_two = previous_two[100:]

lt = open("last_two.txt","w")
for x in previous_two:
    lt.write(x + "\n")
lt.close()
                
q = open("collisions.txt","a")

today = date.today()
dd = today.strftime("%B %d, %Y")

q.write("\n\n")
q.write(dd)
q.write("\n\n")

song_exit_count = 0

for song in songs100:
    tna = song.title + '|' + song.artist
    removal_set.add(tna)

    if dict_of_songs[tna] == 1:
        song_exit_count += 1

if song_exit_count > 0:
    q.write("disappearing song count: " + str(song_exit_count) + "\n")


uh1 = len(unheard_songs)
unheard_songs -= removal_set

unheard = len(unheard_songs)
new_songs_this_playlist = uh1 - unheard

# NUM_DISTINCT_SONGS = 20610

perc_heard_songs =  100 * (NUM_DISTINCT_SONGS - unheard) / NUM_DISTINCT_SONGS

print("\niterations:",iterationCounter)

q.write("playlist number: " + str(num) + "\n")
q.write("number of songs: " + str(numOfSongs) + "\n")
q.write("number of distinct songs: " + str(distinct_song_count) + "\n")
q.write("number of distinct artists: " + str(distinct_artist_count) + "\n")
q.write("same song collisions:" + "\t" + str(sameSongCollisions) + "\n")
q.write("number of duplicates:" + "\t" + str(dup_count) + "\n")
q.write("conflicts with last 2 playlists:" + "\t" + str(pcounter) + "\n")
q.write("probability of distinct playlist:" + "\t" + str(prob_of_no_dups) + "\n")
q.write("unheard songs:" + "\t" + str(unheard) + "\n")
q.write("percentage of songs heard:" + "\t" + str(perc_heard_songs) + "\n")
q.write("new songs this playlist:" + "\t" + str(new_songs_this_playlist) + "\n")
q.write("Most unheard song: " + title + " by " + artist + ".\n")
q.write("It is in the source file " + str(maxi) + " times.\n")
q.write("\n")
q.close()

# j = open("newfile.csv","w")

# for x in songs100:
#     j.write(x.title + ";" + x.artist + "\n")

# j.close()

path = "../archive/hot_100/hot100_0" + num + ".csv"

j = open(path,"w")

for x in songs100:
    j.write(x.title + ";" + x.artist + "\n")

j.close()

# write to external file
k = open("charts.csv","w")
for y in songs:
    if y.used == False:
        k.write(y.title + "," + y.artist + "\n")

k.close()

b = open("list_of_unheard_songs.txt","w")

for k in unheard_songs:
    b.write(k + "\n")

b.close()