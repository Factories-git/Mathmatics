import sys

input = sys.stdin.readline

def facto(num):
    re = 1
    for j in range(1,num+1):
        re *= j
    return len(str(re))
for i in range(int(input())):
     n = int(input().strip())
     print(facto(n))