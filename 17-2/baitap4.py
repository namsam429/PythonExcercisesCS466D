fileSinhVien = open("name", "w+")
for i in range(10):
	name = input("Nhap ten sinh vien: ")
	fileSinhVien.write(name +"\n")

fileSinhVien.seek(0)