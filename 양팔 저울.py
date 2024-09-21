def dfs(idx,total):
    global add
    if total > add:
        return
    if idx == k:
        if 0 < total <= add:
            ch[total] = 1
    else:
        dfs(idx + 1, total + w[idx])
        dfs(idx + 1, total - w[idx])
        dfs(idx +1, total)
k = int(input())
w = list(map(int, input().split()))
add = sum(w)
ch = [0] * (add+1)
dfs(0,0)
count = 0
for x in ch:
    if x == 0:
        count += 1
print(count - 1)