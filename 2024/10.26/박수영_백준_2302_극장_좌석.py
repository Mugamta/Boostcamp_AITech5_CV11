N = int(input())
M = int(input())

prev = 0
n_seats = []
for _ in range(M):
    vip = int(input())
    n_seats.append(vip - prev - 1)
    prev = vip

n_seats.append(N - prev)

ub = max(n_seats)

dp = [0] * (N + 1)
dp[0], dp[1] = 1, 1
for i in range(2, ub + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

res = 1
for n in n_seats:
    res *= dp[n]

print(res)