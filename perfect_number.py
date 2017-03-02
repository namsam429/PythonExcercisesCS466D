n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
sum = 0

for i in range(n,m):
	if i == 1:
		continue;
	sum = 1
	for j in range (2,i):
		if(i%j == 0):
			sum += j
	if sum == i:
		print(i)