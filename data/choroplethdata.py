f = open("g:\My Drive\_UNI\FIT3179\A2\data\emdat_trimmed_joined_sedac_datefixed.csv", "r")

cols = f.readline().split(",")
country = cols.index("country")
deaths = cols.index("Total Deaths")
d = {}
for line in f:
	try:
		line = line.split(",")
		if (line[country] == "United States"):
			line[country] = "United States of America"
		if (line[country] in d):
			d[line[country]] += int(line[deaths])
		else:
			d[line[country]] = int(line[deaths])
	except:
		continue
f.close()

out = open("g:\My Drive\_UNI\FIT3179\A2\data\emdat_trimmed_joined_sedac_datefixed_choropleth.csv", "w")
out.write("country,cumulativeDeaths\n")
for c in d.keys():
	out.write(c + "," + str(d[c]) + "\n")

out.close()