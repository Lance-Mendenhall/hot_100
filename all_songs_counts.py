from datetime import datetime, date


class Song_for_stats:
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist
		self.counter = 1

class Records:
	def __init__(self, weeks, count):
		self.weeks = weeks
		self.count = count

songs_for_stats = []
songsGrouped = []
mydict = {}
        

def print_timestamp():
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	print(dt_string)


def write_stats():

    with open("charts.csv") as f:
        for line in f:
            if(line.strip(' \n') != ""):
                # print(line)
                sss = line.split(",")
                t = sss[0].strip()     # title
                a = sss[1].strip()     # artist
                s = Song_for_stats(t,a)          # song
                songs_for_stats.append(s)


    for s in songs_for_stats:
        key = s.title + "|" + s.artist
        if key in mydict.keys():
            mydict[key] += 1
        else:
            mydict[key] = 1

    for s in mydict:
        ttaa = s.split("|")
        title = ttaa[0]
        artist = ttaa[1]
        mysong = Song_for_stats(title,artist)
        mysong.counter = mydict[s]
        songsGrouped.append(mysong)

    songsGrouped.sort(key=lambda x: x.counter, reverse=True)


    xdict = {}

    for s in songsGrouped:
        # need 2 things - number of weeks, and how many with that count
        # key is weeks, value is num of songs with that num of weeks
        if s.counter in xdict.keys():
            xdict[s.counter] += 1
        else:
            xdict[s.counter] = 1

    record_list = []

    for key in xdict:
        val = xdict[key]
        my_record = Records(key,val)
        record_list.append(my_record)

    record_list.sort(key = lambda x: x.weeks)

    # for x in record_list:
    # 	print("weeks",x.weeks,"\t",x.count)


    total = len(songsGrouped)

    avg = str(len(songs_for_stats)/total)

    q = open("count_stats.txt","a")

    today = date.today()
    dd = today.strftime("%B %d, %Y")

    q.write("\n\n")
    q.write(dd)
    q.write("\n\n")

    q.write("total: ")
    q.write(str(total))
    q.write("\n\n")

    q.write("weeks\tcount")
    q.write("\n\n")

    for x in record_list:
        q.write(str(x.weeks))
        q.write("\t\t")
        q.write(str(x.count))
        q.write("\n")

    q.write("\nAverage weeks on chart: ")
    q.write(avg)
    q.write("\n")

    q.close()

