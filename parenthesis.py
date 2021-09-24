#To check if a string of parentheses are balanced or not.
P = []
for i in range(int(input())):
	P.append(str(input()))

for j in P:
	x = 0
	for p in range(len(j)):
		if j[p] == "(": 
			x += 1
		else: 
			x -= 1
		if(x < 0): break
	print(x == 0)
