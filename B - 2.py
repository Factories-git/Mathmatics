a,b = map(int, input().split())
print(str(a//b) ,end='.')
d = a%b
i = 0
while i < 1000:
    d *= 10
    print(str(d//b) , end='')
    d %= b
    if d == 0:
        break
    i += 1
#git clone https://github.com/Factories-git/BaekjoonOnlineJudge.git
