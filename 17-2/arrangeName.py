list = []
for i in range(4):
	list.append(input("Nhap ten: "))

for i in range(len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			name = list[i]
			list[i] = list[j]
			list[j] = name

for x in list:
	print(x)
