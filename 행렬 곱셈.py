n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
s, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(s)]

ans = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for u in range(m):
            ans[i][j] += (arr1[i][u] * arr2[u][j])
for i in ans:
    print(*i)