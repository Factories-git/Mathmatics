MOD = 10 ** 9 + 7


# 모듈러 역원을 구하는 함수
def modular_inverse(x):
    return pow(x, MOD - 2, MOD)


# 기댓값을 계산하는 함수
def calculate_expectation(p, q):
    q_inv = modular_inverse(q)
    return (p * q_inv) % MOD


# 입력 처리
Q, N = map(int, input().split())  # 라운드 수, 운영진 수
counts = list(map(int, input().split()))  # 각 운영진의 공 개수
rounds = [tuple(map(int, input().split())) for _ in range(N)]  # 라운드 범위 (l_i, r_i)

# 각 운영진의 기댓값을 저장할 배열 (N개의 운영진이 있음)
expectations = [0] * N

# 각 라운드에 대해 기댓값 계산
for l, r in rounds:
    selected_counts = counts[l - 1:r]  # 라운드에 참여한 운영진의 공 개수
    total_balls = sum(selected_counts)  # 총 공의 개수

    # 각 운영진에 대해 기댓값을 계산하고 expectations 배열에 더함
    for i in range(r - l + 1):  # l에서 r까지 참여하는 운영진
        c_i = selected_counts[i]  # 운영진 i의 공 개수
        if c_i == 0:
            continue
        # 기댓값 계산 (p_i / C * (C-1) * ...)
        p = c_i * (c_i - 1)  # 연속으로 뽑힐 확률
        q = total_balls * (total_balls - 1)
        expectations[l - 1 + i] += calculate_expectation(p, q)

# 출력
print(" ".join(map(str, expectations)))
