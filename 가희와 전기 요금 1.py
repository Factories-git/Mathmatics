q = int(input())
for i in range(q):
    a, m = map(int, input().split())
    print(int((105.6 * (a*m)) // 60000))