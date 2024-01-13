from collections import deque


def func():
    N, M = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]
    time = 0

    while True:
        flag = False
        for y in range(N):
            for x in range(M):
                if cheese[y][x] == 1:  # 남아있는 치즈가 있는지
                    flag = True

        if not flag:  # 없으면 종료
            break

        time += 1
        next_cheese = [cheese[i][:] for i in range(N)]  # 우선 다음 치즈의 모양을 복사해둠

        # 치즈 내부의 공간은 외부 공기로 처리하지 않으므로, (0, 0)부터 dfs를 시작하여 외부 공기의 값을 2로 바꿈
        # 이후 값이 2인 곳의 개수를 세어 외부 공기를 카운트함
        dq = deque()
        dq.append([0, 0])
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[0][0] = True

        # BFS
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                ny = y + plus_y[i]
                nx = x + plus_x[i]

                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx] and cheese[ny][nx] == 0:  # 공기라면 탐색
                        cheese[ny][nx] = 2  # 외부 공기이므로 값을 2로 바꿈
                        dq.append([nx, ny])
                        visited[ny][nx] = True

        # 각 좌표에서 상하좌우 네 점을 살펴보며 녹아야 하는 치즈 위치 탐색
        for y in range(N):
            for x in range(M):
                air = 0
                for i in range(4):
                    ny = y + plus_y[i]
                    nx = x + plus_x[i]

                    # 좌표를 벗어나지 않으며 값이 2이면 (외부 공기이면)
                    if 0 <= nx < M and 0 <= ny < N and cheese[ny][nx] == 2:
                        air += 1

                if air >= 2:  # 두 칸 이상이 공기이면 다음 시간에서 이 치즈는 녹게 됨
                    next_cheese[y][x] = 0

        # 다음 치즈를 현재 치즈로 덮어씌움
        cheese = next_cheese[:]

    print(time)


func()
