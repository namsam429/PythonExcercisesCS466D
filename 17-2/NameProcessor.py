fileSinhVien = open("tensv", "w+")
for i in range(4):
	name = input("Nhap ten sinh vien: ")
	fileSinhVien.write(name + "\n")

fileSinhVien.seek(0)
listSv = []
while True:
	text = fileSinhVien.readline()
	if(text == ""):
		break

	s = ""
	for i in range(len(text.split(" "))):
		if text.split(" ")[i].strip() != "":
			s += text.split(" ")[i].strip() + " "
	listSv.append(s.strip())
fileSinhVien.close()

fileSinhVien = open("tensv", "w+")
for t in listSv:
	fileSinhVien.write(t + "\n")
fileSinhVien.close()

for i in range(len(listSv)-1):
	for j in range(i+1, len(listSv)):
		name1 = listSv[i].split(" ")[len(listSv[i].split(" "))-1]
		name2 = listSv[j].split(" ")[len(listSv[j].split(" "))-1]
		# print(name1)
		# print(name2)
		if  name1 > name2:
			text = listSv[i]
			listSv[i] = listSv[j]
			listSv[j] = text

fileSinhVien = open("tensv", "w+")
for t in listSv:
	fileSinhVien.write(t + "\n")
fileSinhVien.close()

fileSinhVien.seek(0)
print(fileSinhVien.read())

fileSinhVien.close()