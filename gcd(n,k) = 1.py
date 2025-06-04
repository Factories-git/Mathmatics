from math import gcd
import random
n = int(input())


def is_prime_miller_rabin(p):
    if p == 2 or p == 3: return True
    if p < 2 or p % 2 == 0: return False

    r = 0
    d = p-1
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
        if a >= p: continue
        x = pow(a, d, p)
        if x == 1 or x == p-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, p)
            if x == p-1:
                break
        else:
            return False
    return True


def pollard_rho(p):
    if is_prime_miller_rabin(p):
        return p
    if p == 1:
        return 1
    if not p % 2:
        return 2
    if not p % 3:
        return 3
    if not p % 5:
        return 5

    while True:
        x = random.randrange(2, p)
        y = x
        c = random.randrange(2, p)
        f = lambda x : (pow(x,2,p) + c) % p
        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), p)
        if d != p and p % d == 0:
            return d


def prime_factoriziation(p):
    result = p
    re = set()
    stack = [n]

    while stack:
        curr = stack.pop()
        if curr == 1: continue
        if is_prime_miller_rabin(curr):
            re.add(curr)
            continue
        d = pollard_rho(curr)
        stack.append(d)
        stack.append(curr//d)
    for i in re:
        result -= result // i
    return result

print(prime_factoriziation(n))