"""
https://www.acmicpc.net/problem/27211
문제 조건:
N, M이 최대 1000 -> O(NM) 혹은 O(N^2logM)등의 시간 복잡도가 가능

키워드:
N x M (2차원 배열) -> 그래프, BFS, DFS, 완전탐색, 누적합 등
상하좌우 -> BFS, DFS

실제 문제:
목표는 탐험할 수 있는 구역의 개수를 찾는 것
상하좌우로 도달할 수 없다면 서로 다른 구역
즉, 완전탐색으로 도달할 수 있는 같은 영역을 구별하고, 총 영역의 개수가 몇개인지 판단하기.
단, 도넛형(격자 밖을 벗어나면 반대쪽 끝으로 도달)이므로, 이 것에 주의해야하는 문제

따라서 완전탐색에서 약간의 변형이 주어진 것
"""

from collections import deque


def func():
    N, M = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    res = 0  # 구역의 수
    for y in range(N):
        for x in range(M):
            if planet[y][x] == 1:  # 숲으로 막혀있는 지역은 탐험 불가능
                continue

            res += 1  # 0인 곳을 찾았다면 구역을 하나 찾은 것

            dq = deque()
            dq.append((x, y))

            while dq:
                tmp_x, tmp_y = dq.popleft()

                for i in range(4):
                    nx, ny = tmp_x + plus_x[i], tmp_y + plus_y[i]

                    # 도넛 형태이므로, 범위를 벗어나면 반대쪽으로 돌아온다.
                    if nx == -1:
                        nx = M - 1
                    elif nx == M:
                        nx = 0

                    if ny == -1:
                        ny = N - 1
                    elif ny == N:
                        ny = 0

                    # 이동하려는 장소가 숲이면 이동 불가능하다.
                    if planet[ny][nx] == 1:
                        continue

                    dq.append((nx, ny))
                    planet[ny][nx] = 1  # 이동했으므로, 숲으로 바꿔주어 방문을 표기한다.

    print(res)


func()
