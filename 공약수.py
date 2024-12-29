n = int(input())
l = list(map(int, input().split()))
for i in range(1,min(l)+1):
    if len(l) == 3:
        if l[0] % i == 0 and l[1] % i == 0 and l[2] % i == 0:
            print(i)
    else:
        if l[0] % i == 0 and l[1] % i == 0:
            print(i)