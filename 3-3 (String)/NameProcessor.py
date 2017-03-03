# Xu ly khoang trang va sap xep ten

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
fileSinhVien2 = open("tensv2", "w+")
fileSinhVien3 = open("tensv3", "w+")
fileSinhVien4 = open("tensv4", "w+")
for t in listSv:
	fileSinhVien.write(t + "\n")
	
	text = ""
	for c in t:
		text = c + text
	fileSinhVien4.write(text + "\n")

	text2 = ""
	for c in t.split(" "):
		text2 = c + " " + text2
	fileSinhVien2.write(text2.strip() + "\n")

	text3 = ""
	for c in text2:
		text3 = c + text3
	fileSinhVien3.write(text3.strip() + "\n")

# fileSinhVien.seek(0)
# print(fileSinhVien.read())

fileSinhVien.close()
fileSinhVien2.close()
fileSinhVien3.close()
fileSinhVien4.close()
