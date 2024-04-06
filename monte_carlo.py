import random

list_count = 0
songs = []


with open("charts.csv") as f:
    for line in f:
        line = line.strip()
        if line != "":
            songs.append(line)

def prob():

    NUMSONGS = 100

    title_and_artist = set()
    dup_flag = 0

    counter = NUMSONGS

    while counter > 0:
        #print(counter)
        mysong = random.choice(songs)
        if mysong in title_and_artist:
            # print(mysong)
            dup_flag = 1
        else:
            title_and_artist.add(mysong)
        counter -= 1
    

    return dup_flag


def loopy():
    numerator = 0
    retval = 0
    for _ in range(0,10000):
        y = prob()
        numerator += y
    numerator = 1 - numerator/10000
    retval = round(numerator,4)
    return retval






