# Kiem tra day so tang dan
def isIncremental(myList):
	for i in range (0,len(myList)-1):
		if myList[i] > myList[i+1]:
			return False
	return True

while True:
	myList = []
	while True:
		a = input("Nhap so nguyen (An E de ket thuc nhap): ")
		if a == "E":
			break
		else:
			myList.append(int(a))

	if isIncremental(myList) == True:
		print("Day la day so tang dan")
	else:
		print("Day khong phai day so tang dan")
	kt = input("Ban co muon KT day so khac? (C/K): ")
	if kt == "K" or kt == "k":
		break