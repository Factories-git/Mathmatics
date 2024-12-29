n = int(input()) #응시생의 수
student = list(map(int, input().split())) #응시장에 있는 응시생의 수
main, sub = map(int, input().split()) #총감독관이 감독할 수 있는 응시생의 수, 부 감독관이 감독할 수 있는 응시생의 수
re = 0 #정답 변수
for i in student: #응시장에 있는 응시생에 대해 반복
    j = i - main #총감독관이 무조건 필요하단 가정하에, 응시생의 수에서 총감독관의 감독 가능 응시생을 뺌
    if j < 0:
        re += 1
        continue
    re += 1 #총감독관 때문에 감독관 수 추가
    if j != 0: #만약 나눌수 있다면
        if j % sub != 0: #나누었을때 나머지가 있다면
            re += (j // sub)+1 #정답에 나눈 몫 + 나머지(즉 하나 더 필요함)
        else: #나머지가 없을 경우
            re += j // sub #그냥 더해줌
print(re) #정답 결과
