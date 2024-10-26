import sys
from collections import deque
input = sys.stdin.readline

dp = [0] * (41)
dp[0] = 1
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
m = int(input())
result = 1
start_point = 1
fixed_sit = deque([int(input()) for _ in range(m)])

while (start_point < n):
    if fixed_sit:
        now_point = fixed_sit.popleft()
        result *= dp[now_point - start_point]
        start_point = now_point + 1
    else:
        result *= dp[(n+1) - start_point]
        start_point = n

print(result)
