fo = open("inp", "r+")
str = fo.read()
print(fo.name)
print(str)
for i in range(10):
	x = input("Nhap so nguyen: ")
	str += x + " "
fo.write(str)
fo.close()