#
# 19:47 [START]
# 19:47 prefix-sum: answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
# 19:57 [AC]
#

import sys

input = sys.stdin.readline

# Input.
N, M = map(int, input().split())
dp = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# Compute.
for i in range(1, N + 1):
    for j in range(1, N + 1):
    	dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

# Output.
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])