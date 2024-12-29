import sys

input = sys.stdin.readline

for i in range(int(input())):
    re = 0
    for k in range(1,int(input())+1):
        re += k * sum(range(k+2))
    print(re)