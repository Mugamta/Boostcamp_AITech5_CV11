def func():
    s = "0" + input()

    if s[1] == '0':
        return 0

    length = len(s)

    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    dp[1] = 1

    for i in range(2, length):
        if int(s[i]) > 0:
            dp[i] = dp[i - 1]
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            dp[i] += dp[i - 2]

    return dp[length - 1] % 1000000


print(func())
