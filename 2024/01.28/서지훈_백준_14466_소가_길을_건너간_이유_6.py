from collections import deque


def func():
    N, K, R = map(int, input().split())

    # N * N * 4 (상, 하, 좌, 우)의 길 존재 여부
    # 1, 1이 좌측 상단, N, N이 우측 하단
    roads = [[[False for _ in range(4)] for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(R):
        y1, x1, y2, x2 = map(int, input().split())

        if y1 < y2:  # 1이 더 위에 존재하므로, 1은 내려가고 2는 올라갈 수 있음
            roads[y1][x1][1] = True
            roads[y2][x2][0] = True
        elif y1 > y2:
            roads[y1][x1][0] = True
            roads[y2][x2][1] = True

        elif x1 < x2:  # 1이 더 좌측에 존재하므로, 1은 우측으로 갈 수 있고 2는 좌측으로 갈 수 있음
            roads[y1][x1][3] = True
            roads[y2][x2][2] = True
        elif x1 > x2:  # 1의 좌측에 2가 존재함, 2의 우측에 1이 존재함
            roads[y1][x1][2] = True
            roads[y2][x2][3] = True

    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    plus_x = [0, 0, -1, 1]
    plus_y = [-1, 1, 0, 0]

    # 길을 건너지 않고 이용할 수 있는 각 구역을 칠함
    area = 1
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if visited[y][x] == 0:  # 아직 방문하지 않은 지역이라면
                dq = deque()
                dq.append((x, y))
                visited[y][x] = area

                while dq:
                    tmp_x, tmp_y = dq.popleft()

                    for i in range(4):
                        nx = tmp_x + plus_x[i]
                        ny = tmp_y + plus_y[i]

                        # 범위를 벗어나지 않으며, 방문하지 않은 지역이며, 도로가 이어져 있지 않다면
                        if 1 <= nx <= N and 1 <= ny <= N and visited[ny][nx] == 0 and not roads[tmp_y][tmp_x][i]:
                            dq.append((nx, ny))
                            visited[ny][nx] = area

                area += 1

    # 현재 BFS를 통하여 길을 건너지 않고 지나갈 수 있는 영역들을 같은 숫자로 묶어놓음

    # 이제 같은 영역의 개수를 셈
    d = dict()
    for _ in range(K):
        y, x = map(int, input().split())
        if visited[y][x] not in d:
            d[visited[y][x]] = 1
        else:
            d[visited[y][x]] += 1

    li = list(d.values())  # 이를 리스트로 바꾸고
    res = 0  # 조합의 개수를 세줌
    for i in li:
        res += i * (K - i)  # 자기 자신을 제외하고 이후의 값들에서 가능한 조합의 경우
        K -= i  # 이미 사용한 조합 제외
    print(res)


func()
