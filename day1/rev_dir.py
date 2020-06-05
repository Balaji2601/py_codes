with open("directory.txt") as f:
	content = f.readlines()
content = [l.strip().split("\t") for l in content]

content.sort(key = lambda k:k[1])

with open("rev_dir.txt","w") as f:
	for row in content:
		s = row[1] + "\t\t" + row[0] + "\n"
		f.write(s)