f1=open('data/SPC members.txt','r')
f2=open('SPC-html.txt','w')
line = f1.readline()
while line!="":
	line = line.strip(" \r\n")
	line = line.split(', ')
	firstName = line[0]
	lastName = line[1]
	affiliation = line[2]
	for i in range(3, len(line)):
		affiliation += ", "
		affiliation += line[i]
	f2.write("<li>"+firstName+" "+lastName+" ("+affiliation+")</li>"+"\n")
	line = f1.readline()
f1.close()
f2.close()


f3=open('data/PC members.txt','r')
f4=open('PC-html.txt','w')
line = f3.readline()
while line!="":
	line = line.strip(" \r\n")
	line = line.split(', ')
	firstName = line[0]
	lastName = line[1]
	affiliation = line[2]
	for i in range(3, len(line)):
		affiliation += ", "
		affiliation += line[i]
	f4.write("<li>"+firstName+" "+lastName+" ("+affiliation+")</li>"+"\n")
	line = f3.readline()
f3.close()
f4.close()