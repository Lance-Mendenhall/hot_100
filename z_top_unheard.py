

all_dict = {}
count_2d_songs = []   # count of unplayed songs
unplayed_songs = []
all_songs = []

with open("charts.csv") as f:
	for line in f:
		line = line.strip()
		if line != "":
            # print(line)
			sss = line.split(",")
			t = sss[0].strip()     # title
			a = sss[1].strip()     # artist
			tna = t + "|" + a
            
			if tna in all_dict.keys():
				all_dict[tna] += 1
			else:
				all_dict[tna] = 1


               

with open("list_of_unheard_songs.txt") as g:
    for line in g:
        line = line.strip()
        if line != "":
            unplayed_songs.append(line)
            
for k in all_dict.keys():
      all_songs.append([all_dict[k],k])
      if k in unplayed_songs:
            count_2d_songs.append([all_dict[k],k])
            

count_2d_songs.sort(reverse=True)
all_songs.sort(reverse=True)

print("\nMost common unplayed songs")
print()
for i in range(30):
      print(count_2d_songs[i])
      

print("\nMost common songs")
print()
for i in range(30):
      print(all_songs[i])