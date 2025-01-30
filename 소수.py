m = int(input())
n = int(input())
d = 0
arr = [False, False] + [True] * (n-1)

for i in range(2, n+1):
    if arr[i]:
        for j in range(i+i, n+1, i):
            arr[j] = False

min_ = 0
re = 0
for i in range(m, n+1):
    if arr[i]:
        if min_ == 0:
            min_ = i
        re += i

if re == min_ == 0:
    print(-1)
    exit(0)
print(re)
print(min_)