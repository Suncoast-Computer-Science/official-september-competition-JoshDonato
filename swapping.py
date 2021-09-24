x = []
for i in range(int(input())):
	x.append(str(input()))

for j in x:
	s = j[0]
	e = j[-1]
	print(e + j[1:-1] + s)
