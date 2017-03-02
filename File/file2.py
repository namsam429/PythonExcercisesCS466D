f = open("int", "r")
s = 0
while True:
	x = f.readline()
	if x == "":
		break
	print(x)
	s += int(x)
print(s)