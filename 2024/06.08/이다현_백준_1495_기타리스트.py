n, s, m = map(int, input().split())  # 곡 수, 시작 볼륨, 볼륨 최대 값
lst = list(map(int, input().split()))  # 변경할 수 있는 볼륨 리스트

dp = [[0] * (m + 1) for _ in range(n + 1)]  # 곡 수만큼 볼륨 최대값까지의 변경 상태 저장

dp[0][s] = 1  # 시작볼륨 상태 1로 저장

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j] == 1:  # 이전 곡의 볼륨 상태가 가능한 경우
            min_temp = j + lst[i - 1]  # 현재 상태 j 볼륨에서 플러스
            max_temp = j - lst[i - 1]  # 현재 상태 j볼륨에서 마이너스
            if 0 <= min_temp <= m:
                dp[i][min_temp] = 1
            if 0 <= max_temp <= m:
                dp[i][max_temp] = 1

res = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        res = i
        break

print(res)
