import os

def is_Prime(n):
	if n < 2:
		isPrime = False
	for i in range (2, n):
		if (n%i == 0):
			return False
			break
	return True

os.mkdir("BT")
F = open("BT/snt", "w")
s = ""
for i in range(10):
	n = input("Nhap mot so nguyen: ")
	if is_Prime(int(n)):
		s += str(n) + " "
F.write(s)
F.close()