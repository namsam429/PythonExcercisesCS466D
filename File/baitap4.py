import os
if not os.path.exists("BT"):
    os.makedirs("BT")
F = open("BT/baitap4", "w+")
for i in range(4):
	s = input("Nhap cau van ban thu " + str(i+1) + ": ")
	F.write(s + "\n")
F2 = open("BT/luumoi", "w")
F.seek(0,0)
F2.write(F.readline())
F.readline()
F.readline()
F2.write(F.readline())
F2.close()

F3 = open("BT/snt", "w+")
for i in range(10):
	s = input("Nhap so nguyen thu " + str(i+1) + ": ")
	F3.write(s + "\n")
F3.seek(0,0)
s = 0
while True:
	x = F3.readline()
	if x == "":
		break
	s += int(x)
print(s)
F.write(str(s) + "\n")

F3.close()
F.close()