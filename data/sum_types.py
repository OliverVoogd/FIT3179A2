file = "g:\My Drive\_UNI\FIT3179\A2\data\pend-gdis-1960-2018-disasterlocations.csv"
d = {} # disastertype: {year, count}
country = 1
year = 4
dtype = 13 


for disaster in ["Drought", "Flood", "Landslide", "Earthquake", "Volcanic activity"]:
	d[disaster] = {"1960": 0}
	for y in range(1961, 2019):
		d[disaster][str(y)] = 0


with open(file, "r", errors="ignore") as f:
	cols = f.readline().split(",")
	# now actually read the data
	for line in f:
		l = line.split(",")
		#print(l)
		if len(l) <= dtype: continue

		if l[dtype] in d.keys():
			if l[year] in d[l[dtype]].keys():
				d[l[dtype]][l[year]] += 1
			else:
				d[l[dtype]][l[year]] = 1
		else:
			d[l[dtype]] = {}

#print(d)

with open("g:\My Drive\_UNI\FIT3179\A2\data\summed_disastertype_year.csv", "w") as o:
	o.writelines(["disastertype,year,count\n"])
	for t in d.keys():
		for y in d[t].keys():
			o.write(t + "," + y + "," + str(d[t][y]) + "\n")
