n, b = input().split()
n = n[::-1]
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
re = 0

for i in range(len(n)):
    re += (int(b) ** i) * s.index(n[i])
    print(int(b) ** i, s.index(n[i]))
print(re)