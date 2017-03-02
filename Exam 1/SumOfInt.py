# Tinh tong cac chu so trong 1 so nguyen
def sumOfInt(n):
	s = 0
	for i in range(0,len(n)):
		s += int(n[i])
	return s

while True:
	n = input("Nhap mot chu so nguyen: ")
	print(sumOfInt(n))
	kt = input("Ban co muon KT day so khac? (C/K): ")
	if kt == "K" or kt == "k":
		break