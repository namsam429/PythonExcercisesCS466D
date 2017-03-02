def isPrime(n):
	if n < 2:
		return False
	for i in range(3,n):
		if n%i == 0:
			return False
	return True

def isPerfect(n):
	i = 2
	while True:
		if isPrime(2**i-1):
			x = 2**(i-1)*(2**i-1)
		if x == n:
			return True
		if x > n:
			return False
		i = i + 1

a = input("Nhap 1 so: ")
if isPerfect(int(a)):
	print("True")
else:
	print("False")

