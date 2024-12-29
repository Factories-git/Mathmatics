for i in range(int(input())):
    a,b = map(int, input().split())
    inn = b - a if b > a else 43 - (a-b)
    out = a-b if a > b else 43 - (b-a)
    if inn < out:
        print('Inner circle line')
    elif inn > out:
        print('Outer circle line')
    else:
        print('Same')