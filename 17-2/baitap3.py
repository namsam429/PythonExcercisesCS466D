fileVanBan = open("baihoc1", "w+")
fileVanBan.write(input("Nhap van ban bat ky: "))
fileVanBan.seek(0)
text = fileVanBan.read()
listAlpha = []
for i in range(len(text)):
	if text[i] not in listAlpha and text[i].isalpha():
		listAlpha.append(text[i])

listAlpha.sort()
for i in listAlpha:
	print(i + "\t" + str(text.count(i))) 
