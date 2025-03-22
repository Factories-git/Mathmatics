import sys

input = sys.stdin.readline
prime = [False] + [False] + [True] * 10000
for i in range(2, 10001):
    if not prime[i]:
        continue
    for j in range(i+i, 10001, i):
        prime[j] = False
t = int(input())
for _ in range(t):
    n = int(input())
    i = j = n // 2
    while True:
        if prime[i] and prime[j]:
            print(i, j)
            break
        else:
            i -= 1
            j += 1