import sys

input = sys.stdin.readline

primes_count = []
primes = [False] * 2 + [True] * (123456 * 2)
for i in range(2, 123456 * 2 + 1):
    if primes[i]:
        for j in range(i+i, 123456 * 2 + 1, i):
            primes[j] = False
for i in primes:
    if not primes_count:
        primes_count.append(0)
        continue
    if i:
        primes_count.append(primes_count[-1] + 1)
    else:
        primes_count.append(primes_count[-1])

while True:
    n = int(input())
    if n == 0:
        break
    print(primes_count[2*n] - primes_count[n])