def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False

    r = 0
    d = n-1

    while d % 2 == 0:
        d //= 2
        r += 1

    for i in [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if i >= n: continue
        x = pow(i, d, n)
        if x == 1 or x == n-1: continue
        for _ in range(r):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


cnt = 0
l, h = map(int, input().split())
palindromes = set()
for i in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    for j in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        for k in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            for r in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                for c in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    for p in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                        s = ''.join([i, j, k, r, c, p]).lstrip('0')
                        if not s: continue
                        palindromes.add(int(s + s[::-1]))
                        palindromes.add(int(s + s[:-1][::-1]))

for i in palindromes:
    if h >= i >= l:
        if is_prime(i):
            cnt += 1
print(cnt)