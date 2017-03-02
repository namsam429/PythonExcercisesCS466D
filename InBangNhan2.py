s = ""
for i in range(1,11):
	for x in range(2,6):
		s += str(x) + " x " + str(i) + " = " + str(x*i) + "\t"
	s = s + "\n"
s = s + "\n"
for i in range(1,11):
	for x in range(6,10):
		s += str(x) + " x " + str(i) + " = " + str(x*i) + "\t"
	s = s + "\n"
print(s)
