isContinue = True
while isContinue:
	n = int(input("Ban muon in bang nhan may: "))
	for i in range(1,11):
		print("%d x %d = %d" %(n,i,n*i))
	c = input("Ban co muon tiep tuc? (Y/N): ")
	if c == "N":
		isContinue = False