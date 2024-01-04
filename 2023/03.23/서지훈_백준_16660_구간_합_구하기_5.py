"""
대략 20분 소요
"""

import sys


def func():
    N, M = map(int, sys.stdin.readline().split())

    table = [[0 for i in range(N)]]

    for i in range(N):
        table.append([0] + list(map(int, sys.stdin.readline().split())))

    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + table[i][j] - dp[i-1][j-1]

    for i in range(M):
        y1, x1, y2, x2 = map(int, sys.stdin.readline().split())

        sys.stdout.write(str(dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]))
        sys.stdout.write("\n")


func()
