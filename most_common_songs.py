from datetime import datetime


class Song:
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist
		self.counter = 1

songs = []
songsGrouped = []
mydict = {}
        

def print_timestamp():
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	print(dt_string)

def get_count_certain_weeks():
    x = int(input("How many weeks?\n"))
    print()
    count = 0
    for s in songsGrouped:
        if s.counter == x:
            count += 1
    print("\ntotal:",count)

def get_songs_certain_weeks():
    x = int(input("How many weeks?\n"))
    print()
    count = 0
    for s in songsGrouped:
        if s.counter == x:
            count += 1
            print(s.title,"\t",s.artist)
    print("\ntotal:",count)

def get_top_10():
    for x in range(10):
        mysong = songsGrouped[x]
        print()
        print(mysong.title)
        print(mysong.artist)
        print(mysong.counter)

def gl():  # greater than or less than
    print("\n1) >=")
    print("2) <=")
    ccc = input("Which?\n")
    x = int(input("How many weeks?\n"))
    count = 0
    for s in songsGrouped:
        if ccc == "1":
            if s.counter >= x:
                count += 1
        elif ccc == "2":
            if s.counter <= x:
                count += 1
    print("\ntotal:",count)

print_timestamp()

with open("charts.csv") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            s = Song(t,a)          # song
            songs.append(s)

print("total songs:",len(songs))

for s in songs:
	key = s.title + "|" + s.artist
	if key in mydict.keys():
		mydict[key] += 1
	else:
		mydict[key] = 1

for s in mydict:
	ttaa = s.split("|")
	title = ttaa[0]
	artist = ttaa[1]
	mysong = Song(title,artist)
	mysong.counter = mydict[s]
	songsGrouped.append(mysong)






# for s in songs:
#     foundSong = False
#     for x in songsGrouped:
#         if s.artist == x.artist and x.title == s.title:
#             x.counter += 1
#             foundSong = True
#             break
#     if not foundSong:
#         songsGrouped.append(s)

print_timestamp()

print("grouped songs:",len(songsGrouped))
print()


songsGrouped.sort(key=lambda x: x.counter, reverse=True)

notDone = True

while notDone:
    print("\nWhat do you want to do?")
    print("1) Get all songs that were on the charts a certain number of weeks")
    print("2) List 10 most common")
    print("3) How many distinct songs there are")
    print("4) How many songs with a certain 'week' number")
    print("5) Get count of songs that were on the charts >= or <= a certain number of weeks")
    print("6) Quit")
    choice = int(input("Enter your selection\n"))
    if choice == 1:
        get_songs_certain_weeks()
    elif choice == 2:
        get_top_10()
    elif choice == 3:
        print("total songs:",len(songsGrouped))
    elif choice == 4:
        get_count_certain_weeks()
    elif choice ==5:
        gl()
    elif choice == 6:
        notDone = False
    else:
        print("\nYou're stoopid...")



