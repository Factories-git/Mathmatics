from collections import Counter
def solution(arr):
    answer = 1
    maxes = {i : 0 for i in range(100)}
    for n in arr:
        prime_factors = []
        while n != 1:
            for i in range(2, n+1):
                if n % i == 0:
                    prime_factors.append(i)
                    n //= i
                    break
        c = Counter(prime_factors)
        for i in prime_factors:
            maxes[i] = max(maxes[i], c[i])
    for num, count in maxes.items():
        if count == 0:
            continue
        answer *= num ** count
    return answer


print(solution([1,2,3]))