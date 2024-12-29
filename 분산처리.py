import sys

input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int, input().split())
    l = [a ** i % 10 for i in range(1,5)]
    print(l[(b % 4) - 1] if a != 10 else 10)