n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for value in values:
    for num in range(1, k + 1):
        if value <= num:
            dp[num] += dp[num - value]

print(dp[k])