# n,bpm,k = map(float, input().split())
# re = 0
# last = 1
# n,k = int(n), int(k)
# for i in range(k):
#     M,s = map(float, input().split())
#     M = int(M)
#     if i == 0:
#         re += (M - last) *( 4 * 60 / bpm)
#     re += (M-last) *(4 * 60 / s)
#     last = M-1
# re += (N-last + 1) *(4 * 60 / s)
# print(f'{re:.12f}')

# 입력 받기
N, S_0, K = input().split()
N = int(N)
S_0 = float(S_0)
K = int(K)

# 변속 정보 입력 받기
changes = []
for _ in range(K):
    M_i, S_i = input().split()
    M_i = int(M_i)
    S_i = float(S_i)
    changes.append((M_i, S_i))

# 초기 값 설정
total_time = 0.0
current_bpm = S_0
previous_measure = 1

# 변속 처리
for M_i, S_i in changes:
    # 변속 전 구간의 마디 수 계산
    measure_count = M_i - previous_measure
    # 해당 구간의 시간 계산
    total_time += measure_count * (4 * 60 / current_bpm)
    # BPM 업데이트
    current_bpm = S_i
    # 처리한 마디를 업데이트
    previous_measure = M_i

# 마지막 변속 이후의 구간 처리
remaining_measures = N - previous_measure + 1
total_time += remaining_measures * (4 * 60 / current_bpm)

# 결과 출력
print(f'{total_time:.12f}')
