import sys
from collections import deque


def func():
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dq, icebergs1, icebergs2 = deque(), deque(), deque()
    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    t = 0
    flag = False  # 빙산이 분리되었는지를 나타내는 변수
    while True:
        # 현존하는 빙산 위치 확인
        for y in range(N):
            for x in range(M):
                if arr[y][x] != 0:
                    icebergs1.append((x, y, arr[y][x]))

        # 더 녹을 빙산이 없다면 종료
        if len(icebergs1) == 0:  # 세 번째 실수 - 더 녹을 빙산이 없을 때 반복되어 시간초과
            break

        iceberg_num = 0  # 녹은 후의 빙산의 개수 저장 용도

        # 빙산의 위치에 대해서, 상하좌우의 0의 칸의 개수에 따라 빙산을 녹임
        while icebergs1:
            x, y, value = icebergs1.popleft()

            sea_num = 0
            for i in range(4):
                nx, ny = x + plus_x[i], y + plus_y[i]

                # 상하좌우의 0(바다)의 칸의 개수를 셈
                if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0:
                    sea_num += 1

            # 이를 별도의 배열에 저장해두되, 0보다 작으면 0이 되도록 함
            icebergs2.append((x, y, max(0, value - sea_num)))
            iceberg_num += 1 if value - sea_num >= 1 else 0

        start_x, start_y = 0, 0
        # 녹은 후 남은 빙산에 대해서, 이 값을 다시 원본 배열에 덮어씌움
        while icebergs2:
            x, y, value = icebergs2.popleft()
            arr[y][x] = value
            if value != 0:  # 첫 번째 실수
                start_x, start_y = x, y  # 빙산의 시작 위치 임의로 지정

        # ---------------- BFS로 빙산이 분리되었는지 확인 -------------

        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[start_y][start_x] = True

        # 빙산이 남아있지 않다면 시작 위치가 0, 0이므로 빙산의 개수는 0이 되며, 이외에는 시작 지점을 포함하여 1로 시작
        num = 1 if arr[start_y][start_x] != 0 else 0  # 두번째 실수
        dq.append((start_x, start_y))

        while dq:
            x, y = dq.popleft()

            for i in range(4):
                nx, ny = x + plus_x[i], y + plus_y[i]

                # BFS로 방문하지 않은 지점 (빙산)을 탐색
                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] != 0:
                    visited[ny][nx] = True
                    dq.append((nx, ny))
                    num += 1  # 빙산의 개수 체크

        t += 1

        # 전체 빙산의 개수와 BFS로 탐색한 빙산의 개수가 다르면 빙산이 분리된 것
        if num != iceberg_num:
            flag = True
            break

    if flag:
        print(t)
    else:
        print("0")


func()