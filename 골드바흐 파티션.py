import sys

input = sys.stdin.readline
check = [False] + [False] + [True] * 1000000
prime = []
for i in range(2, 1000000+1):
    if not check[i]:
        continue
    prime.append(i)
    for j in range(i+i, 1000001, i):
        check[j] = False

t = int(input())
for _ in range(t):
    c = 0
    n = int(input())
    s = set()
    for i in prime:
        if check[n - i] and n-i > 0:
            if f'{n-i} {i}' in s:
                continue
            c += 1
            s.add(f'{i} {n-i}')
    print(c)