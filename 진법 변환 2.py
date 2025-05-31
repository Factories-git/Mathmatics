n, b = map(int, input().split())
re = ''
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n:
    re += str(s[n%b])
    n //= b
print(re[::-1])