a = int(input())
b = int(input())
s = a*b
b = list(str(b))
b.reverse()
b = ''.join(b)
for i in b:
    print(a*int(i))
print(s)