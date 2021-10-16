old = open("g:\My Drive\_UNI\FIT3179\A2\data\emdat_trimmed_joined_sedac.csv", "r")
cols = old.readline().split(",")
i = cols.index("Start Year")
print(i)
new = open("g:\My Drive\_UNI\FIT3179\A2\data\emdat_trimmed_joined_sedac_datefixed.csv", "w")
new.write(",".join(cols[:i]))
new.write(",date,")
new.write(",".join(cols[i+3:]))


for line in old:
	try:
		line = line.split(",")
		if (line[i+2] == "0"):
			line[i+2] = "1"
		if (line[i+1] == "0"):
			line[i+1] = "1"
			
		date = line[i+2] + "/" + line[i+1] + "/" + line[i]

		for c in range(i):
			new.write(line[c])
			new.write(",")

		new.write(date)
		new.write(",")

		new.write(",".join(line[i+3:]))
	except:
		continue