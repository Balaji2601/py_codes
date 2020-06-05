import collections
with open("details.txt") as f:
	std_det = f.readlines()
std_det = [l.strip().split("\t") for l in std_det]

st_details = collections.namedtuple("st_details",["id","name","fname"])

dl = [st_details(n[0],n[1],n[2]) for n in std_det]

Marks = collections.namedtuple("Marks",["id","marks"])

def readfile(fname):
	with open(fname) as f:
		std_quiz = f.readlines()
	tot_marks = float(std_quiz[0].strip())
	std_quiz = [l.strip().split("\t") for l in std_quiz[1:]]
	l = [Marks(n[0],n[1]) for n in std_quiz]
	return l,tot_marks

ql,q_tot = readfile("quiz.txt")
ml,m_tot = readfile("mid.txt")
el,e_tot = readfile("end.txt")

tot_marks = q_tot + m_tot + e_tot

def outmarks(l,id):
	for marks in l:
		if marks.id == id:
			return float(marks.marks)

ranklist = []
for n in dl:
	row = []
	row.append(n.id)
	row.append(n.name)
	total = outmarks(ql,n.id) + outmarks(ml,n.id) + outmarks(el,n.id)
	per = (total/tot_marks)*100
	per = "{:.2f}".format(per)
	row.append(per)
	ranklist.append(row)

ranklist.sort(key = lambda k: float(k[2]),reverse = True)

def option1():
	print(ranklist[0][1])

def option2():
	with open("ranklist.txt","w") as f:
		count = 0
		for row in ranklist:
			count+=1
			s = str(count) + "\t" + row[0] + "\t" + row[1] + "\t" + row[2] + "\n"
			f.write(s)
	print("Saved to ranklist.txt")

if __name__ == "__main__":
	inp = int(input("Enter option 1 or 2 :"))
	if inp == 1:
		option1()
	else:
		option2()
