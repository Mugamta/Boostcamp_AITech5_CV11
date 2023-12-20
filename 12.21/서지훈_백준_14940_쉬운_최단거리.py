import sys
from collections import deque


def func():
    n, m = map(int, sys.stdin.readline().split())

    distances = []
    visited = [[False for _ in range(m)] for _ in range(m)]
    dq = deque()

    for y in range(n):
        distances.append(list(map(int, sys.stdin.readline().split())))

    # 시작 지점 찾기
    for y in range(n):
        if dq:
            break

        for x in range(m):
            if distances[y][x] == 2:
                dq.append((x, y, 0))
                visited[y][x] = True
                distances[y][x] = 0
                break

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    # BFS
    while dq:
        x, y, cnt = dq.popleft()

        for i in range(4):
            next_x = x + plus_x[i]
            next_y = y + plus_y[i]

            if 0 > next_x or next_x >= m or 0 > next_y or next_y >= n:  # 지도를 벗어나면 건너뜀
                continue
            if visited[next_y][next_x]:  # 방문한 구역은 건너뜀
                continue
            if distances[next_y][next_x] == 0:  # 이미 최단거리가 갱신된 지점이면 건너뜀
                continue

            visited[next_y][next_x] = True
            distances[next_y][next_x] = cnt + 1
            dq.append((next_x, next_y, cnt + 1))

    for y in range(n):
        for x in range(m):
            if visited[y][x] or distances[y][x] == 0:  # 방문했거나 거리가 0이면
                sys.stdout.write(str(distances[y][x]) + " ")
            else:
                sys.stdout.write("-1 ")
        sys.stdout.write("\n")


func()
