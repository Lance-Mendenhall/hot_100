
all_songs = []
unplayed_songs = []

with open("charts.csv") as f:
    for line in f:
        line = line.strip()
        if line != "":
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            tna = t + "|" + a
            all_songs.append(tna)

               

with open("list_of_unheard_songs.txt") as g:
    for line in g:
        line = line.strip()
        if line != "":
            unplayed_songs.append(line)
            

total_songs = len(all_songs)
total_unplayed = len(unplayed_songs)
            
print("all songs length:",total_songs)
print("unplayed songs length:",total_unplayed)

counter_unplayed = 0

for x in all_songs:
    if x in unplayed_songs:
        counter_unplayed += 1
        
percentage_unplayed = counter_unplayed / total_songs * 100
print("Percentage unplayed:", percentage_unplayed)