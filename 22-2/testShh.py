def isPerfect(n):
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

a = input("Nhap 1 so: ")
if isPerfect(int(a)):
	print("True")
else:
	print("False")