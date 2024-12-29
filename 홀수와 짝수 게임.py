import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    odd = 0
    cards = list(map(int, input().split()))
    for i in cards:
        if i % 2 == 1:
            odd += 1
    even = n - odd
    if (even == n and n % 2 == 0) or (odd == n and n % 2 == 0):
        print('heeda0528')
        continue
    elif (even == n and n % 2 == 1) or (odd == n and n % 2 == 1):
        print('amsminn')
        continue
    if even >= odd:
        print('heeda0528')
    else:
        print('amsminn')