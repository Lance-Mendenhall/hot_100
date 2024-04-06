
# first, put in a set with pipe
# second, dict with artist count as value
# put in 2d list to see how many songs by each artist
# give a count of how many artists have 1 song, how many with 2, etc. 

tna_set = set()
mydict = {}
twoD_list = []


with open("charts.csv") as f:
    for line in f:
        line = line.strip()
        if line != "":
            # print(line)
            sss = line.split(",")
            t = sss[0].strip()     # title
            a = sss[1].strip()     # artist
            tna = t + "|" + a
            tna_set.add(tna)
            
for x in tna_set:
	tna = x.split("|")
	t = tna[0]
	a = tna[1]
	if a in mydict.keys():
		mydict[a] += 1
	else:
		mydict[a] = 1
     
for k in mydict:
	twoD_list.append([mydict[k],k])

twoD_list.sort()

print(twoD_list)

# create list with zeros

list_of_artist_count = [0] * 64
for e in twoD_list:
	list_of_artist_count[e[0]-1] += 1

print()
print("total size:",len(mydict))
print()
print("num songs\t num artists")
print()

counter = 0
for x in list_of_artist_count:
	if x != 0:
		print(counter + 1,"\t\t",x)
	counter += 1

print("\nsum:",sum(list_of_artist_count))

