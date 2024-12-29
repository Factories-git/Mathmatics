import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a,b,c,p = map(int, input().split())
    p_volume = p**2
    if (a % p == 0 and b % p == 0) or (a % p == 0 and c % p == 0) or (b % p == 0 and c % p == 0):
        print(1)
        continue
    print(0)