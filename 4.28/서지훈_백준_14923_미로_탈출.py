import sys
from collections import deque


def main():
    N, M = map(int, input().split())
    Hy, Hx = map(int, input().split())
    Ey, Ex = map(int, input().split())

    Hx -= 1
    Hy -= 1
    Ex -= 1
    Ey -= 1

    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[0][Hy][Hx] = True

    dq = deque()
    dq.append((Hx, Hy, 0, 0))

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    result = N * M + 1

    while dq:
        x, y, time, flag = dq.popleft()

        if x == Ex and y == Ey:
            result = min(result, time)
            continue

        for i in range(4):
            next_x = x + plus_x[i]
            next_y = y + plus_y[i]

            if 0 <= next_x < M and 0 <= next_y < N:  # 미로 범위 이내에서 상하좌우 이동
                if flag == 1:  # 벽을 이미 부순 경우는
                    if not visited[1][next_y][next_x] and matrix[next_y][next_x] == 0:  # 빈 공간으로만 이동 가능
                        dq.append((next_x, next_y, time + 1, 1))
                        visited[1][next_y][next_x] = True

                else:  # 벽을 아직 부수지 않은 경우
                    if not visited[0][next_y][next_x]:
                        if matrix[next_y][next_x] == 1:  # 이동하려는 공간이 벽인 경우
                            dq.append((next_x, next_y, time + 1, 1))
                            visited[1][next_y][next_x] = True
                        else:
                            dq.append((next_x, next_y, time + 1, 0))
                            visited[0][next_y][next_x] = True

    if result == N * M + 1:
        return -1

    return result


print(main())