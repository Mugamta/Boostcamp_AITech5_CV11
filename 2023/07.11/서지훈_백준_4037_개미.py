"""
결국 개미가 떨어지는 가장 오랜 시간은 좌측으로 떨어진다고 가정하면 가장 우측에 있는 개미가 좌측으로 가는 것/반대방향
가장 빠른 시간은 중앙을 기준으로 개미들이 좌우로 서로 이동하는 경우 -> 즉, 가장 가운데에 가까운 개미가 떨어지는 시간
"""


import sys

for _ in range(int(input())):
    l, n = map(int, sys.stdin.readline().split())

    li = [int(sys.stdin.readline()) for _ in range(n)]

    # 최솟값 구하기 - 가장 가운데에 있는 개미가 떨어지는데 필요한 시간, 가운데에 가장 가까운 개미 탐색
    x = l
    res1 = l
    for i in li:
        if x > abs(i - abs(l - i)):
            x = abs(i - abs(l - i))
            res1 = i
    res1 = min(l - res1, res1)

    # 최댓값 구하기
    res2 = 0
    for i in li:
        if i <= l / 2:  # 중앙 기준 좌측이면
            res2 = max(res2, l - i)  # 우측으로 가기
        else:
            res2 = max(res2, i)  # 중앙 기준 우측이면 좌측으로 가기
    print(res1, res2)