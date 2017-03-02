# Kiem tra day so nguyen, in trung binh cong cac so hoan hao
def is_Perfect(n):
	isPerfect = True
	if n == 1:
		return False
	s = 0
	for i in range (1,n-1):
		if n%i == 0:
			s += i

	if n == s:
		return True
	else:
		return False

myList = []
while True:
	a = input("Nhap so nguyen (An E de ket thuc nhap): ")
	if a == "E":
		break
	else:
		myList.append(int(a))

myPerfectNumber = []
for i in myList:
	if is_Perfect(i) == True:
		print(str(i) + " la so hoan hao")
		myPerfectNumber.append(i)

if len(myPerfectNumber) == 0:
	print("Khong co so hoan hao")
else:
	s = 0
	for i in myPerfectNumber:
		s += (i)

	print("Trung binh cong cua cac so hoan hao: " + str(s/len(myPerfectNumber)))