# for _ in range(1,101):
#     run = True
#     n = _
#     for i in range(1,9):
#         for j in range(1,9):
#             if str(n) in f'{i} * {j} = {i*j}':
#                 print(1)
#                 run = False
#         if not run:
#             break
#     print(0,_)
n = int(input())
for i in range(1,10):
    for j in range(1,10):
        if str(n) in f'{i} * {j} = {i*j}':
            print(1)
            exit(0)
print(0)