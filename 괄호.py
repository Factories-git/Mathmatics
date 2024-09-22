import sys

input = sys.stdin.readline


def solution(s):
    answer = True
    stack = []
    for l in s:
        if l == '(':
            stack.append(l)
        else:
            if not '(' in stack:
                return False
            stack.pop()
    if '(' in stack:
        answer = False
    return answer


for i in range(int(input())):
    s = input().strip()
    print('YES' if solution(s) else 'NO')