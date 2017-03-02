# Nhap 10 so nguyen -> In ra cac so trong khoang  [10,100] va tong cac so do

sum = 0
for i in range (10):
	x = float(input("Nhap x: "))
	if x >= 10 and x <= 100:
		print(str(x) + " nam trong khoang [10, 100]")
		sum += x

print(sum)