# Kiem tra so nguyen to
def is_Prime(n):
	if n < 2:
		isPrime = False
	for i in range (2, n):
		if (n%i == 0):
			return False
			break
	return True

while True:
	n = int(input("Nhap n: "))
	
	if is_Prime(n):
		print(str(n) + " la so nguyen to") 
	else:
		print(str(n) + " khong phai la so nguyen to")

	kt = input("Ban muon KT so khac (C/K): ")
	if (kt == "K" or kt == "k"):
		break

