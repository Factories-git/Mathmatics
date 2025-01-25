n = int(input())
sequence = list(map(int, input().split()))
if n == 2:
    print('Yes')
    exit(0)
for i in range(n-2):
    if sequence[i] * sequence[i+2] != sequence[i+1] ** 2:
        print('No')
        exit(0)
print('Yes')