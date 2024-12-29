while True:
    a,b,c,d = map(int, input().split())
    if a == b == c == d == 0:
        break
    ma = max(a,b)
    mi = min(a,b)
    mi1 = min(c,d)
    ma1 = max(c,d)
    print(mi1 - ma, ma1 - mi)