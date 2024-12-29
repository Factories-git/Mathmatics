a,b = map(int, input().split())
c = int(input())
if c >= 60:
    h,m = divmod(c,60)
    a += h
    b += m
else:
    b += c
if b >= 60:
    b %= 60
    a += 1
if a >= 24:
    a -= 24
print(a, b)