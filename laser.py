T = []
n = int(input())
for i in range(n):
	T.append(int(input()))

S = []
for i in range(int(n/2)):
	S.append(T[2*i] + T[2*i + 1])

S.sort()
print(S)
