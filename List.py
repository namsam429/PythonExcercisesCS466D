myList = []
n = int(input("Nhap so luong phan tu cua List: "))
for i in range(0,int(n)):
	x = int(input("Nhap phan tu thu %d: " %(i+1)))
	myList.append(x)
print("Your list: " + str(myList))

x = int(input("Nhap x: "))
if x in myList:
	print("%d co trong myList" %(x))
	print("%d co trong myList %d lan" %(x,myList.count(x)))
else:
	print("Khong co trong myList")
