import sys

buffer = sys.stdout.flush

n = int(input())
temp = [''] * (n+1)
temp[1] = 's'
res = ['' ] * (n+1)
one_more_ques = True
for i in range(2, n+1):
    print(f'? 1 * {i}')
    buffer()
    reply = input()
    if reply == '-':
        temp[i] = 'd'
    else:
        if one_more_ques:
            print(f'? 1 + {i}')
            buffer()
            reply = input()
            if reply == '-':
                res[1] = '-'
            else:
                res[1] = '+'
            one_more_ques = False
        temp[i] = 's'

if one_more_ques:
    print(f'? 2 + 3')
    buffer()
    reply = input()
    if reply == '-':
        res[1] = '+'
    else:
        res[1] = '-'
for i in range(2, n+1):
    if temp[i] == 'd':
        res[i] = '+' if res[1] == '-' else '-'
    else:
        res[i] = res[1]
print(f"! {' '.join(res[1:])}") # - + - +
buffer()