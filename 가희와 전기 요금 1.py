for a in range(100,1000):
    for m in range(100, 10**5):
        # for i in range(int(input())):
        #     # a, m = map(int, input().split())
        w_m = m / 60
        print(round((int(a*w_m)) * 105.6 // 1000))