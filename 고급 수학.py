import sys

input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    a,b,c = sorted(map(int, input().split()))
    print(f'Scenario #{i}:')
    print('yes' if a**2 + b**2 == c**2 else 'no')
    if n != i:
        print()
