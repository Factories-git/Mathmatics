import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer1 *= denom2
    numer2 *= denom1
    denom2 *= denom1
    h = numer1 + numer2
    n = math.gcd(h,denom2)
    answer.append(h // n)
    answer.append(denom2 // n)
    return answer


numer1, denom1 = map(int, input().split())
numer2, denom2 = map(int, input().split())
print(' '.join(map(str,solution(numer1, denom1, numer2, denom2))))