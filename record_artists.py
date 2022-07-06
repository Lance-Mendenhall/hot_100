from datetime import date
import pandas as pd


def write_stats():

	songs = pd.read_csv("charts.csv")

	songs.columns = ['title','artist']

	q = open("common_artists.txt","a")

	today = date.today()
	dd = today.strftime("%B %d, %Y")

	q.write("\n\n")
	q.write(dd)
	q.write("\n\n")

	counter = 0
	for idx, name in enumerate(songs['artist'].value_counts().index.to_list()):

		q.write(name)
		q.write('\t')
		z = songs['artist'].value_counts()[idx]
		q.write(str(z))
		q.write('\n')

		if counter > 18:
			break;
		counter += 1

	q.write('\n\n')

	q.close()
