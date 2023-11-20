import sys


def func():
    N, M, Q = map(int, sys.stdin.readline().split())

    fish = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 세로로 존재하는 물고기의 수를 미리 구간합으로 구해 놓는다. O(NM)
    prefix_sum = [[0 for _ in range(M)] for _ in range(N)]
    for x in range(M):
        prefix_sum[0][x] = fish[0][x]
        for y in range(1, N):
            prefix_sum[y][x] = prefix_sum[y - 1][x] + fish[y][x]

    # 이제 갂 낚시하는 위치에 대해서, 대각선으로 올라갈 때 몇 마리의 물고기가 낚이는지 계산한다. O(NM)
    dp = [[0 for _ in range(M)] for _ in range(N)]
    for x in range(M-1, -1, -1):
        dp[0][x] = fish[0][x]

    for y in range(1, N):
        for x in range(M-1, -1, -1):
            dp[y][x] = prefix_sum[y][x]
            if x >= 1:
                dp[y][x] += dp[y-1][x-1]

    # 이전 물고기를 낚은 기록은 무시되므로, 미리 구해놓은 dp를 이용한다. O(Q)
    for _ in range(Q):
        W, P = map(int, sys.stdin.readline().split())

        sys.stdout.write(str(dp[W-1][P-1]) + "\n")


func()
