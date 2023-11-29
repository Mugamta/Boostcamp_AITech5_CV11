import sys


def func():
    n = int(sys.stdin.readline())

    if n == 1:  # wine이 하나면 선택지가 없으므로 바로 출력
        print(int(sys.stdin.readline()))
        return

    wines = [0] + [int(sys.stdin.readline()) for _ in range(n)]

    # "최대"로 마실 수 있는 포도주의 양
    # "연속으로" 3개의 잔을 모두 마실 수는 "없다"
    # -> DP 문제

    # DP이므로, 점화식을 세워야 함...
    # 연속으로 3개의 잔을 마실 수 없다
    # -> 현재 잔을 마시려면, 이전 두 잔을 연속해서 마셨으면 안 된다
    # dp[1] = wines[1],
    # dp[2] = wines[1] + wines[2],
    # dp[3] = wines[1] + wines[3],
    #       wines[1] + wines[2],
    #       wines[2] + wines[3]
    # -> dp[i] = dp[i-2]  (i-1을 마시지 않음) - wines[1] + wines[3]
    #            dp[i-3] + wines[i-1] + wines[i] (i-2를 마시지 않음) - dp[0] + wines[2] + wines[3]
    #            dp[i-1] (i번째를 마시지 않음) - wines[1] + wines[2] = dp[2]

    dp = [0 for _ in range(n+1)]
    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]

    for i in range(3, n+1):
        dp[i] = max(
            dp[i-2] + wines[i],   # i-2번째까지의 최대값 + i-1 건너뜀 + i를 마심
            dp[i-3] + wines[i-1] + wines[i],   # i-3까지의 최대값 + i-2 건너뜀 + i-1, i를 마심
            dp[i-1])  # i-1번째까지의 최댓값, i를 마시지 않음

    print(max(dp))


func()
