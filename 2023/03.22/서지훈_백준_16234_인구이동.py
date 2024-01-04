"""
10:05 시작

"""

import sys
import copy
from collections import deque


def func():
    N, L, R = map(int, sys.stdin.readline().split())
    land = []

    for i in range(N):
        land.append(list(map(int, sys.stdin.readline().split())))

    if N == 1:
        return 0

    time = 0

    while time < 2000:  # 2000일 이상은 주어지지 않음
        time += 1

        visited = [[False for i in range(N)] for j in range(N)]  # BFS로 인구 이동이 일어나는 곳을 체크하기 위함

        tmp_lands = copy.deepcopy(land)
        lands_cnt = 0  # 인구 이동에 포함된 나라의 수

        plus_x = [1, -1, 0, 0]
        plus_y = [0, 0, 1, -1]

        for i in range(N):  # 인구 이동을 할 나라가 있는지 탐색
            for j in range(N):
                if visited[i][j]: continue

                # BFS로 열려 있는 국경선끼리 인구 공유

                lands_cnt += 1

                people_sum = land[i][j]  # 국경선이 인접한 나라의 인구의 합
                country_num = 1  # 국경선이 인접한 나라의 개수
                countries = [(i, j)]

                dq = deque()
                dq.append((i, j))
                visited[i][j] = True

                # BFS를 하며 인접한 국가 탐색
                while dq:
                    tup = dq.popleft()
                    y = tup[0]
                    x = tup[1]

                    for k in range(4):
                        nx = x + plus_x[k]
                        ny = y + plus_y[k]

                        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and L <= abs(land[y][x] - land[ny][nx]) <= R:
                            visited[ny][nx] = True
                            dq.append((ny, nx))

                            people_sum += land[ny][nx]
                            country_num += 1
                            countries.append((ny, nx))

                if len(countries) == N * N:  # 모든 나라를 방문할 수 있는 경우
                    return time

                for country in countries:  # 나라 인구의 합의 평균 값을 대입
                    tmp_lands[country[0]][country[1]] = people_sum // country_num

        if lands_cnt == N * N:  # 모든 나라가 인접하지 않은 경우
            return time - 1

        land = copy.deepcopy(tmp_lands)

    if time >= 2001:
        return 0


print(func())
