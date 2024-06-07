"""
제약조건:
O(NMS) 가능

키워드:
순서대로, 최댓값, i = P +- V[i]
-> 그리디, DP, BFS 등

종합:
제약 조건이 매우 작으므로, DP나, BFS를 이용하면 풀릴 것

실제 분석:
각 곡이 변경될때마다 볼륨의 개수가 두 배씩 늘어날 수 있으나, 볼륨의 범위가 1000 이하임.
즉, 매 곡마다 큐의 최대 개수는 1000개 이하이므로 시간 내에 풀 수는 있음

-> 메모리 제한이 다른 문제와 다르게 128MB로 작음...
단순 BFS는 메모리 초과
"""


from collections import deque
from sys import stdin


def func():
    input = stdin.readline

    N, S, M = map(int, input().split())

    volumes = tuple(map(int, input().split()))

    # N개의 곡을 연주해야 한다.
    # i번째 곡은 현재 볼륨 +- volumes[i]로만 연주할 수 있다. (0 ~ M 범위 이내인 경우만 변경 가능)
    # 시작 볼륨이 S일때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값은? (0 ~ M 범위가 불가능하면 -1)

    visited = [[False] * (M + 1) for _ in range(N)]

    dq = deque()
    dq.append((S, -1))

    res = -1

    while dq:
        volume, idx = dq.popleft()

        if idx + 1 == N:
            if res < volume:
                res = volume
            continue

        if 0 <= volume + volumes[idx + 1] <= M and not visited[idx + 1][volume + volumes[idx + 1]]:
            visited[idx + 1][volume + volumes[idx + 1]] = True
            dq.append((volume + volumes[idx + 1], idx + 1))

        if 0 <= volume - volumes[idx + 1] <= M and not visited[idx + 1][volume - volumes[idx + 1]]:
            visited[idx + 1][volume - volumes[idx + 1]] = True
            dq.append((volume - volumes[idx + 1], idx + 1))

    print(res)


func()
