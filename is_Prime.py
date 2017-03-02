n = int(input("Nhap n: "))
isPrime = True
if n < 2:
	isPrime = False
	
for i in range (2,n):
	if (n%i == 0):
		isPrime = False
		break
if isPrime:
	print(str(n) + " la so nguyen to")
else:
	print(str(n) + " khong phai la so nguyen to")