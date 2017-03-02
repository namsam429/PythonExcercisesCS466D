def is_Perfect(n):
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

n = int(input("Ma trận có n dòng: "))
m = int(input("Ma trận có m cột: "))

fileSoNguyen = open("mtrsong", "w+")
fileSoNguyen.write(str(n) + " " + str(m) + "\n")

fileSoNguyen.seek(0,0)
s = fileSoNguyen.readline()
# print(s.split(" ")[0] + " " + s.split(" ")[1])

Matrix = [[0 for x in range(m)] for y in range(n)]

for i in range(n):
	for j in range(m):
		Matrix[i][j] = input("Nhập giá trị cho phần tử dòng " + str(i+1) + " cột " + str(j+1) + ": ")

fileSoHoanHao = open("Shh", "w+")
for i in range(n):
	for j in range(m):
		if is_Perfect(int(Matrix[i][j])) == True:
#			print(Matrix[i][j])
			fileSoHoanHao.write(Matrix[i][j] + "\n")
		fileSoNguyen.write(str(Matrix[i][j]) + " ")
	fileSoNguyen.write("\n")

text = fileSoHoanHao.read()
print(text)

fileSoHoanHao.close()
fileSoNguyen.close()