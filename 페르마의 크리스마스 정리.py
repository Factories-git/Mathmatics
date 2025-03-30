def sieve_of_eratosthenes(n):
    prime = [False]*2 + [True] * (n-1)
    for i in range(2, n+1):
        if not prime[i]:
            continue
        for j in range(i+i, n+1, i):
            prime[j] = False
    return prime


primes = sieve_of_eratosthenes(1000000)
sieve1 = [0]
sieve2 = [0]
for i in range(1, len(primes)):
    if primes[i]:
        sieve1.append(sieve1[-1] + 1)
    else:
        sieve1.append(sieve1[-1])
for i in range(1, len(primes)):
    if primes[i]:
        if i % 4 == 1 or i == 2:
            sieve2.append(sieve2[-1] + 1)
        else:
            sieve2.append(sieve2[-1])
    else:
        sieve2.append(sieve2[-1])
while True:
    p_c = 0
    r_c = 0
    l, u = map(int, input().split())
    r_l = l
    if l == u == -1:
        break
    if u < 0:
        print(l, u, 0, 0)
        continue
    if l <= 0:
        r_l = 1
    print(l, u, sieve1[u] - sieve1[r_l-1], sieve2[u] - sieve2[r_l-1])