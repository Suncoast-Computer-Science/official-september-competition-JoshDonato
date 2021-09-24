b = str(input())
p = str(input())
x = int(input())
print((b+p if len(b) < len(p) else p+b) if len(p)+len(b) <= x else False)
