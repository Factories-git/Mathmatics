n = int(input())
new_ = list(str(n))
new = 0
c = 0
while new != n:
    new = int(str(new_[-1] + str(sum(list(map(int, new_))))))
    new_ = list(str(new))
    c += 1
print(c)