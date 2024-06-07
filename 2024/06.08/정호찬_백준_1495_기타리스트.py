"""
    메모리 : 31120 kb
    시간 : 52 ms
"""
import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
V = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        #모든 가능한 경우 체크
        if dp[i][j]: #i번째 j 볼륨이 될 수 있다면
            if j + V[i] <= m: 
                #j + V[i]이 최대 볼륨 보다적거나 같다면
                #다음번째 j + V[i] 볼륨 가능
                dp[i + 1][j + V[i]] = 1

                #j - V[i]이 0보다 크거나 같다면
                #다음번째 j - V[i] 볼륨 가능
            if j - V[i] >= 0:
                dp[i + 1][j - V[i]] = 1

#거꾸로 탐색
for idx in range(m, -1 , -1):
    if dp[n][idx] == 1:
        print(idx)
        break
else:
    print(-1)
    