"""
더하는 숫자의 순서가 달라지면 다른 방법으로 취급함
n은 1 + n-1, 2 + n-2, 3 + n-3의 세 가지 방법으로 만들 수 있음
마찬가지로 n-1은 1 + n-2...
"""
def func():
    dp = [0 for _ in range(1000001)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    m = 3

    for _ in range(int(input())):
        n = int(input())

        if m < n:
            for i in range(m+1, n+1):
                dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
            m = n

        print(dp[n] % 1000000009)


func()
