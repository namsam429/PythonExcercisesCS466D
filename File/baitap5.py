import os

def is_Prime(n):
	if n < 2:
		return False
	for i in range (2, n):
		if (n%i == 0):
			return False
			break
	return True

fileSoNguyen = open("Songuyen", "w+")
while True:
	kt = input("Nhap vao mot so nguyen (Nhan E de ket thuc): ")
	if kt == "E" or kt == "e":
		break
	fileSoNguyen.write(kt + "\n")

fileSoNguyen.seek(0,0)

fileSoNguyenTo = open("Snto", "w+")
for sng in fileSoNguyen:
	if is_Prime(int(sng)) == True:
		fileSoNguyenTo.write(sng)

s = 0
fileSoNguyenTo.seek(0,0)
while True:
	x = fileSoNguyenTo.readline()
	if x == "":
		break
	s += int(x)
fileSoNguyenTo.write(str(s))

fileSoNguyenTo.close()
fileSoNguyen.close()

os.remove("Songuyen")
os.rename("Snto", "Songuyento")