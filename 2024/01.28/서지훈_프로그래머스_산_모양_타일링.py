def solution(n, tops):
    dp = [[0, 0] for _ in range(n + 1)]

    dp[0][0] = 2 + tops[0]
    dp[0][1] = 1

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] * (2 + tops[i]) + dp[i - 1][1] * (1 + tops[i])
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

        dp[i][0] %= 10007
        dp[i][1] %= 10007

    answer = (dp[n - 1][0] + dp[n - 1][1]) % 10007
    
    return answer