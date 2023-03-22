# 배열 만들고 순회하면서 더하기?


# 11시 30분 시작
# 11시 33분 제출 -> 시간초과
# 11시 47분 DP 배열 생성
# 11시 54분 인덱싱 에러 -> 55분 해결
# 11시 56분 제출 성공


import sys

N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + array[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = list(map(int, sys.stdin.readline().split()))
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)