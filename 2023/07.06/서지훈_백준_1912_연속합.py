n = int(input())
li = [0] + list(map(int, input().split()))

dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    if dp[i-1] < 0:  # 이전까지의 합이 음수면 버리는게 나을수도 있음
        dp[i] = max(dp[i-1], li[i])
    else:
        dp[i] = dp[i-1] + li[i]  # 이전까지의 합이 음수가 아니면 현재 값을 추가로 더해줌
del dp[0]
print(max(dp))