listSV = []
while True:
	text = input("Nhap ten sv: ")
	if text == "E":
		break
	listSV.append(text)

for i in range(len(listSV)-1):
	for j in range(i+1,len(listSV)):
		name1 = listSV[i].split(" ")[len(listSV[i].split(" "))-1]
		name2 = listSV[j].split(" ")[len(listSV[j].split(" "))-1]
		if  name1 > name2:
			text = listSV[i]
			listSV[i] = listSV[j]
			listSV[j] = text

for i in listSV:
	print(i)