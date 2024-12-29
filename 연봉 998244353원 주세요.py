import sys
import math

input = sys.stdin.readline

x,q = map(int, input().split())
query = []
for i in range(q):
    query.append(int(input()))

def caculate(X,A):
    sala = X
    for i in range(1, A+1):
        sala = math.ceil(sala / i) * i
    return sala


for A in query:
    print(caculate(x, A))