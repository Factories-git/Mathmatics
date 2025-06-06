import math
min,max = map(int, input().split())
check = [False] * (max-min +1)
for i in range(2,int(math.sqrt(max)+1)):
    pow = i * i
    start_idx = int(min / pow)
    if min % pow != 0:
        start_idx += 1
    for j in range(start_idx, int(max / pow) + 1):
        check[int((j * pow) - min)] = True

count = 0

for i in range(0,max-min+1):
    if not check[i]:
        count += 1

print(count)
