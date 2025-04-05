from math import gcd
import random


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def isprime(p):
    if p == 2 or p == 3:
        return True
    if p < 2 or p % 2 == 0:
        return False

    r = 0
    d = p-1
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in primes:
        if a >= p:
            continue
        x = pow(a, d, p)
        if x == 1 or x == p-1:
            continue
        for i in range(r-1):
            x = pow(x, 2, p)
            if x == p-1:
                break
        else:
            return False

    return True


def pollard_rho(n):
    if isprime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    while True:
        x = random.randrange(2, n)
        y = x
        c = random.randrange(2, n)
        f = lambda x: (pow(x, 2, n) + c) % n
        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d

def prime_factorziation(n):
    re = []
    stack = [n]

    while stack:
        c = stack.pop()
        if c == 1:
            continue
        if isprime(c):
            re.append(c)
            continue
        d = pollard_rho(c)
        stack.append(d)
        stack.append(c // d)

    return sorted(re)


n = int(input())
for i in prime_factorziation(n):
    print(i)
