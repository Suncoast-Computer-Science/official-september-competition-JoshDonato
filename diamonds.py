n = int(input())

for i in range(1, 1+n): #all diamonds
	for j in range(1, 1+ n - 2 * abs(i - int((n+1)/2))): #columns of each diamond
		m = n - 2 * abs(i - int((n+1)/2))
		for k in range(abs(int((m+1) / 2) - j)):
			print(" ",end="")
		for k in range(m - 2 * abs(j - int((m+1)/2))):
			print("*",end="")
		for k in range(abs(int((m+1) / 2) - j)):
			pass #print(" ",end="")
		print("")
	print("")
