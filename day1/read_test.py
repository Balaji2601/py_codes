import collections
with open("directory.txt") as f:
	content = f.readlines()
content = [l.strip().split("\t") for l in content]

#content.sort(key = lambda k : k[1])

Tele = collections.namedtuple("Tele", ["num", "name"])

tl = []
for n in content:
	t = Tele(n[0],n[1])
	tl.append(t)

tl.sort(key = lambda k: k.name)



with open("dir-new.txt", "w") as f:
	for row in content:
		s = row[1] + "\t" + row[0] + "\n"
		f.write(s)

